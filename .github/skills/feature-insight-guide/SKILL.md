---
name: feature-insight-guide
description: "Framework for creating feature insight documents by aggregating customer feedback from CAT CRM, NPS, Enterprise Voice, and in-product feedback. Defines source types, aggregation methodology, and output format."
---

# Feature Insight Guide

Framework for creating feature insight documents that aggregate customer feedback about a specific Fabric feature or capability. This skill guides the `@engagement-orchestrator` through multi-source data gathering, de-duplication, and synthesis into a reusable living document.

## When to Use

Load this skill when a user asks to:
- "Create a feature insight doc for {feature}"
- "Aggregate feedback on {feature}"
- "Pull all customer signals for {feature}"
- "Summarize customer feedback about {feature}"
- "What are customers saying about {feature}?"

## Evidence Sources

Feature insights are built from four primary evidence sources, in order of reliability:

| Source | Data Location | Queried By | Confidence |
|--------|--------------|------------|------------|
| **CAT CRM** (issue reports, escalations) | Dataverse (`pbicat.crm.dynamics.com`) | `dataverse` MCP | High — verified, tracked issues |
| **Enterprise Voice** (interviews) | Dataverse (`pbicat_interaction` entity) | `dataverse` MCP | High — direct customer voice |
| **NPS / CSAT** (verbatim feedback) | Dataverse (`pbicat_feedback` entity) | `dataverse` MCP | Medium — unstructured, volume-based |
| **In-product feedback** | Dataverse (`pbicat_feedback` entity) | `dataverse` MCP | Medium — self-selected respondents |

### Enterprise Voice Recordings

Full interview recordings are available at:
- **Recordings library**: [Enterprise Voice — All Fabric](https://microsoft.sharepoint.com/teams/EnterpriseVoiceStakeholders/Interview%20Recordings/Forms/All%20Fabric.aspx)

Reference this link in the Enterprise Voice section of the output document.

## Workflow

### Step 1: Identify the Feature

1. Parse the feature name from the user's request
2. Check `customer-engagement/features.yaml` for an existing entry
3. If found: read the existing insight document for prior content
4. If not found: create a new entry in `customer-engagement/features.yaml`

### Step 2: Gather Evidence

Query `dataverse` MCP with specific requests (load `dataverse-queries` skill first):

**Request 1 — CAT CRM Issues**:
```
Retrieve issue reports and escalations related to "{feature_name}".
Query pbicat_issuereport and pbicat_escalation by product area or keyword.
Include: title, severity, status, customer, description, dates.
```

**Request 2 — Enterprise Voice Interviews** (wait 1-2s after Request 1):
```
Retrieve interactions mentioning "{feature_name}".
Filter pbicat_interaction for Enterprise Voice type records.
Include: customer, date, summary, key topics.
```

**Request 3 — NPS/Feedback** (wait 1-2s after Request 2):
```
Retrieve feedback records related to "{feature_name}".
Query pbicat_feedback by product area or keyword.
Include: source type, verbatim text, score, customer, date.
```

Optionally query `powerbi-remote` MCP for adoption metrics (load `customer-360-queries` skill first):
```
Retrieve workload-level adoption metrics that map to "{feature_name}".
```

### Step 3: Aggregate and De-duplicate

1. **Cross-reference sources**: The same customer complaint may appear as a CAT issue, an NPS verbatim, and an Enterprise Voice mention
2. **De-duplicate**: Merge overlapping items into single tagged bullets with source attribution
3. **Tag each item**: Mark the source(s) — e.g., `[CAT CRM, NPS]`, `[Enterprise Voice]`

### Step 4: Classify

Group feedback into themes, then classify each theme:

**Severity Classification**:
| Level | Definition |
|-------|-----------|
| Critical | Blocking production workloads, revenue impact |
| High | Significant friction, workaround exists but painful |
| Medium | Noticeable issue, workaround available |
| Low | Minor inconvenience, nice-to-have improvement |

**Frequency Classification**:
| Level | Definition |
|-------|-----------|
| Widespread | 5+ customers, multiple sources |
| Common | 3-4 customers or strong Enterprise Voice signal |
| Occasional | 1-2 customers |

### Step 5: Generate the Document

Write to `customer-engagement/features/{feature-slug}/insight.md` using the output format below.

### Step 6: Update the Registry

If this is a new feature, add to `customer-engagement/features.yaml`:

```yaml
- name: {Feature Name}
  slug: {feature-slug}
  keywords:
    - {keyword 1}
    - {keyword 2}
  workload: {workload or "Cross-workload"}
  description: {one-line description}
  created: '{YYYY-MM-DD}'
  last_updated: '{YYYY-MM-DD}'
```

## Output Format

```markdown
# Feature Insight — {Feature Name}

**Last Updated:** {YYYY-MM-DD}
**Workload:** {workload}
**Sources Queried:** CAT CRM, Enterprise Voice, NPS, In-Product Feedback

---

## Summary

{2-3 paragraph PM-oriented summary: what customers are saying, how severe, how widespread, and what the implications are for investment decisions}

---

## CAT CRM Evidence

| # | Customer | Title | Severity | Status | Type | Created |
|---|----------|-------|----------|--------|------|---------|
| 1 | {customer} | {title} | {sev} | {status} | {Issue/Blocker/DCR} | {date} |

### Key Themes from CRM
- **{Theme 1}**: {description} ({n} customers affected) — Severity: {level}
- **{Theme 2}**: {description} ({n} customers affected) — Severity: {level}

---

## Enterprise Voice

| Customer | Date | Key Topics | Sentiment |
|----------|------|-----------|-----------|
| {customer} | {date} | {topics} | {Positive/Neutral/Negative} |

**Interview Highlights:**
- {Key verbatim or insight from interview}

📁 Full recordings: [Enterprise Voice — All Fabric](https://microsoft.sharepoint.com/teams/EnterpriseVoiceStakeholders/Interview%20Recordings/Forms/All%20Fabric.aspx)

---

## NPS Signals

| Source | Score | Customer | Verbatim (excerpt) | Date |
|--------|-------|----------|-------------------|------|
| NPS | {score} | {customer} | "{excerpt}" | {date} |

**NPS Theme Summary:**
- {Theme and direction}

---

## In-Product Feedback

{Summary of in-product feedback signals, if available}

---

## Cross-Customer Theme Summary

| Theme | Severity | Frequency | Customers | Sources |
|-------|----------|-----------|-----------|---------|
| {theme} | {Critical/High/Med/Low} | {Widespread/Common/Occasional} | {list} | {CAT, NPS, EV} |

---

## Related Customers

| Customer | Issue Count | Last Interaction | Key Concern |
|----------|------------|-----------------|-------------|
| {customer} | {n} | {date} | {one-line concern} |

---

## Notes

{Analyst notes, next steps, areas needing more data}
```

## De-duplication Rules

1. **Same customer, same issue across CAT CRM + NPS**: Merge into one bullet, tag both sources
2. **Same theme across multiple customers**: Group into a theme row in Cross-Customer Theme Summary
3. **Enterprise Voice + CAT CRM overlap**: Enterprise Voice is the richer source; use it as primary, note CAT CRM correlation
4. **Conflicting scores/sentiment**: Report both data points, flag the discrepancy
