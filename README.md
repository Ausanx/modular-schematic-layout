# Modular Schematic Layout

**让 AI 按通用设计原则，画出功能清楚、视觉统一的电路原理图。**

一个面向硬件设计的 Agent Skill，以功能关系、可见拓扑和统一视觉语言指导原理图绘制、网表转换、布局重排与可读性审查。适用于各类电路，按器件的实际功能角色推导布局，并在整套图纸中复用同一套符号、文字、线条、间距与分页规范；已有网表、器件和逻辑方案作为保留基线。

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

## v0.4.0 更新

- **按阅读任务组织图纸**：总览说明系统关系，局部实现展开关键拓扑，接口映射方便查针脚；共用一套样式，允许不同密度和形状。
- **重复功能可以排阵列**：复用完整通道、连接器或 Bank，标明真实范围与特例；避免将局部电路按器件种类拆散。
- **直连与标签各有位置**：相邻级联和局部关键路径优先实线，共享控制及密集接口可用端口、标签与合法总线；保留索引、别名及针号映射。
- **图框按需使用**：留白、对齐和短标题已经能区分功能时无需逐组套框；图形框、层次页符号和器件符号保持各自语义。
- **信息与导航有层级**：明确去耦归属、跨页去向及装配条件，弱化重复库字段；通过“找到功能 → 读懂局部 → 查到针脚”验收。

通用设计哲学与项目视觉规范继续保留，详见 [SKILL.md](SKILL.md)、[功能关系参考](references/layout-patterns.md) 和新增的[图纸组织与导航](references/document-architecture.md)。上方截图仍为早期示例；本次新增独立构造的多页排版方案测试，未重绘截图中的工程。

## 安装

使用 [Skills CLI](https://github.com/vercel-labs/skills) 安装，需要可用的 Node.js、npm 和 Git：

```bash
npx skills add Ausanx/modular-schematic-layout
```

安装到 Codex，供所有项目使用：

```bash
npx skills add Ausanx/modular-schematic-layout --skill modular-schematic-layout --agent codex --global
```

也可以从 [Releases](https://github.com/Ausanx/modular-schematic-layout/releases/latest) 下载 `.skill` 包，交给支持该格式的客户端导入。手动安装时，将本仓库的 `SKILL.md` 和 `references/` 一起放入客户端的 `modular-schematic-layout/` 技能目录。

## 开始使用

在 Codex 中显式调用：

```text
$modular-schematic-layout
优化这份 KiCad 原理图的美观和可读性。保留网表、芯片与逻辑方案，
按功能组织连续的功率和信号路径，展开可读的逻辑链；调整分页、
留白和位号/数值。交付可编辑源文件、渲染预览和实际检查结果。
```

也可以直接描述任务，让支持技能发现的客户端按描述选择技能。提供原生文件、网表、芯片资料和目标工具版本，有助于确认连接与格式。

**从网表生成布局：**

```text
按这份已确认的网表绘制模块化原理图。先识别主路径、支路、
反馈、成对及共享关系，再选择构图；跨模块信号用清楚的接口。
保留真实引脚映射，在整套图纸中复用同一套样式。
```

**审查现有原理图：**

```text
审查这份原理图的可读性、标签使用、分页和文字排版。
先沿导线追踪，不把带名称的连续导线误判为标签跳转。
按阅读影响列出页码、器件、可见证据和具体建议，先不要修改源文件。
```

## 核心规则

| 规则 | 具体要求 |
| --- | --- |
| 按功能分组 | 相关器件就近成组，可阵列复用完整功能单元；图框与分页服从阅读任务 |
| 让拓扑可见 | 主路径、支路、反馈、成对与耦合关系清楚；按真实结构选择构图 |
| 按角色定朝向 | 主通路、旁接支路和共享资源采用相应画法；不同电路不强求相同形状 |
| 风格全局统一 | 全项目共用一套符号、字体、线条、间距、端口、图框和颜色语义 |
| 有节制地使用标签 | 跨边界、共享控制及密集端点映射可用；连续导线上的名称可以保留 |
| 分页与标注清楚 | 按功能与阅读比例安排密度，文字靠近所属符号，必要操作说明保留 |
| 保留电气身份 | 保留引脚号、器件值、标签作用域和不同地网；不自行添加汇接 |
| 验证后交付 | 查看实际渲染和跨页一致性，比较可用的连接基线，报告实际执行的格式及电气检查 |

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

仓库包含七个可复用的[测试场景](evals/evals.json)，涵盖布局、描述审查、图像连线辨认、SVG 绘制、分页、跨拓扑风格，以及多页组织与映射方案。图像和抽象任务均为独立合成内容；运行方法与边界见[测试说明](evals/README.md)。这些样例用于发现规则缺口，不代表所有电路都已验证，也不是原生 EDA 端到端测试或电气认证。

## 仓库结构

```text
modular-schematic-layout/
├── SKILL.md          # Agent 加载的技能规范
├── references/       # 功能关系、图纸组织与导航
├── README.md         # 中文介绍
├── README.en.md      # English introduction
├── docs/images/      # 用户提供的使用前后原图
└── evals/            # 测试场景、合成图样与说明
```

## 反馈与贡献

欢迎通过 [Issues](https://github.com/Ausanx/modular-schematic-layout/issues) 提供使用反馈，或提交针对规则、示例和格式兼容性的改进。报告问题时请注明目标工具与版本、预期行为，以及可以公开的最小示例。

## 介绍写法参考

README 的用途说明、安装入口与示例组织参考了 [Anthropic Skills](https://github.com/anthropics/skills)、[Superpowers](https://github.com/obra/superpowers) 和 [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills)。电路布局规范来自本项目的独立指令与示例；未复制上述项目的技能实现，也不表示它们为本项目背书。
