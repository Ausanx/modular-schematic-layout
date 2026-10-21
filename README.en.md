# Modular Schematic Layout · PCB Design Guidelines

This repository provides two independent Agent Skills for electronics design:

| Skill | Use it for | Main focus |
| --- | --- | --- |
| [modular-schematic-layout](modular-schematic-layout/SKILL.md) | Drawing, generating, reorganizing, and reviewing schematics | Functional grouping, visible topology, one visual language, pagination, field ownership, and no unresolved occlusion |
| [pcb-design-guidelines](pcb-design-guidelines/SKILL.md) | PCB planning, placement, routing guidance, and board review | Constraint-driven zoning, critical loops and return paths, stackup/impedance, thermal, isolation, assembly, and manufacturing |

Install either skill independently. A complete hardware flow can use the schematic skill to preserve a confirmed connectivity baseline before the PCB skill applies component, footprint, mechanical, and fabricator constraints. Schematic readability does not replace PCB DRC, impedance, thermal, or DFM checks.

## Schematic examples

<table>
  <tr>
    <th width="50%">Before · Scattered parts and labels</th>
    <th width="50%">After · Functional blocks and visible topology</th>
  </tr>
  <tr>
    <td valign="top"><a href="modular-schematic-layout/docs/images/before.png"><img src="modular-schematic-layout/docs/images/before.png" alt="Before schematic detail" width="100%"></a></td>
    <td valign="top"><a href="modular-schematic-layout/docs/images/after.png"><img src="modular-schematic-layout/docs/images/after.png" alt="After modular schematic" width="100%"></a></td>
  </tr>
</table>

The images illustrate a change in organization. They do not prove pin-level equivalence, ERC, PCB, or manufacturing checks. The schematic skill also includes a synthetic annotation task that checks local reference/value ownership and the absence of text, symbol, wire, or page-edge occlusion in the rendered result.

## Install

Install either skill with the [Skills CLI](https://github.com/vercel-labs/skills):

~~~bash
# Schematic
npx skills add Ausanx/modular-schematic-layout --skill modular-schematic-layout

# PCB
npx skills add Ausanx/modular-schematic-layout --skill pcb-design-guidelines
~~~

Install globally for Codex:

~~~bash
npx skills add Ausanx/modular-schematic-layout --skill modular-schematic-layout --agent codex --global
npx skills add Ausanx/modular-schematic-layout --skill pcb-design-guidelines --agent codex --global
~~~

A GitHub Release also provides separate `modular-schematic-layout.skill` and `pcb-design-guidelines.skill` assets. For manual installation, copy only the selected directory with its `SKILL.md` and `references/`; do not mix the other skill or evaluation fixtures into an installation.

## Use

Schematic:

~~~text
$modular-schematic-layout
Improve this KiCad schematic's readability. Preserve the netlist, devices,
pins, and logic. Organize real paths, branches, feedback, pages, and shared
annotations; deliver editable source, rendered previews, and checks actually run.
~~~

PCB:

~~~text
$pcb-design-guidelines
Review this PCB's zoning, critical power loops, return paths, stackup,
impedance, thermal, isolation, assembly, and manufacturability. Start with
known and missing constraints, give evidence-based priorities, and distinguish
checks actually run from proposed DRC, SI, thermal, and DFM checks.
~~~

## Verification and boundaries

- Schematic evals: [modular-schematic-layout/evals](modular-schematic-layout/evals/README.md) contains eight layout, image review, SVG drawing, pagination, cross-topology style, interface mapping, and annotation-placement scenarios.
- PCB evals: [pcb-design-guidelines/evals](pcb-design-guidelines/evals/README.md) covers power-loop/return-path review, mixed-signal and high-speed constraints, and mechanical/assembly/test/fabricator limits.
- Both skills preserve confirmed networks, components, footprints, polarity, isolation, and mechanical identity. Missing data is marked as an assumption; visual neatness is not electrical evidence.
- Standards are linked as scoped references, not copied, and do not imply automatic compliance or certification. See the [schematic standards index](modular-schematic-layout/references/standards-and-sources.md) and [PCB standards index](pcb-design-guidelines/references/standards-and-sources.md).
- If ERC, DRC, field solving, thermal/current calculations, Gerber/DFM, or fabricator checks were not actually run, output must not claim they passed.

## Repository layout

~~~text
modular-schematic-layout/
├── modular-schematic-layout/
│   ├── SKILL.md
│   ├── references/
│   └── evals/
├── pcb-design-guidelines/
│   ├── SKILL.md
│   ├── references/
│   └── evals/
├── README.md
└── README.en.md
~~~

Only general skills, public examples, and synthetic evaluations are included. User project schematics, PDFs, netlists, and private reviews are not in this repository. Standards links, feedback, and releases are available in the [GitHub repository](https://github.com/Ausanx/modular-schematic-layout).
