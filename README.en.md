# Modular Schematic Layout

**Teach your AI agent to draw readable circuit schematics with a consistent visual language.**

An Agent Skill for hardware design, built around functional relationships, visible topology, and a shared visual language. It derives layouts from component roles across circuit types and reuses one project style for symbols, text, lines, spacing, and pages. Use it for schematic generation, netlist conversion, layout cleanup, and readability reviews while preserving the existing circuit.

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

## What's new in v0.4.1

- **No occlusion at delivery:** inspect all visible text, symbols, wires, and page edges using actual rendered bounds. Render again after repairs and inspect full pages and dense details.
- **Keep fields beside their component:** group references, values, and required specifications locally. Reposition them after moves, rotations, mirrors, or copies; unrelated wires and neighboring parts must not confuse ownership.
- **Rearrange crowded areas:** adjust within the shared local annotation zones, then increase nearby spacing. Do not move fields far away, shrink text, or mask conflicts. Preserve legitimate pin, junction, and label-anchor contacts.

An independent synthetic [SVG annotation task](evals/fixtures/annotation-collisions.png) checks both collisions and field ownership. The skill defines acceptance checks; generated results still require inspection. The early screenshots above do not prove compliance with this revision.

## What's new in v0.4.0

- **Organize by reading task:** overviews explain system relationships, implementation sheets expose local topology, and interface maps support pin lookup. Share a style while allowing different shapes and densities.
- **Repeat complete functions:** arrays of complete channels, connectors, or banks can aid comparison. Show actual ranges and exceptions rather than separating parts by type.
- **Choose wires and labels by role:** prefer wires for adjacent cascade stages and critical local paths; allow ports, labels, and valid buses for shared controls and dense interface maps. Preserve indices, aliases, and pin assignments.
- **Use frames where useful:** spacing, alignment, and short headings may already establish boundaries. Keep graphical frames, hierarchy symbols, and component symbols semantically distinct.
- **Make information easy to find:** identify decoupling ownership, sheet destinations, and assembly conditions; reduce repeated library-field clutter. Verify a reader can find the function, understand its local circuit, and locate the physical pin.

The general principles and shared project style remain in place. See [SKILL.md](SKILL.md), the [functional layout reference](references/layout-patterns.md), and the new [document organization reference](references/document-architecture.md). The screenshots above remain early examples. This revision adds an independently constructed planning test and does not redraw that project.

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
Create a modular schematic from this confirmed netlist. Identify paths,
branches, feedback, paired structures, and shared resources before choosing
the layout. Use clear interfaces across blocks. Preserve actual pin mappings
and reuse one project style across all sheets.
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
| Group by function | Place related parts together; repeat complete cells where useful and organize pages by reading task |
| Expose topology | Show paths, branches, feedback, pairs, and coupling in an appropriate arrangement |
| Orient by role | Use consistent treatment for paths, branches, and shared resources without forcing identical topology shapes |
| Share one visual language | Reuse symbol conventions, typography, lines, spacing, ports, frames, and color meanings across the project |
| Limit label jumps | Allow boundaries, shared controls, and dense endpoint maps; names on continuous wires can remain |
| Compose pages and annotations | Use function and reading scale to set density; keep text close to its symbol and retain operating notes |
| Prevent occlusion and detached fields | Inspect actual final bounds; keep fields locally associated with their component and recheck after transforms or copies |
| Preserve electrical identity | Retain pin numbers, values, label scopes, and distinct ground networks |
| Verify the result | Inspect rendered pages and cross-sheet consistency; compare available baselines and report checks actually performed |

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

Eight reusable [test scenarios](evals/evals.json) cover layout, text review, visual wire tracing, SVG drawing, pagination, cross-topology style, document organization with interface mapping, and actual text placement with field ownership. Images and abstract tasks are independently synthetic. See [test instructions](evals/README.md) for procedure and limits. These examples help reveal gaps; they do not validate every circuit type or constitute native EDA end-to-end validation or certification.

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
