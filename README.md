# Modular Schematic Layout · PCB Design Guidelines

同一仓库提供两个独立的电子设计 Agent Skill：

| Skill | 适用任务 | 核心关注 |
| --- | --- | --- |
| [modular-schematic-layout](modular-schematic-layout/SKILL.md) | 绘制、生成、重排和审查原理图 | 功能分组、拓扑可见、统一视觉语言、分页、文字归属和无遮挡 |
| [pcb-design-guidelines](pcb-design-guidelines/SKILL.md) | 从已有原理图制定逐步 PCB 施工指南，或审查 PCB | 可追溯器件/网络步骤、约束化尺寸计算、关键回路与回流、层叠/阻抗、制造和验证 |

中文 · [English](README.en.md) · [Releases](https://github.com/Ausanx/modular-schematic-layout/releases)

两项 skill 可以分别安装。完整硬件流程通常先用原理图 skill 整理已确认的连接基线，再用 PCB skill 将器件、封装、机械和板厂约束落实到板级；原理图的美观或连通表达不能替代 PCB 的 DRC、阻抗、热和 DFM 检查。

## 原理图示例

<table>
  <tr>
    <th width="50%">使用前 · 元件和标签分散</th>
    <th width="50%">使用后 · 功能分区和可见拓扑</th>
  </tr>
  <tr>
    <td valign="top"><a href="modular-schematic-layout/docs/images/before.png"><img src="modular-schematic-layout/docs/images/before.png" alt="使用前的原理图局部" width="100%"></a></td>
    <td valign="top"><a href="modular-schematic-layout/docs/images/after.png"><img src="modular-schematic-layout/docs/images/after.png" alt="使用后的模块化原理图" width="100%"></a></td>
  </tr>
</table>

图片用于展示组织方式变化，不证明逐引脚等价、ERC、PCB 或制造检查通过。原理图 skill 还包含独立合成的文字遮挡与字段归属评测，重点检查位号/数值紧随所属元件，且最终渲染没有文字、符号、导线或页边界遮挡。

## 安装

使用 [Skills CLI](https://github.com/vercel-labs/skills) 安装单项 skill：

~~~bash
# 原理图
npx skills add Ausanx/modular-schematic-layout --skill modular-schematic-layout

# PCB
npx skills add Ausanx/modular-schematic-layout --skill pcb-design-guidelines
~~~

安装到 Codex 全局目录：

~~~bash
npx skills add Ausanx/modular-schematic-layout --skill modular-schematic-layout --agent codex --global
npx skills add Ausanx/modular-schematic-layout --skill pcb-design-guidelines --agent codex --global
~~~

v0.5.0 GitHub Release 提供独立的 [modular-schematic-layout.skill](https://github.com/Ausanx/modular-schematic-layout/releases/download/v0.5.0/modular-schematic-layout.skill) 和 [pcb-design-guidelines.skill](https://github.com/Ausanx/modular-schematic-layout/releases/download/v0.5.0/pcb-design-guidelines.skill) 下载包。手动安装时，只复制所需目录及其 `SKILL.md` 和 `references/`，不要把另一个 skill 或评测夹具混入安装目录。

PCB 施工指南和线宽计算辅助脚本是在 v0.5.0 之后加入 `main` 的更新；该旧 Release 包不包含这些新内容。安装最新版请使用上面的 Skills CLI，或从仓库 `main` 复制 `pcb-design-guidelines/` 中的 `SKILL.md`、`references/` 与 `scripts/`。

## 开始使用

原理图：

~~~text
$modular-schematic-layout
优化这份 KiCad 原理图的可读性。保留网表、器件、引脚和逻辑，
按真实功能组织主路径、支路、反馈、分页与统一标注；交付可编辑源、
渲染预览和实际执行的检查结果。
~~~

PCB：

~~~text
$pcb-design-guidelines
根据这份原理图和器件/板厂资料，给我一份可照着完成 PCB 的逐步指南。
列出 RefDes、网络端点、器件邻接、每一步 CAD 操作和完成条件；对电源
线给出有来源和假设的线宽/压降计算，对阻抗和安规参数标出待确认输入。
最后列出 KiCad 9 规则设置、DRC 和制造文件验收步骤；不要声称未运行的检查通过。
~~~

## 验证与边界

- 原理图 evals：见 [modular-schematic-layout/evals](modular-schematic-layout/evals/README.md)，包含 8 个布局、图像审查、SVG 绘制、分页、跨拓扑风格、接口映射和文字避让场景。
- PCB evals：见 [pcb-design-guidelines/evals](pcb-design-guidelines/evals/README.md)，覆盖审查、完整原理图到施工指南、具体线宽/压降计算及输入不足时的局部阻断。
- 两项 skill 都要求保留用户确认的网络、器件、封装、极性、隔离和机械身份；缺少数据时标出假设，不用整齐外观替代电气证据。
- 标准只作为适用范围和验证来源，不复制标准正文，也不代表自动符合标准或完成认证。参见[原理图标准索引](modular-schematic-layout/references/standards-and-sources.md)和[PCB 标准索引](pcb-design-guidelines/references/standards-and-sources.md)。
- 没有实际运行 ERC、DRC、阻抗场求解、热/载流计算、Gerber/DFM 或板厂检查时，输出不得写成“已通过”。

## 仓库结构

~~~text
modular-schematic-layout/
├── modular-schematic-layout/
│   ├── SKILL.md
│   ├── references/
│   └── evals/
├── pcb-design-guidelines/
│   ├── SKILL.md
│   ├── references/
│   ├── scripts/
│   └── evals/
├── README.md
└── README.en.md
~~~

仓库只公开通用技能、公开示例和合成评测；用户项目原理图、PDF、网表和私人审查内容不在仓库中。标准链接、问题反馈和发布版本见 [GitHub 仓库](https://github.com/Ausanx/modular-schematic-layout)。
