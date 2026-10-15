# Modular Schematic Layout

**让 AI 按功能模块与真实拓扑绘制电路原理图。**

一个面向硬件设计的 Agent Skill，指导 AI 将分散的元件和网络标签组织为可追踪的功率、信号与反馈路径。适用于原理图绘制、网表转换、布局重排和可读性审查。

中文 · [English](README.en.md) · [技能规范](SKILL.md) · [下载](https://github.com/Ausanx/modular-schematic-layout/releases/latest)

## 使用前后

<table>
  <tr>
    <th width="50%">使用前 · 元件与网络标签分散排列</th>
    <th width="50%">使用后 · 功能分框与可见拓扑</th>
  </tr>
  <tr>
    <td valign="top"><a href="docs/images/before.png"><img src="docs/images/before.png" alt="使用前的原理图局部：电容、电感和芯片分散排列，主要依靠网络标签表达连接" width="100%"></a></td>
    <td valign="top"><a href="docs/images/after.png"><img src="docs/images/after.png" alt="使用后的整页原理图：按功能分框，围绕核心芯片组织实线功率通路、反馈和垂直滤波支路" width="100%"></a></td>
  </tr>
</table>

点击图片查看原图。图一是局部视图，图二是整页视图，两者展示的是组织方式的变化；截图不作为逐器件连接等价或 ERC 通过的证明。

使用后的组织重点：

- 输入保护、电源转换、控制、接口和测试点各自成区，标题与留白帮助定位。
- 主功率通路围绕核心芯片用实线连接，反馈与滤波支路就近放置。
- 去耦电容垂直放置，使用标准电源与接地符号；跨模块控制信号保留必要的标签。

## 安装

使用 [Skills CLI](https://github.com/vercel-labs/skills) 安装，需要可用的 Node.js、npm 和 Git：

```bash
npx skills add Ausanx/modular-schematic-layout
```

安装到 Codex，供所有项目使用：

```bash
npx skills add Ausanx/modular-schematic-layout --skill modular-schematic-layout --agent codex --global
```

也可以从 [Releases](https://github.com/Ausanx/modular-schematic-layout/releases/latest) 下载 `.skill` 包，交给支持该格式的客户端导入。手动安装时，将本仓库的 `SKILL.md` 放入客户端的 `modular-schematic-layout/` 技能目录。

## 开始使用

在 Codex 中显式调用：

```text
$modular-schematic-layout
重排这份 KiCad 原理图：按功能模块分框，恢复电源级的实线拓扑，
将去耦电容改为垂直并接标准地符号。保留器件、参数和网表连接，
交付可编辑源文件、预览，以及实际执行的检查结果。
```

也可以直接描述任务，让支持技能发现的客户端按描述选择技能。提供原生文件、网表、芯片资料和目标工具版本，有助于确认连接与格式。

**从网表生成布局：**

```text
按这份已确认的网表绘制模块化原理图。输入在左、输出在右，
围绕核心 IC 组织主通路和反馈；跨模块控制信号使用端口。
先核对真实引脚定义，不要为了减少交叉改变连接。
```

**审查现有原理图：**

```text
审查这份电源原理图的可读性、标签使用和拓扑表达。
按严重程度列出器件或引脚位置、问题及具体修正建议。
区分视觉问题和需要网表确认的电气问题，先不要修改源文件。
```

## 核心规则

| 规则 | 具体要求 |
| --- | --- |
| 按功能分框 | 模块有标题、已确认的参数与清楚的边界；不按位号排成元件矩阵 |
| 显示主通路 | 输入在左、处理在中、输出在右；关键功率与信号路径使用实线 |
| 反馈就近 | 分压器垂直串联，中点直接连入反馈引脚，参考端遵循真实拓扑 |
| 符号与朝向一致 | 对地去耦、滤波电容垂直；标准接地符号朝下；保留器件极性 |
| 有节制地使用标签 | 用于跨模块、跨页或次要控制信号；不打断局部关键连接 |
| 保留电气身份 | 保留引脚号、器件值、标签作用域和不同地网；不自行添加汇接 |
| 验证后交付 | 比较引脚到网络关系；工具可用时加载工程、运行 ERC 并查看渲染预览 |

完整流程与特殊拓扑例外见 [SKILL.md](SKILL.md)。

## 适用对象与工作方式

| 对象 | 技能提供的指导 |
| --- | --- |
| KiCad、Altium、EasyEDA | 复用项目符号与真实引脚，按目标格式绘制、重排或审查 |
| 网表、SKiDl | 从连接关系确定功能分区、元件相对位置与可见拓扑 |
| SVG、Canvas | 显式表达引脚、导线、连接点、电源与接地，并与连接表对应 |
| 截图或图片 | 审查可见的布局问题，并标出无法从图像确认的连接 |

本仓库提供绘图与审图指令。实际文件生成依赖所用 Agent 的 EDA 工具、符号库或代码能力；不内置各 EDA 格式的转换器。纯 PCB 布局布线、纯参数计算和纯 SPICE 仿真不单独触发该技能。

## 检查与边界

修改现有设计时，保留“位号 + 引脚号 → 网络”的基线并在完成后比较。新设计按输入连接表核对。没有运行的检查明确标为未验证。

AGND、PGND、DGND 等不同网络不得为了版面整洁而合并。图纸可读性、截图外观或纯 SVG 预览不能代替 ERC、器件额定值、稳定性及 PCB 实现检查。

仓库包含两个可复用的[测试场景](evals/evals.json)：按已确认的抽象 Buck 连接表制定布局，以及审查标签滥用、混地与交叉走线。它们检查指令执行情况，不是原生 EDA 端到端测试或电气认证。

## 仓库结构

```text
modular-schematic-layout/
├── SKILL.md          # Agent 加载的技能规范
├── README.md         # 中文介绍
├── README.en.md      # English introduction
├── docs/images/      # 用户提供的使用前后原图
└── evals/evals.json  # 可复用测试场景
```

## 反馈与贡献

欢迎通过 [Issues](https://github.com/Ausanx/modular-schematic-layout/issues) 提供使用反馈，或提交针对规则、示例和格式兼容性的改进。报告问题时请注明目标工具与版本、预期行为，以及可以公开的最小示例。

## 介绍写法参考

README 的用途说明、安装入口与示例组织参考了 [Anthropic Skills](https://github.com/anthropics/skills)、[Superpowers](https://github.com/obra/superpowers) 和 [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills)。电路布局规范来自本项目的独立指令与示例；未复制上述项目的技能实现，也不表示它们为本项目背书。
