# Escalation Engagement Template

Use this template for **escalation** engagement documents. Replace all `{placeholder}` values with actual data from the specialist agents.

---

```markdown
# {Customer Name} — Escalation Engagement

**Date:** {YYYY-MM-DD}
**Type:** Escalation
**Prepared by:** {PM Name}
**Prior Engagement:** [{prior-date}-{prior-type}.md]({prior-date}-{prior-type}.md)

---

## Escalation Trigger

**What happened:** {brief description of the escalation trigger}
**When:** {date the escalation started}
**Who escalated:** {person/team that raised the escalation}
**Current status:** {active/monitoring/resolved}

---

## Prior Context

**Last engagement:** {prior-date} ({prior-type})
**Escalation history:** {has this customer escalated before? when?}

### Carried-Forward Open Items

- [ ] {Open item 1} (carried from {prior-date}-{prior-type})
- [ ] {Open item 2} (carried from {prior-date}-{prior-type})

---

## Escalation Summary

**What happened:** {detailed description of the escalation — what broke, what's the impact}
**Who's involved:** {customer stakeholders, Microsoft stakeholders, engineering teams}
**Business impact:** {revenue at risk, deployment blocked, users affected}
**Timeline:**

| Date | Event | Action Taken |
|------|-------|-------------|
| {date} | {event} | {action} |

---

## Full Engagement History

{Chronological timeline of all prior engagements with this customer, with links to engagement docs}

| Date | Type | Summary | Link |
|------|------|---------|------|
| {date} | {type} | {one-line summary} | [{date}-{type}.md]({date}-{type}.md) |

---

## Email & Teams Thread Summary

### Key Threads

| Date | Subject | Sender | Key Decision/Action |
|------|---------|--------|-------------------|
| {date} | {subject} | {sender} | {decision made or action committed} |

### Decisions Log

{Chronological list of decisions made across email/Teams threads}

1. **{date}** — {decision and who made it}
2. **{date}** — {decision and who made it}

---

## Risk Signals

### NPS Trends
- {NPS direction and recent scores}
- {Verbatim feedback themes if available}

### Support Trends
- {Support case volume trend}
- {Severity distribution changes}
- {Repeat issue patterns}

### CAT Flags
- {Open blockers or high-severity issues}
- {Escalation patterns}

### Churn Indicators
- {Usage decline signals}
- {Competitive activity observed}
- {Contract/renewal timeline}

---

## Exec Relationships

| Microsoft Exec | Customer Exec | Relationship Level | Last Touchpoint |
|---------------|---------------|-------------------|-----------------|
| {name, title} | {name, title} | {Strong/Building/New} | {date and context} |

**Key relationship notes:** {who has rapport, who can unlock decisions}

---

## Current Deployment & Workloads — Full Customer 360

### Key Metrics

| Metric | Current | MoM% | YoY% | Trend |
|--------|---------|------|------|-------|
| Fabric MAU | {val} | {mom}% | {yoy}% | {↑/↓/→} |
| CU Hours (28d) | {val} | {mom}% | {yoy}% | {↑/↓/→} |
| ARR (MTD) | ${val} | {mom}% | {yoy}% | {↑/↓/→} |
| NPS | {val} | — | — | — |
| Active Service Requests | {val} | — | — | — |

### Workload Breakdown

| Workload | MAU | CU Hours | Trend |
|----------|-----|----------|-------|
| {workload 1} | {val} | {val} | {↑/↓/→} |

---

## PBI CAT Feedback

### Issue Reports

| # | Title | Severity | Status | Product Area | Created |
|---|-------|----------|--------|-------------|---------|
| 1 | {title} | {sev} | {status} | {area} | {date} |

### Escalation History

| Date | Issue | Severity | Resolution | Status |
|------|-------|----------|-----------|--------|
| {date} | {issue} | {sev} | {resolution or pending} | {resolved/open} |

### Enterprise Voice Interviews

{Summary of Enterprise Voice interview records, key themes, customer sentiment}

---

## Open Questions

- {Question about the escalation that needs resolution}
- {Question for engineering team}
- {Question for customer}

---

## Action Items

- [ ] {Action item 1} — {Owner} — {Due date}
- [ ] {Action item 2} — {Owner} — {Due date}
```
