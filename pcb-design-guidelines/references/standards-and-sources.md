# PCB 标准与一手资料索引

来源状态于 **2026-10-21** 核查。优先使用标准机构、器件/工具厂商及目标板厂的公开原始资料。IPC 页面可访问的是目录/范围信息，不是标准全文；购买或项目授权后按合同版本核对条文。引用目录、应用笔记或计算器不构成合规声明。

## IPC 标准

| 来源 | 可确认范围 | 本 skill 如何使用及边界 |
| --- | --- | --- |
| [IPC-2152, Standard for Determining Current Carrying Capacity in Printed Board Design](https://www.ipc.org/TOC/IPC-2152.pdf) | IPC 官方目录，标题与载流能力主题可核实；资料包含不同导体、板结构及环境因素的目录章节 | 载流/温升方法的主要标准参考。目录不能代替公式、曲线或全文要求；对特定板叠层按持有版本查询。 |
| [IPC-2221C, Generic Standard on Printed Board Design](https://www.electronics.org/TOC/IPC-2221C-TOC.pdf) | 官方目录显示 C 版，2023 年 12 月 | 通用设计框架；不能将其中任何某一旧经验式冒称为所有情形适用的 IPC-2152 算法。 |
| [IPC-7351B](https://www.electronics.org/TOC/IPC-7351B.pdf) | 官方公开目录/版本页 | land-pattern 方法参考；结合器件机械图、焊接工艺和封装库核对。 |
| [IPC-6012E, Qualification and Performance Specification for Rigid Printed Boards](https://www.ipc.org/TOC/IPC-6012E-toc.pdf) | 官方公开目录，E 版 | 刚性板资格/性能背景；验收等级由产品类别、合同与采购要求确定。不要从目录推断板级产品已符合。 |

## 工具与半导体厂商的工程资料

| 来源 | 资料实际范围 | 对应实践 |
| --- | --- | --- |
| [KiCad PCB Editor 9.0 文档](https://docs.kicad.org/9.0/en/pcbnew/pcbnew.html) | 官方文档：板规则、Net Class、Custom Rules、PCB 更新、铺铜及 DRC | Net Class 轨宽/过孔是布线默认/偏好值，不自动作为最小/最大 DRC 限制；要强制限制需配置规则。运行 DRC 前重新填充铜区。 |
| [KiCad PCB Calculator 9.0 文档](https://docs.kicad.org/9.0/en/pcb_calculator/pcb_calculator.html) | 官方计算器说明 | Track Width 工具所用公式源于 IPC-2221；另有过孔和传输线计算器。计算器估算不等于 IPC-2152 全文分析或板厂阻抗签核。 |
| [KiCad 9.0 Track Width 实现源码](https://github.com/KiCad/kicad-source-mirror/blob/9.0/pcb_calculator/calculator_panels/panel_track_width.cpp) | 对应公开源码含 0.048/0.024 常数、指数和 mil 单位 | 本技能脚本用其经验关系作为可追溯初估，并同时计算简单 DC 压降；不宣称实现了 IPC-2152。 |
| [TI AN-1149, Layout Guidelines for Switching Power Supplies](https://www.ti.com/lit/pdf/snva021) | TI 电源布局应用说明，当前入口转向修订 C | 输入/输出电容、电感、开关回路、反馈和接地布局的示例。具体拓扑需按对应控制器资料分析，不能将 Buck 环路模板套给所有拓扑。 |
| [TI High-Speed Layout Guidelines](https://www.ti.com/lit/pdf/scaa082) | TI SCAA082A，时钟、传输线、串扰、差分、回流、层叠和过孔等 | 依据边沿、参考层和结构分析高速信号；MHz/Gbps 不能单独决定轨宽/长度。 |
| [ADI MT-031, Grounding Data Converters and Solving the Mystery of “AGND” and “DGND”](https://www.analog.com/media/en/training-seminars/tutorials/MT-031.pdf) | ADI 官方教程 | 混合信号地按电流和回流组织；不要只从 AGND/DGND 名称推断切割平面。 |
| [ADI MT-101, Decoupling Techniques](https://www.analog.com/media/en/training-seminars/tutorials/MT-101.pdf) | ADI 官方教程 | 去耦需考虑供电/回流路径、寄生电感和器件频率特性，不硬套固定距离/电容值。 |
| [ADI AN-1119](https://www.analog.com/en/resources/app-notes/an-1119.html) | 特定双通道降压控制器的低噪声 PCB 布局指南 | 仅作对应降压电源示例；不是通用高速/模拟布局规范。 |

## 制造商能力表（条件性示例）

- [JLCPCB PCB Capabilities](https://jlcpcb.com/capabilities/pcb-capabilities)：按其铜厚、层数和工艺选项列制造能力；页面中的极限/公差只适用于标注条件，订单前重新确认，不能自动当成产品电气间距或推荐设计值。
- [PCBWay Capabilities](https://www.pcbway.com/capabilities.html)：其孔径、环宽、丝印等能力示例同样依赖制造选项；成品孔与钻头孔、板厂最小值和设计目标应分开记录。

## 决策依据和冲突处理

1. 先核对项目适用的产品/安全标准、客户合同、器件数据手册、实际叠层和制造供应商能力；把各自限制写到网络/对象规则中。
2. 线宽至少分开评估载流温升、DC 压降、信号阻抗和制造能力；没有一个单独指标能替代其余指标。载流优先查 IPC-2152 适用方法；脚本/IPC-2221 公式只是早期初估。
3. 爬电/电气间隙由适用产品要求和工作环境决定，不能从板厂最小蚀刻间距推导。标准全文不可得时明确该限制未验证，不引用未查证的条款号/尺寸。
4. 如果板厂、器件数据手册、标准和工具估算冲突，列出冲突项及其影响，使用项目适用且经授权的要求；不能通过悄悄选择一个更方便的值来消除冲突。
5. 任何目录、公开应用笔记、脚本计算或合成 eval 都不等于实际 DRC、场求解、热分析、DFM 或法规认证。
