---
name: engagement-templates
description: "Templates and formatting rules for customer engagement documents — syncs, EBCs, and escalations. Defines document structure, required sections, and formatting conventions for each engagement type."
---

# Engagement Templates

Templates and formatting rules for generating customer engagement documents. This skill defines the document structure, required sections, and formatting conventions for each of the three engagement types: sync, EBC, and escalation.

## When to Use

Load this skill when the `@engagement-orchestrator` is generating an engagement document (Step 6 of the engagement preparation workflow).

## Engagement Types

| Type | Depth | Use When |
|------|-------|----------|
| **sync** | Lightweight | Recurring customer cadence — quick metric update and context refresh |
| **ebc** | Full | Executive Briefing Center visit — comprehensive prep with competitive and stakeholder analysis |
| **escalation** | Deep | Active escalation — full history, risk signals, exec relationships |

## Template Selection Logic

1. Parse the engagement type from the user's request:
   - Keywords `sync`, `cadence`, `check-in`, `recurring` → **sync**
   - Keywords `ebc`, `executive briefing`, `briefing center` → **ebc**
   - Keywords `escalation`, `escalate`, `critical`, `sev a` → **escalation**
2. If unclear, ask the user which type to use
3. Load the full template from the appropriate reference file

## Full Templates

The complete templates with all sections and placeholder syntax are in the references subdirectory:

- [Sync Template](references/sync-template.md) — Lightweight recurring cadence document
- [EBC Template](references/ebc-template.md) — Full Executive Briefing Center document
- [Escalation Template](references/escalation-template.md) — Deep escalation document

## Formatting Conventions

### General Rules

1. **Markdown only** — All engagement docs are `.md` files
2. **ISO 8601 dates** — Always use `YYYY-MM-DD` format
3. **Actual customer names** — Use "L'Oréal", not "loreal". Only strip filesystem-unsafe characters for file/folder names
4. **File naming** — `{YYYY-MM-DD}-{type}.md` (e.g., `2026-03-26-sync.md`)
5. **Location** — Save to `customer-engagement/customers/{Customer Name}/engagements/`

### Heading Hierarchy

- `#` — Document title (e.g., `# Nokia — Sync Engagement`)
- `##` — Major sections (e.g., `## Metrics Snapshot`, `## Discussion Topics`)
- `###` — Subsections (e.g., `### Workload Breakdown`)

### Metric Presentation

Always present metrics in tables with growth context:

```markdown
| Metric | Current | MoM% | YoY% | Trend |
|--------|---------|------|------|-------|
| Fabric MAU | 12,450 | +3.2% | +18.7% | ↑ |
```

Trend indicators:
- `↑` — Growth (positive MoM)
- `↓` — Decline (negative MoM)
- `→` — Stable (MoM within ±1%)

### Action Items

Format all action items as checkboxes:

```markdown
- [ ] {Action description} — {Owner} — {Due date if known}
```

### Prior Context Links

Every engagement document must link to the previous engagement:

```markdown
**Prior Engagement:** [2026-03-10-sync.md](2026-03-10-sync.md)
```

### Open Items Carry-Forward

When carrying forward items from a prior engagement:
1. Copy unchecked `- [ ]` items from the prior doc's Open Items section
2. Mark them with the source: `(carried from {date}-{type})`
3. If an item has been resolved, mark it `- [x]` in the prior doc

## Section-by-Section Guidance

### Sync Documents

Syncs are lightweight — focus on what changed since the last engagement:
- Metric deltas (not full tables — just what moved)
- Recent emails/meetings context
- Carried-forward open items
- 2-3 discussion topics

### EBC Documents

EBCs are comprehensive — the PM needs a complete picture:
- Full Customer 360 with workload-level breakdown
- Competitive landscape (who else is the customer using, positioning)
- Stakeholder profiles with decision authority and relationship history
- Crafted talking points (what to say, what to avoid)
- Prep documents and resources

### Escalation Documents

Escalations are the deepest — capture the full timeline and risk:
- Complete engagement history (chronological timeline of all prior interactions)
- Email/Teams thread summary with decision log
- Risk signals (NPS decline, support trends, CAT flags, churn indicators)
- Exec relationships (who knows whom at Microsoft, last touchpoint)
- Full C360 and PBI CAT feedback
