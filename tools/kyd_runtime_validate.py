#!/usr/bin/env python3
import argparse, hashlib, json, re, sys
from pathlib import Path

START = "<!-- KYD_RUNTIME_DATA_START -->"
END = "<!-- KYD_RUNTIME_DATA_END -->"
PLACEHOLDER = re.compile(r"<[^<>]+>")

AUTH_KIND = {"AUTHORITY", "EVIDENCE"}
AUTH_STATUS = {"DRAFT","ACTIVE","FROZEN","SUPERSEDED","RETIRED"}
FEATURE_STATUS = {"NOT_STARTED","READY","IN_PROGRESS","IMPLEMENTED","VERIFIED","BLOCKED","DEFERRED","OUT_OF_SCOPE"}
TASK_STATUS = {"NOT_READY","READY","IN_PROGRESS","IMPLEMENTED","VERIFIED","BLOCKED","DEFERRED","CANCELLED"}
GATE_STATUS = {"NOT_RUN","PASS","FAIL","BLOCKED","NOT_APPLICABLE"}
TRACE_STATUS = {"OPEN","IMPLEMENTED","VERIFIED","BLOCKED","SUPERSEDED"}
EXECUTABLE_TASK_STATUS = {"READY","IN_PROGRESS","IMPLEMENTED"}

CORE = {
  "project_index": ("docs/PROJECT_INDEX.md","kyd.project-index.v1"),
  "current_state": ("docs/CURRENT_STATE.md","kyd.current-state.v1"),
  "feature_matrix": ("docs/product/FEATURE_MATRIX.md","kyd.feature-matrix.v1"),
  "task_index": ("docs/tasks/TASK_INDEX.md","kyd.task-index.v1"),
  "implementation_trace": ("docs/execution/IMPLEMENTATION_TRACE.md","kyd.implementation-trace.v1"),
}

class V:
    def __init__(self, root):
        self.root = Path(root).resolve()
        self.errors = []
        self.data = {}
    def err(self, cls, msg):
        self.errors.append((cls,msg))
    def load_md(self, rel, schema):
        p = self.root / rel
        if not p.is_file():
            self.err("RUNTIME_SCHEMA_INVALID", f"missing file: {rel}")
            return None
        txt = p.read_text(encoding="utf-8")
        if START not in txt or END not in txt:
            self.err("RUNTIME_SCHEMA_INVALID", f"missing Runtime JSON block: {rel}")
            return None
        raw = txt.split(START,1)[1].split(END,1)[0].strip()
        try:
            d = json.loads(raw)
        except Exception as e:
            self.err("RUNTIME_SCHEMA_INVALID", f"invalid JSON: {rel}: {e}")
            return None
        if d.get("runtime_schema") != schema:
            self.err("RUNTIME_SCHEMA_INVALID", f"{rel}: runtime_schema={d.get('runtime_schema')!r}, expected {schema}")
        if self.has_placeholder(d):
            self.err("RUNTIME_SCHEMA_INVALID", f"{rel}: unresolved <...> placeholder in machine data")
        return d
    def has_placeholder(self, obj):
        if isinstance(obj,str): return bool(PLACEHOLDER.search(obj))
        if isinstance(obj,list): return any(self.has_placeholder(x) for x in obj)
        if isinstance(obj,dict): return any(self.has_placeholder(k) or self.has_placeholder(v) for k,v in obj.items())
        return False
    def hash_file(self, rel):
        p = self.root / rel
        return hashlib.sha256(p.read_bytes()).hexdigest()
    def load(self):
        if not (self.root/"AGENTS.md").is_file():
            self.err("RUNTIME_SCHEMA_INVALID","missing file: AGENTS.md")
        for key,(rel,schema) in CORE.items():
            self.data[key] = self.load_md(rel,schema)
        cs = self.data.get("current_state")
        if cs and cs.get("current_task") not in (None,"NONE"):
            self.data["current_task"] = self.load_md("docs/tasks/CURRENT_TASK.md","kyd.current-task.v1")
    def cross_identity(self):
        vals = []
        for key,d in self.data.items():
            if isinstance(d,dict):
                vals.append((key,d.get("project"),d.get("runtime_version")))
        projects = {p for _,p,_ in vals if p}
        versions = {v for _,_,v in vals if v}
        if len(projects)>1: self.err("STATE_INCONSISTENCY",f"project mismatch: {sorted(projects)}")
        if len(versions)>1: self.err("STATE_INCONSISTENCY",f"runtime_version mismatch: {sorted(versions)}")
    def index_checks(self):
        pi = self.data.get("project_index")
        if not pi: return {}
        auths = pi.get("authorities")
        if not isinstance(auths,list):
            self.err("RUNTIME_SCHEMA_INVALID","PROJECT_INDEX.authorities must be list"); return {}
        amap={}
        for a in auths:
            if not isinstance(a,dict): self.err("RUNTIME_SCHEMA_INVALID","authority entry must be object"); continue
            aid=a.get("authority_id")
            if not aid: self.err("RUNTIME_SCHEMA_INVALID","authority_id missing"); continue
            if aid in amap: self.err("RUNTIME_SCHEMA_INVALID",f"duplicate authority_id: {aid}"); continue
            amap[aid]=a
            if a.get("kind") not in AUTH_KIND: self.err("RUNTIME_SCHEMA_INVALID",f"{aid}: invalid kind")
            if a.get("status") not in AUTH_STATUS: self.err("RUNTIME_SCHEMA_INVALID",f"{aid}: invalid status")
            if not a.get("version"): self.err("RUNTIME_SCHEMA_INVALID",f"{aid}: missing version")
            rel=a.get("path")
            if not rel or not (self.root/rel).is_file():
                self.err("AUTHORITY_GAP",f"{aid}: path missing: {rel}")
            if a.get("status")=="FROZEN":
                expected=a.get("sha256")
                if not expected:
                    self.err("AUTHORITY_GAP",f"{aid}: FROZEN without sha256")
                elif rel and (self.root/rel).is_file():
                    actual=self.hash_file(rel)
                    if actual != expected:
                        self.err("AUTHORITY_GAP",f"{aid}: FROZEN sha256 mismatch")
        return amap
    def gate_checks(self):
        cs=self.data.get("current_state")
        if not cs:return {}
        gates=cs.get("gates")
        if not isinstance(gates,list):
            self.err("RUNTIME_SCHEMA_INVALID","CURRENT_STATE.gates must be list"); return {}
        gm={}
        for g in gates:
            gid=g.get("gate_id") if isinstance(g,dict) else None
            if not gid: self.err("RUNTIME_SCHEMA_INVALID","gate_id missing"); continue
            if gid in gm: self.err("RUNTIME_SCHEMA_INVALID",f"duplicate gate_id: {gid}"); continue
            gm[gid]=g
            if g.get("status") not in GATE_STATUS: self.err("RUNTIME_SCHEMA_INVALID",f"{gid}: invalid Gate status")
            evidence=g.get("evidence",[])
            if not isinstance(evidence,list):
                self.err("RUNTIME_SCHEMA_INVALID",f"{gid}: evidence must be list")
            elif g.get("status")=="PASS" and not evidence:
                self.err("GATE_FAILURE",f"{gid}: PASS without evidence")
            elif g.get("status")=="PASS" and any(not isinstance(item,str) or not item.strip() for item in evidence):
                self.err("GATE_FAILURE",f"{gid}: PASS evidence entries must be non-empty strings")
        return gm
    def task_checks(self):
        ti=self.data.get("task_index")
        if not ti:return {},[]
        tasks=ti.get("tasks")
        if not isinstance(tasks,list):
            self.err("RUNTIME_SCHEMA_INVALID","TASK_INDEX.tasks must be list"); return {},[]
        tm={}
        graph={}
        required_contract={"goal","depends_on","authority_inputs","touches","shared_resources","gates_required","allowed_changes","forbidden_changes","acceptance","verification"}
        for t in tasks:
            tid=t.get("task_id") if isinstance(t,dict) else None
            if not tid:self.err("TASK_GAP","task_id missing");continue
            if tid in tm:self.err("TASK_GAP",f"duplicate task_id: {tid}");continue
            tm[tid]=t
            if t.get("status") not in TASK_STATUS:self.err("TASK_GAP",f"{tid}: invalid status")
            c=t.get("contract")
            if not isinstance(c,dict):
                self.err("TASK_GAP",f"{tid}: missing full contract"); graph[tid]=[]; continue
            missing=required_contract-set(c)
            if missing:self.err("TASK_GAP",f"{tid}: contract missing {sorted(missing)}")
            deps=c.get("depends_on",[])
            if not isinstance(deps,list):self.err("TASK_GAP",f"{tid}: depends_on must be list");deps=[]
            graph[tid]=deps
            for dep in deps:
                if dep not in [x.get("task_id") for x in tasks if isinstance(x,dict)]:
                    self.err("DEPENDENCY_GAP",f"{tid}: dependency does not exist: {dep}")
            for fld in ("allowed_changes","forbidden_changes","acceptance","verification"):
                if not isinstance(c.get(fld),list) or len(c.get(fld))==0:
                    self.err("TASK_GAP",f"{tid}: {fld} must be non-empty list")
            ai=c.get("authority_inputs")
            if not isinstance(ai,dict) or not isinstance(ai.get("mandatory",[]),list) or not isinstance(ai.get("reference",[]),list):
                self.err("TASK_GAP",f"{tid}: authority_inputs invalid")
            for fld in ("shared_resources","gates_required"):
                if not isinstance(c.get(fld),list): self.err("TASK_GAP",f"{tid}: {fld} must be list")
            if not isinstance(c.get("touches"),dict): self.err("TASK_GAP",f"{tid}: touches must be object")
        self.detect_cycle(graph)
        return tm,tasks
    def detect_cycle(self,graph):
        state={}
        def dfs(n,stack):
            s=state.get(n,0)
            if s==1:
                self.err("DEPENDENCY_GAP","dependency cycle: "+" -> ".join(stack+[n])); return
            if s==2:return
            state[n]=1
            for m in graph.get(n,[]):
                if m in graph: dfs(m,stack+[n])
            state[n]=2
        for n in graph: dfs(n,[])
    def feature_checks(self,amap):
        fm=self.data.get("feature_matrix")
        if not fm:return
        feats=fm.get("features")
        if not isinstance(feats,list):self.err("RUNTIME_SCHEMA_INVALID","FEATURE_MATRIX.features must be list");return
        seen=set()
        for f in feats:
            fid=f.get("feature_id") if isinstance(f,dict) else None
            if not fid:self.err("RUNTIME_SCHEMA_INVALID","feature_id missing");continue
            if fid in seen:self.err("RUNTIME_SCHEMA_INVALID",f"duplicate feature_id: {fid}")
            seen.add(fid)
            if f.get("status") not in FEATURE_STATUS:self.err("RUNTIME_SCHEMA_INVALID",f"{fid}: invalid feature status")
            for aid in f.get("authority",[]):
                if aid not in amap:self.err("AUTHORITY_GAP",f"{fid}: unknown authority: {aid}")
    def trace_checks(self,tm):
        tr=self.data.get("implementation_trace")
        if not tr:return set()
        traces=tr.get("traces")
        if not isinstance(traces,list):
            self.err("RUNTIME_SCHEMA_INVALID","IMPLEMENTATION_TRACE.traces must be list")
            return set()
        seen=set()
        verified_trace_tasks=set()
        required_fields=("trace_id","source_id","task_id","implementation","verification","evidence","status")
        for x in traces:
            xid=x.get("trace_id") if isinstance(x,dict) else None
            if not xid:self.err("TRACE_GAP","trace_id missing");continue
            if xid in seen:self.err("TRACE_GAP",f"duplicate trace_id: {xid}")
            seen.add(xid)
            missing=[field for field in required_fields if field not in x]
            if missing:self.err("TRACE_GAP",f"{xid}: missing required fields {missing}")
            if not x.get("source_id"):self.err("TRACE_GAP",f"{xid}: source_id must be non-empty")
            if not x.get("implementation"):self.err("TRACE_GAP",f"{xid}: implementation must be non-empty")
            if x.get("task_id") not in tm:self.err("TRACE_GAP",f"{xid}: unknown task_id {x.get('task_id')}")
            if x.get("status") not in TRACE_STATUS:self.err("TRACE_GAP",f"{xid}: invalid status")
            if x.get("status")=="VERIFIED":
                if not x.get("verification") or not x.get("evidence"):
                    self.err("TRACE_GAP",f"{xid}: VERIFIED without verification/evidence")
                elif not missing and x.get("source_id") and x.get("implementation") and x.get("task_id") in tm:
                    verified_trace_tasks.add(x.get("task_id"))
        for tid,t in tm.items():
            if t.get("status")=="VERIFIED" and tid not in verified_trace_tasks:
                self.err("TRACE_GAP",f"{tid}: VERIFIED task without evidence-bearing VERIFIED trace")
        return verified_trace_tasks
    def current_task_checks(self,amap,gm,tm,mode):
        cs=self.data.get("current_state")
        if not cs:return
        cur=cs.get("current_task")
        nxt=cs.get("next_task")
        if nxt not in ("NONE","BLOCKED",None) and nxt not in tm:
            self.err("STATE_INCONSISTENCY",f"next_task does not exist: {nxt}")
        if cur in ("NONE",None):
            if mode=="execution":self.err("TASK_GAP","execution mode requires current_task")
            return
        if cur not in tm:
            self.err("STATE_INCONSISTENCY",f"current_task does not exist in TASK_INDEX: {cur}");return
        ct=self.data.get("current_task")
        if not ct:return
        if ct.get("task_id") != cur:self.err("STATE_INCONSISTENCY","CURRENT_STATE.current_task != CURRENT_TASK.task_id")
        t=tm[cur]
        if ct.get("status") != t.get("status"):self.err("STATE_INCONSISTENCY","CURRENT_TASK.status != TASK_INDEX status")
        if ct.get("contract") != t.get("contract"):self.err("TASK_GAP","CURRENT_TASK.contract != TASK_INDEX preplanned contract")
        status=t.get("status")
        if mode=="execution" and status not in EXECUTABLE_TASK_STATUS:
            self.err("TASK_GAP",f"current task status not executable: {status}")
        c=t.get("contract",{})
        for dep in c.get("depends_on",[]):
            if dep in tm and tm[dep].get("status")!="VERIFIED":
                self.err("DEPENDENCY_GAP",f"{cur}: dependency {dep} status={tm[dep].get('status')}, requires VERIFIED")
        ai=c.get("authority_inputs",{})
        for kind in ("mandatory","reference"):
            for ref in ai.get(kind,[]):
                if not isinstance(ref,dict):
                    self.err("AUTHORITY_GAP",f"{cur}: {kind} authority ref must be object");continue
                aid,ver=ref.get("authority_id"),ref.get("version")
                a=amap.get(aid)
                if not a:
                    self.err("AUTHORITY_GAP",f"{cur}: unknown {kind} authority {aid}");continue
                if a.get("version") != ver:self.err("AUTHORITY_GAP",f"{cur}: {aid} version mismatch: task={ver}, index={a.get('version')}")
                if kind=="mandatory":
                    if a.get("kind")!="AUTHORITY":self.err("AUTHORITY_GAP",f"{cur}: mandatory {aid} kind must be AUTHORITY")
                    if a.get("status") not in {"ACTIVE","FROZEN"}:self.err("AUTHORITY_GAP",f"{cur}: mandatory {aid} invalid status {a.get('status')}")
                elif a.get("status")=="RETIRED":
                    self.err("AUTHORITY_GAP",f"{cur}: reference {aid} is RETIRED")
        for gid in c.get("gates_required",[]):
            g=gm.get(gid)
            if not g:self.err("GATE_FAILURE",f"{cur}: required Gate missing: {gid}")
            elif g.get("status")!="PASS":self.err("GATE_FAILURE",f"{cur}: Gate {gid} status={g.get('status')}, requires PASS")
    def run(self,mode):
        self.load()
        self.cross_identity()
        amap=self.index_checks()
        gm=self.gate_checks()
        tm,_=self.task_checks()
        self.feature_checks(amap)
        self.trace_checks(tm)
        self.current_task_checks(amap,gm,tm,mode)
        return self.errors

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--root",default=".")
    ap.add_argument("--mode",choices=["structure","execution","closeout"],default="structure")
    ap.add_argument("--hash",dest="hash_path")
    args=ap.parse_args()
    if args.hash_path:
        p=Path(args.hash_path)
        print(hashlib.sha256(p.read_bytes()).hexdigest())
        return 0
    v=V(args.root)
    errs=v.run(args.mode)
    if errs:
        print("KYD_RUNTIME_VALIDATE: FAIL")
        for cls,msg in errs: print(f"[{cls}] {msg}")
        print("EXECUTION_ALLOWED = FALSE")
        return 2
    print("KYD_RUNTIME_VALIDATE: PASS")
    print(f"MODE = {args.mode}")
    print("EXECUTION_ALLOWED = TRUE" if args.mode=="execution" else "RUNTIME_STATE_VALID = TRUE")
    return 0

if __name__=="__main__":
    sys.exit(main())
