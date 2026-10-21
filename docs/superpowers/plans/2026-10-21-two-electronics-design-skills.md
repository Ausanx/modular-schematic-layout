# Two Electronics Design Skills Implementation Plan

> **For agentic workers:** Execute this plan task by task. Steps use checkbox syntax for tracking.

**Goal:** Publish a schematic readability skill and a general PCB design guidelines skill from the same GitHub repository, each independently installable and validated.

**Architecture:** Move the existing schematic skill and its public examples under `modular-schematic-layout/`, preserving content and updating links. Add `pcb-design-guidelines/` with a focused entrypoint, standards references, and synthetic evaluations; keep repository-level READMEs as the bilingual index and release guide.

**Tech Stack:** Markdown, YAML frontmatter, JSON eval fixtures, SVG/PNG synthetic examples, Python skill validator, Git, GitHub Releases.

**Spec:** `docs/superpowers/specs/2026-10-21-two-electronics-design-skills-design.md`

## Global Constraints

- Keep the existing repository and remote `Ausanx/modular-schematic-layout`.
- Schematic guidance remains general, prioritizing readability, topology, consistent visual language, local field ownership, and zero unresolved occlusion.
- PCB guidance is constraint-driven and does not prescribe universal geometry, line width, clearance, or a single board type.
- Preserve real component, net, polarity, isolation, package, and mechanical identities; do not invent missing design inputs.
- Link standards and explain scope; do not reproduce copyrighted standards or claim certification.
- Use only existing public schematic examples and new synthetic PCB evaluation data.
- Distinguish proposed checks from checks actually run; never claim unexecuted ERC, DRC, field solving, manufacturing review, or certification.
- Verify remote tags and Releases before choosing a release version; never overwrite an existing tag or release.

## Review Focus

- Existing relative links or evaluator file paths break after moving the schematic skill; run repository-wide link and fixture checks after migration.
- Standard scope or edition is overstated; check titles, current publisher pages, and applicability notes before publishing references.
- PCB examples accidentally imply fixed values or a particular circuit/board are universal; review eval prompts and expectations for explicit constraints and unknowns.
- Skill packages accidentally include both skills or omit linked references; inspect archive contents and install each independently in a temporary directory.
- Remote release/tag already exists or the `main` branch moved; fetch and compare before push/release, and stop if non-fast-forward or version collision requires a decision.

---

### Task 1: Move the existing schematic skill into its own directory

**Files:**
- Move: `SKILL.md` → `modular-schematic-layout/SKILL.md`
- Move: `references/` → `modular-schematic-layout/references/`
- Move: `evals/` → `modular-schematic-layout/evals/`
- Move: `docs/images/` → `modular-schematic-layout/docs/images/`
- Modify: both existing READMEs into repository indexes in Task 3; update moved internal links in this task

**Interfaces:**
- Consumes: existing schematic skill, eight eval scenarios, synthetic fixtures, and public before/after images.
- Produces: a self-contained skill directory whose internal references and evaluator paths resolve from repository root.

- [x] **Step 1: Move files without changing content**

Use `git mv` for the four existing skill-owned paths. Preserve root README files and the design spec/plan under root `docs/`.

- [x] **Step 2: Update paths and verify migration**

Update relative links in the moved skill/reference/eval documentation to resolve from their new locations. Run:

```powershell
git diff --check
python -c "import json; p='modular-schematic-layout/evals/evals.json'; d=json.load(open(p,encoding='utf-8')); assert len(d['evals']) == 8; print('8 schematic evals parse')"
```

Check every `files` entry in `modular-schematic-layout/evals/evals.json` exists relative to the repository root and confirm both image screenshots exist.

### Task 2: Add the independent PCB guidelines skill and evaluations

**Files:**
- Create: `pcb-design-guidelines/SKILL.md`
- Create: `pcb-design-guidelines/references/standards-and-sources.md`
- Create: `pcb-design-guidelines/evals/README.md`
- Create: `pcb-design-guidelines/evals/evals.json`
- Create: `pcb-design-guidelines/evals/fixtures/` only for synthetic inputs needed by the evals

**Interfaces:**
- Consumes: the approved PCB skill scope and source list from the design spec.
- Produces: an independently invocable skill that can guide constrained PCB planning, layout/routing review, and evidence-based verification.

- [x] **Step 1: Write skill entrypoint**

Include a discriminating description; scope; constraint intake; placement/routing priority; reference-plane, return-path, power, thermal, isolation, assembly and test considerations; evidence limits; and a concise verification checklist. Route readers to the standards source index for exact references. Keep the entrypoint operational and avoid copying standard text.

- [x] **Step 2: Add source index with scope notes**

List IPC-2221C, IPC-2152, IPC-7351B, IPC-6012E and the approved vendor application-note examples with publisher links, applicability notes, edition caveats, and a reminder to verify current editions and actual contract/fabricator constraints. Do not turn examples into fixed universal dimensions.

- [x] **Step 3: Add three synthetic evaluations**

Create separate JSON tasks for a constrained power stage, mixed-signal/high-speed board, and manufacturing/assembly review. Each prompt must state the available constraints, expose missing high-impact inputs, and request an evidence-based plan or review without claiming native CAD/DRC completion. Expectations must test preservation of connectivity and package/mechanical facts, return paths, constraint-dependent calculations, DFM/test access, and honest reporting. Keep example values explicitly local to the synthetic task.

- [x] **Step 4: Validate the new skill and fixtures**

Run the skill validator and parse eval JSON:

```powershell
python C:\Users\Ausan\.codex\skills\.system\skill-creator\scripts\quick_validate.py pcb-design-guidelines
python -c "import json; d=json.load(open('pcb-design-guidelines/evals/evals.json',encoding='utf-8')); assert len(d['evals']) == 3; print('3 PCB evals parse')"
```

### Task 3: Rewrite bilingual root documentation for the two-skill repository

**Files:**
- Modify: `README.md`
- Modify: `README.en.md`
- Create: `docs/standards-sources.md` only if shared citation notes cannot live cleanly within each skill

**Interfaces:**
- Consumes: the two skill directories and their eval documentation.
- Produces: root-level purpose, comparison, independent install, combined workflow, validation limits, release and contribution guidance.

- [x] **Step 1: Add matching Chinese and English repository overview**

Explain when to use each skill, what is out of scope, how an approved schematic/netlist baseline feeds board design, and why schematic visual review does not validate PCB implementation. Keep content aligned across languages.

- [x] **Step 2: Document independent installation and packages**

Add Skills CLI commands that target each skill directory, confirm command syntax against the installed CLI help/docs, and document separate `.skill` assets from the same Release. Ensure manual installation tells users to copy only the chosen skill directory.

- [x] **Step 3: Preserve and relocate public examples**

Point to the migrated before/after images from the schematic README section. Keep these historical examples distinct from current acceptance evidence and link each skill's evals.

- [x] **Step 4: Check documentation paths and parity**

Verify all local README links and image links. Compare feature, install, scope, and release information between Chinese and English versions.

### Task 4: Package, validate, and publish both skills

**Files:**
- Create release assets: `modular-schematic-layout.skill`, `pcb-design-guidelines.skill`
- Modify as required: root README files and release notes only

**Interfaces:**
- Consumes: validated skill directories and repository documentation.
- Produces: two independent installable packages, a pushed `main`, and one GitHub Release containing both assets.

- [x] **Step 1: Run complete local validation**

Run `quick_validate.py` on both skill directories; parse both eval JSON files; verify every referenced fixture and local link; run `git diff --check`; inspect `git status` and `git diff --stat` for private or unrelated files.

- [x] **Step 2: Build and inspect packages**

Package each skill directory separately with its `SKILL.md` and referenced resources. Inspect archive listings and extract each into a temporary directory; rerun the validator there and confirm no other skill or user project data is present.

- [x] **Step 3: Check remote version state**

Fetch `origin`, inspect remote tags and GitHub Releases, then choose the next unused release version. If the remote branch has advanced incompatibly or the release/tag collides, stop before overwriting and report the exact conflict.

- [x] **Step 4: Commit and push the repository update**

Commit the migration, new skill, evals, and bilingual README as a focused change. Push to `origin/main` only if the branch is a fast-forward of the latest remote `main`.

- [x] **Step 5: Create the GitHub Release**

Create a release for the unused version and attach both validated `.skill` packages. Verify the release page/assets and installation links after publishing.

- [x] **Step 6: Report evidence**

Report commit, release URL, package assets, validation commands/results, and any checks not performed. Do not claim native EDA checks or certification unless they were actually run.
