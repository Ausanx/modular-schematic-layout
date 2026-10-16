# Modular Schematic Layout

**Teach your AI agent to draw clear, readable circuit schematics with visible signal paths.**

An Agent Skill for hardware design. It improves functional grouping, visible wiring, page composition, spacing, and annotations while preserving the existing netlist, devices, and logic. Use it for schematic generation, netlist conversion, layout cleanup, and readability reviews.

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

## What's new in v0.2.0

- **More circuit patterns:** relay drivers, RC inputs, divider/comparator stages, gate chains, cascades, and dedicated power units now have concrete [layout guidance](references/layout-patterns.md).
- **Topology before frames:** align repeated functional channels rather than parking passive components in a separate matrix.
- **Evidence from visible wires:** a net name on a continuous wire does not make it a label jump. Distinguish named nodes, actual label jumps, and connections an image cannot resolve.
- **Page composition and typography:** arrange sheets by function and reading scale; check reference/value anchors after rotation, decoupling associations, and note placement.
- **Rendered checks:** synthetic image review and SVG drawing cases supplement the original text cases. Frames and vertical capacitors alone are insufficient acceptance criteria.

The before/after screenshots above remain early examples. This revision uses separate synthetic fixtures for testing and does not redraw that project.

## Install

Install with the [Skills CLI](https://github.com/vercel-labs/skills), using Node.js, npm, and Git:

```bash
npx skills add Ausanx/modular-schematic-layout
```

Install globally for Codex:

```bash
npx skills add Ausanx/modular-schematic-layout --skill modular-schematic-layout --agent codex --global
```

Alternatively, download the `.skill` package from [Releases](https://github.com/Ausanx/modular-schematic-layout/releases/latest) for a client that supports that format. For manual installation, copy both `SKILL.md` and `references/` into your client's `modular-schematic-layout/` skill directory.

## Use

Invoke explicitly in Codex:

```text
$modular-schematic-layout
Improve this KiCad schematic's appearance and readability. Preserve the
netlist, devices, and logic. Expose power and signal paths, arrange readable
logic chains, and improve pagination, spacing, and reference/value placement.
Deliver editable source, rendered previews, and the checks actually performed.
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
Review this schematic's readability, labels, pagination, and typography.
Trace the visible wires before deciding whether a label fragments a path.
List page/component locations, visible evidence, and concrete improvements.
Do not modify the source yet.
```

## Rules at a glance

| Rule | Expected behavior |
| --- | --- |
| Partition by function | Give each block a title, confirmed parameters, and visible space |
| Expose the main path | Arrange input, processing, and output from left to right; wire critical paths directly |
| Show logic relationships | Reuse available functional/multiunit symbols and retain complete pin mappings |
| Keep feedback nearby | Stack divider resistors vertically and wire the midpoint to the feedback pin |
| Use consistent symbols | Draw shunt capacitors vertically, point ground symbols downward, and retain polarity |
| Limit label jumps | Use them across modules, pages, or necessary controls; names on continuous wires can remain |
| Compose pages and annotations | Use function and reading scale to set density; keep text close to its symbol and retain operating notes |
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

Five reusable [test scenarios](evals/evals.json) cover a Buck layout, a text review, visual wire tracing, a two-channel logic SVG, and pagination. The visual review uses a public [synthetic fixture](evals/fixtures/labeled-paths.png). See [test instructions](evals/README.md) for procedure and limits. These cases do not guarantee satisfactory layout on every schematic and are not native EDA end-to-end validation or certification.

## Repository

```text
modular-schematic-layout/
├── SKILL.md
├── references/
├── README.md
├── README.en.md
├── docs/images/
└── evals/
```

## Feedback

Open an [issue](https://github.com/Ausanx/modular-schematic-layout/issues) or propose improvements to the rules, examples, or format guidance. Include the tool and version, expected behavior, and a minimal example you can share publicly.

## Presentation references

The README's purpose, installation, and example structure was informed by [Anthropic Skills](https://github.com/anthropics/skills), [Superpowers](https://github.com/obra/superpowers), and [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills). The circuit-layout instructions and examples belong to this project. No skill implementation was copied from those repositories, and no endorsement is implied.
