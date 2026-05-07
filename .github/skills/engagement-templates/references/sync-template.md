# Sync Engagement Template

Use this template for **sync** (recurring cadence) engagement documents. Replace all `{placeholder}` values with actual data from the specialist agents.

---

```markdown
# {Customer Name} — Sync Engagement

**Date:** {YYYY-MM-DD}
**Type:** Sync
**Prepared by:** {PM Name}
**Prior Engagement:** [{prior-date}-{prior-type}.md]({prior-date}-{prior-type}.md)

---

## Prior Context

**Last engagement:** {prior-date} ({prior-type})
**Key outcome:** {one-line summary of last engagement}

### Carried-Forward Open Items

{Copy unchecked items from prior engagement's Open Items section. Mark source.}

- [ ] {Open item 1} (carried from {prior-date}-{prior-type})
- [ ] {Open item 2} (carried from {prior-date}-{prior-type})

---

## Metrics Snapshot

| Metric | Current | Prior | Delta | MoM% | YoY% | Trend |
|--------|---------|-------|-------|------|------|-------|
| Fabric MAU | {val} | {prior_val} | {delta} | {mom}% | {yoy}% | {↑/↓/→} |
| CU Hours (28d) | {val} | {prior_val} | {delta} | {mom}% | {yoy}% | {↑/↓/→} |
| ARR (MTD) | ${val} | {prior_val} | {delta} | {mom}% | {yoy}% | {↑/↓/→} |
| NPS | {val} | — | — | — | — | — |
| Active Service Requests | {val} | {prior_val} | {delta} | — | — | {↑/↓/→} |

**Notable changes:** {1-2 sentence summary of significant metric movements}

---

## What Changed

{Summary of significant changes since last engagement — new issues, resolved items, metric shifts, product launches, etc. Source: Dataverse + Work IQ}

### Recent Issues (PBI CAT)

| Title | Severity | Status | Product Area | Updated |
|-------|----------|--------|-------------|---------|
| {title} | {sev} | {status} | {area} | {date} |

### Recent Communications

{Summary of notable email threads and meetings from Work IQ}

---

## Discussion Topics

1. **{Topic 1}** — {brief context and what to discuss}
2. **{Topic 2}** — {brief context and what to discuss}
3. **{Topic 3}** — {brief context and what to discuss}

---

## Meeting Notes

{Filled in during or after the meeting}

---

## Open Items

- [ ] {Action item 1} — {Owner} — {Due date}
- [ ] {Action item 2} — {Owner} — {Due date}
```
