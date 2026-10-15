# Modular Schematic Layout

**Teach your AI agent to draw circuit schematics organized around function and topology.**

An Agent Skill for hardware design. It guides schematic generation, netlist conversion, layout cleanup, and readability reviews, keeping power, signal, and feedback paths visible around their core ICs.

[中文](README.md) · English · [Skill instructions](SKILL.md) · [Download](https://github.com/Ausanx/modular-schematic-layout/releases/latest)

## Before and after

<table>
  <tr>
    <th width="50%">Before · Scattered parts and net labels</th>
    <th width="50%">After · Functional blocks and visible topology</th>
  </tr>
  <tr>
    <td valign="top"><a href="docs/images/before.png"><img src="docs/images/before.png" alt="Before: a schematic detail with scattered capacitors, inductors, and an IC connected primarily through net labels" width="100%"></a></td>
    <td valign="top"><a href="docs/images/after.png"><img src="docs/images/after.png" alt="After: a full schematic sheet organized into functional frames with visible power paths, feedback, and vertical filter branches" width="100%"></a></td>
  </tr>
</table>

Click either image to view the original. The first image is a detail and the second is a full sheet, so they illustrate a change in organization. They do not establish pin-level connectivity equivalence or an ERC pass.

- Functional frames separate input protection, conversion, control, interfaces, and test points.
- Wires expose the main power paths around the core ICs, with feedback and filtering nearby.
- Vertical decoupling branches use standard power and ground symbols; labels remain available for signals crossing module boundaries.

## Install

Install with the [Skills CLI](https://github.com/vercel-labs/skills), using Node.js, npm, and Git:

```bash
npx skills add Ausanx/modular-schematic-layout
```

Install globally for Codex:

```bash
npx skills add Ausanx/modular-schematic-layout --skill modular-schematic-layout --agent codex --global
```

Alternatively, download the `.skill` package from [Releases](https://github.com/Ausanx/modular-schematic-layout/releases/latest) for a client that supports that format. For manual installation, place `SKILL.md` in your client's `modular-schematic-layout/` skill directory.

## Use

Invoke explicitly in Codex:

```text
$modular-schematic-layout
Reorganize this KiCad schematic into functional blocks. Restore visible
power-stage wiring and vertical decoupling branches with standard ground
symbols. Preserve components, values, pin numbers, and connectivity.
Deliver editable source, a preview, and the checks actually performed.
```

You can also describe the task and let a client with skill discovery select the skill. Provide native files, a netlist, device documentation, and the target tool version when available.

**Generate from a netlist:**

```text
Create a modular schematic from this confirmed netlist. Put inputs on the
left and outputs on the right. Place the main path and feedback around the
core IC, and use ports for control signals crossing module boundaries.
Verify actual pin definitions before drawing. Preserve connectivity.
```

**Review a schematic:**

```text
Review this power schematic for readability, net-label use, and topology.
List issues by severity with component or pin locations and concrete fixes.
Distinguish visual issues from electrical concerns requiring a netlist.
Do not modify the source yet.
```

## Rules at a glance

| Rule | Expected behavior |
| --- | --- |
| Partition by function | Give each block a title, confirmed parameters, and visible space |
| Expose the main path | Arrange input, processing, and output from left to right; wire critical paths directly |
| Keep feedback nearby | Stack divider resistors vertically and wire the midpoint to the feedback pin |
| Use consistent symbols | Draw shunt capacitors vertically, point ground symbols downward, and retain polarity |
| Limit labels | Use them across modules, pages, or secondary controls without fragmenting local topology |
| Preserve electrical identity | Retain pin numbers, values, label scopes, and distinct ground networks |
| Verify the result | Compare pin-to-net membership; load, run ERC, and inspect rendered previews when tools are available |

See [SKILL.md](SKILL.md) for the full workflow and exceptions. The skill instructions are currently written in Chinese; the examples above can be used in English.

## Supported work

| Input or output | Guidance |
| --- | --- |
| KiCad, Altium, EasyEDA | Reuse project symbols and actual pin mappings while generating, reorganizing, or reviewing schematics |
| Netlists, SKiDl | Derive functional groups, relative placement, and visible topology from connections |
| SVG, Canvas | Draw explicit pins, wires, junctions, power ports, and ground symbols corresponding to a connection table |
| Screenshots | Review visible layout issues and identify connections that cannot be confirmed from the image |

This repository supplies instructions. Native file generation depends on the agent's EDA tools, symbol libraries, or coding capabilities; format converters are not bundled. PCB routing, parameter calculations, and standalone SPICE simulation are outside the skill's trigger scope.

## Verification

For existing designs, retain and compare the component-pin-to-net baseline. For new designs, check against the supplied connection table. Report checks that could not be performed.

Keep AGND, PGND, DGND, and other distinct networks separate unless the input design explicitly defines their connection. Readability, screenshots, and SVG previews do not establish electrical correctness or replace ratings, stability, and PCB checks.

Two reusable [test scenarios](evals/evals.json) cover an abstract Buck layout and a review of label misuse, ground merging, and ambiguous crossings. They exercise instruction following, rather than native EDA end-to-end validation or certification.

## Repository

```text
modular-schematic-layout/
├── SKILL.md
├── README.md
├── README.en.md
├── docs/images/
└── evals/evals.json
```

## Feedback

Open an [issue](https://github.com/Ausanx/modular-schematic-layout/issues) or propose improvements to the rules, examples, or format guidance. Include the tool and version, expected behavior, and a minimal example you can share publicly.

## Presentation references

The README's purpose, installation, and example structure was informed by [Anthropic Skills](https://github.com/anthropics/skills), [Superpowers](https://github.com/obra/superpowers), and [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills). The circuit-layout instructions and examples belong to this project. No skill implementation was copied from those repositories, and no endorsement is implied.
