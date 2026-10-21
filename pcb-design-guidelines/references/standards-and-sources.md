# PCB 标准与资料索引

本页只保存公开链接和适用范围提示，不复制标准正文。发布前核对出版社页面上的当前版本、修订状态、购买/访问条件和项目合同要求。

## 通用设计与制造

- [IPC-2221C](https://www.electronics.org/TOC/IPC-2221C-TOC.pdf)：通用印制板设计要求的框架性参考。具体产品、材料、环境和采购等级可能有更严格要求。
- [IPC-2152](https://www.ipc.org/TOC/IPC-2152.pdf)：导体载流与温升的设计参考。线宽不能脱离铜厚、内外层、热环境和允许温升直接套用。
- [IPC-7351B](https://www.electronics.org/TOC/IPC-7351B.pdf)：表面贴装 land pattern 设计方法参考。实际焊盘以器件厂商机械图、库验证、装配工艺和项目公差为准。
- [IPC-6012E](https://www.electronics.org/TOC/IPC-6012E-toc.pdf)：刚性印制板资格与性能要求背景。验收等级和测试要求由采购、合同、产品类别与板厂能力决定。

## 厂商应用资料示例

- [TI AN-1149](https://www.ti.com/lit/an/snva021b/snva021b.pdf)：电源布局与回路实践示例。仅适用于其讨论的电源拓扑和器件条件，不能当作所有开关电源的固定模板。
- [Analog Devices AN-1119](https://www.analog.com/en/resources/app-notes/an-1119.html)：高速/模拟布局实践参考。应结合具体转换器、信号带宽、参考平面和数据手册。
- [Infineon AP2402635](https://www.infineon.com/assets/row/public/documents/30/42/infineon-ap2402635-general-pcb-applicationnotes-en.pdf)：通用 PCB 应用说明示例。对层叠、走线和制造的建议需要按项目和供应商约束复核。

## 使用规则

1. 标准是约束和验证来源，不是自动生成一套普适坐标。
2. 先记录适用产品标准、板厂规则、材料/层叠和器件数据手册，再引用标准中的计算或间距方法。
3. 当资料冲突时，遵循项目合同、适用法规和器件/板厂明确限制，并记录取舍；不要用一条通用经验覆盖全部约束。
4. 目录页或摘要不能证明设计符合全文要求。只有实际执行并查看计算、DRC、阻抗、热或制造检查，才能报告对应检查结果。
