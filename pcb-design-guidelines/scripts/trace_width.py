#!/usr/bin/env python3
"""Estimate rectangular PCB trace width from legacy thermal and DC drop limits.

Thermal equation matches the IPC-2221 empirical relation used by KiCad 9's
Track Width calculator. This is a screening estimate, not IPC-2152 analysis.
"""

import argparse
import math
import sys


MIL_TO_MM = 0.0254
COPPER_RESISTIVITY_20C_OHM_M = 1.72e-8
THERMAL_K = {"external": 0.048, "internal": 0.024}


def estimate(current_a, copper_um, layer, delta_t_c, length_mm=None,
             max_drop_mv=None, fab_min_mm=0.0):
    if (length_mm is None) != (max_drop_mv is None):
        raise ValueError("length_mm 与 max_drop_mv 必须同时提供")
    values = [current_a, copper_um, delta_t_c, fab_min_mm]
    if length_mm is not None:
        values.extend((length_mm, max_drop_mv))
    if not all(math.isfinite(value) for value in values):
        raise ValueError("输入必须是有限数值")
    if current_a <= 0 or copper_um <= 0 or delta_t_c <= 0:
        raise ValueError("电流、铜厚和允许温升必须大于 0")
    if fab_min_mm < 0:
        raise ValueError("板厂最小线宽不能小于 0")
    if layer not in THERMAL_K:
        raise ValueError("layer 必须是 external 或 internal")
    if length_mm is not None and (length_mm <= 0 or max_drop_mv <= 0):
        raise ValueError("长度和允许压降必须大于 0")

    thickness_mil = copper_um / 25.4
    area_mil2 = (current_a / (THERMAL_K[layer] * delta_t_c ** 0.44)) ** (1 / 0.725)
    thermal_mm = area_mil2 / thickness_mil * MIL_TO_MM
    drop_mm = None
    if length_mm is not None:
        thickness_m = copper_um * 1e-6
        drop_v = max_drop_mv / 1000
        drop_mm = (
            COPPER_RESISTIVITY_20C_OHM_M * (length_mm / 1000) * current_a
            / (thickness_m * drop_v) * 1000
        )

    selected_mm = max(thermal_mm, drop_mm or 0.0, fab_min_mm)
    result = {
        "area_mil2": area_mil2,
        "thermal_mm": thermal_mm,
        "drop_mm": drop_mm,
        "selected_mm": selected_mm,
        "resistance_20c_ohm": None,
        "voltage_drop_20c_mv": None,
        "power_20c_w": None,
    }
    if length_mm is not None:
        resistance = (
            COPPER_RESISTIVITY_20C_OHM_M * (length_mm / 1000)
            / ((selected_mm / 1000) * (copper_um * 1e-6))
        )
        result["resistance_20c_ohm"] = resistance
        result["voltage_drop_20c_mv"] = current_a * resistance * 1000
        result["power_20c_w"] = current_a**2 * resistance
    return result


def self_test():
    base = estimate(1, 35, "external", 10)
    assert 0.29 < base["thermal_mm"] < 0.31, base
    internal = estimate(1, 35, "internal", 10)
    assert internal["thermal_mm"] > base["thermal_mm"], internal
    higher_current = estimate(2, 35, "external", 10)
    assert higher_current["thermal_mm"] > base["thermal_mm"], higher_current
    drop = estimate(1, 35, "external", 10, 50, 50, 0.15)
    assert 0.48 < drop["drop_mm"] < 0.50, drop
    assert abs(drop["selected_mm"] - drop["drop_mm"]) < 1e-12, drop
    assert drop["voltage_drop_20c_mv"] <= 50.001, drop
    for bad in (
        (0, 35, "external", 10, None, None, 0),
        (1, 35, "external", 10, 50, None, 0),
        (1, 35, "bad-layer", 10, None, None, 0),
    ):
        try:
            estimate(*bad)
        except ValueError:
            continue
        raise AssertionError(f"invalid input was accepted: {bad}")
    return "self-test passed"


def main():
    parser = argparse.ArgumentParser(
        description="初估均匀矩形 PCB 铜线的温升宽度和直流压降宽度。",
        epilog=(
            "结果不是 IPC-2152、阻抗、热仿真或制造符合性结论；"
            "另行检查过孔、颈缩、脉冲、温度和板厂公差。"
        ),
    )
    parser.add_argument("--current-a", type=float, help="该段设计电流，A")
    parser.add_argument("--copper-um", type=float, help="该层有效铜厚，µm")
    parser.add_argument("--layer", choices=THERMAL_K, help="external 或 internal")
    parser.add_argument("--delta-t-c", type=float, help="允许温升，°C")
    parser.add_argument("--length-mm", type=float, help="均匀直线长度，mm；须与 max-drop 同用")
    parser.add_argument("--max-drop-mv", type=float, help="该段允许 DC 压降，mV；须与 length 同用")
    parser.add_argument("--fab-min-mm", type=float, default=0.0, help="板厂适用最小线宽，mm")
    parser.add_argument("--self-test", action="store_true", help="运行公式趋势和已知算例检查")
    args = parser.parse_args()

    if args.self_test:
        print(self_test())
        return 0
    required = (args.current_a, args.copper_um, args.layer, args.delta_t_c)
    if any(value is None for value in required):
        parser.error("除非使用 --self-test，否则须提供 current-a、copper-um、layer 和 delta-t-c")
    try:
        result = estimate(
            args.current_a, args.copper_um, args.layer, args.delta_t_c,
            args.length_mm, args.max_drop_mv, args.fab_min_mm,
        )
    except ValueError as error:
        parser.error(str(error))

    print("模型：KiCad 9 Track Width calculator 使用的旧 IPC-2221 经验式 + 20 °C 铜电阻率 DC 压降")
    print(f"温升初估线宽：{result['thermal_mm']:.3f} mm ({result['thermal_mm'] / MIL_TO_MM:.1f} mil)")
    if result["drop_mm"] is not None:
        print(f"压降约束线宽：{result['drop_mm']:.3f} mm ({result['drop_mm'] / MIL_TO_MM:.1f} mil)")
    print(f"给定板厂最小线宽：{args.fab_min_mm:.3f} mm")
    print(f"约束取大后的初选最小宽度：{result['selected_mm']:.3f} mm")
    if result["resistance_20c_ohm"] is not None:
        print(f"该宽度的 20 °C DC 电阻/压降/耗散：{result['resistance_20c_ohm']:.4f} Ω / "
              f"{result['voltage_drop_20c_mv']:.2f} mV / {result['power_20c_w']:.4f} W")
    print("将设计值向上取到板厂与 CAD 支持的规格；评估温度系数、瞬态、回流、过孔和电流拥挤。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
