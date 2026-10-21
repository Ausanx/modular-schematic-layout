# PCB skill 测试说明

evals.json 包含三个与具体用户项目无关的合成任务。每个任务的 prompt 和 files 是给待测 Agent 的输入；expected_output 与 expectations 只用于独立审查，不放入任务提示。

| ID | 检查重点 | 输出 |
| --- | --- | --- |
| 1 | 电源级的高 di/dt 回路、去耦、回流和约束化建议 | power-review.md |
| 2 | 混合信号/高速分区、参考平面、阻抗和返回路径 | mixed-signal-plan.md |
| 3 | 板框、连接器、装配、测试和板厂 DFM 限制 | manufacturing-review.md |

这些任务评价推理和证据边界，不代表完成原生 CAD 修改、DRC、阻抗场求解、热分析、Gerber 检查或认证。合成参数只在对应任务中有效，不能被抽象成全局线宽、间距或层叠规则。
