# Kyd Project System

## 新项目初始化（Kyd Bootstrap）

### 适用场景

本指南使用当前仓库中的 Bootstrap 工具，把 Kyd 项目管理和执行控制文件安装到一个新的项目目录。Bootstrap 不实现、也不修改业务功能。

目前没有全局安装的 `kyd bootstrap` 命令。initializer 必须通过 Python 从包含 Bootstrap 工具的 Kyd 模板/项目系统仓库中运行。

当前已验证的流程适用于干净的目标目录，或不存在 Kyd 管理路径冲突的目录。

### 1. 设置路径

建议始终使用绝对路径：

```bash
KYD_TEMPLATE=/absolute/path/to/Kyd-Project-System
NEW_PROJECT=/absolute/path/to/my-new-project
PROJECT_ID=my-new-project
```

- `KYD_TEMPLATE`：包含 `tools/kyd-bootstrap/init_project.py` 的 Kyd 模板/项目系统仓库。
- `NEW_PROJECT`：要初始化的目标项目目录。
- `PROJECT_ID`：目标项目的稳定标识，只能使用字母、数字、点、下划线和连字符。

`--target ./my-new-project` 是相对于当前 shell 工作目录的路径，容易创建到或指向错误的位置，因此强烈建议为 `NEW_PROJECT` 使用绝对路径。

### 2. 执行初始化

```bash
cd "$KYD_TEMPLATE"

python3 tools/kyd-bootstrap/init_project.py \
  --project-id "$PROJECT_ID" \
  --target "$NEW_PROJECT"
```

初始化成功后，目标项目会实际包含：

```text
AGENTS.md
KYD_BOOTSTRAP_MANIFEST.json
docs/PROJECT_INDEX.md
docs/CURRENT_STATE.md
docs/delivery-protocol/*
docs/kyd-runtime/*
docs/product/FEATURE_MATRIX.md
docs/tasks/TASK_INDEX.md
docs/tasks/CURRENT_TASK.md
docs/execution/IMPLEMENTATION_TRACE.md
tools/kyd_runtime_validate.py
tools/kyd_bootstrap_validate.py
```

这些文件构成 Kyd 项目管理和执行控制层，不会添加业务实现。

### 3. 验证初始化结果

进入目标项目并运行：

```bash
cd "$NEW_PROJECT"

python3 tools/kyd_runtime_validate.py --root . --mode structure
python3 tools/kyd_runtime_validate.py --root . --mode closeout
python3 tools/kyd_bootstrap_validate.py --root .
```

以上三个命令应通过。还可以检查执行资格：

```bash
python3 tools/kyd_runtime_validate.py --root . --mode execution
```

新项目此时不应具备执行资格。因为 `CURRENT_STATE.current_task = NONE`，execution 模式预期会拒绝或不允许执行。这是正确且安全的零状态，不表示 Bootstrap 失败。

### 4. 启动 Codex

```bash
cd "$NEW_PROJECT"
codex
```

Codex 在目标项目中启动后，会读取并遵循：

```text
AGENTS.md
→ docs/PROJECT_INDEX.md
→ docs/CURRENT_STATE.md
→ docs/tasks/CURRENT_TASK.md
```

新初始化的项目应得出结论：当前没有可执行任务，不要开始实现。后续 Product Authority、仓库审计或实现任务必须先被明确建立并注册。仅创建项目目录或启动 Codex 不会自动运行 Bootstrap。

### 已有代码项目的重要限制

当前 Bootstrap 已验证的是干净目标目录或没有 Kyd 管理路径冲突的目录，并采用 fail-closed 行为。

如果先复制已有模板（例如 `sa-template`）到 `NEW_PROJECT`，是否能够直接接入取决于目标目录中是否已经存在 Kyd 管理路径，例如：

```text
AGENTS.md
docs/PROJECT_INDEX.md
docs/CURRENT_STATE.md
docs/tasks/*
tools/kyd_runtime_validate.py
```

如果这些路径已存在，当前 initializer 可能会拒绝覆盖。不要为了让 Bootstrap 通过而手工删除或覆盖已有文件。“已有代码仓库安全接入 Kyd”目前不是 clean-target Bootstrap 已验证能力。

### 初始化完成后项目处于什么状态

成功完成 Bootstrap 后：

```text
current task = NONE
no active executable task
implementation execution eligibility = FALSE
no inherited project history
no Product-Specific Authority yet
Bootstrap validation = PASS
```
