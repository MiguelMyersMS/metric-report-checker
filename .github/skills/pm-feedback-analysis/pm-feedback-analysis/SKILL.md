---
name: pm-feedback-analysis
description: "Scenario-based analysis methodology for PM feedback on product areas, workloads, or products. Defines analysis framework, scenario extraction, prioritization, and output format."
---

# PM Feedback Analysis

Scenario-based analysis methodology for evaluating customer feedback on a product area, workload, or product. This skill is optimized for PM decision support — it goes beyond listing issues to provide scenario-grouped insights, prioritization by impact × frequency, and actionable recommendations grounded in data.

## When to Use

Load this skill when a user asks:
- "Analyze PM feedback for {product area/workload/product}"
- "What's the feedback on {product}?"
- "Should we invest in {area}?"
- "What are the main PM themes for {workload} feedback?"
- "Using the PM skill, tell me about {topic}"

## How It Differs from Feature Insight

| | Feature Insight | PM Feedback Analysis |
|---|---|---|
| **Scope** | Single feature | Product area, workload, or entire product |
| **Goal** | Evidence aggregation | PM decision support |
| **Grouping** | By source type | By usage scenario |
| **Output** | Living reference doc | Point-in-time analysis with recommendations |
| **Depth** | Wide evidence collection | Deep scenario analysis with prioritization |

## Critical Rules

1. **Always retrieve and filter raw feedback data first** — You may reason only over live Dataverse query results via `mcp_dataverse_read_query`. Never summarize or conclude without verified query results.
2. **No data = no analysis** — If the query fails or returns no rows, respond only with: *"I cannot summarize or consolidate issues because the Dataverse query returned no data. Please check the scope value and MCP server connectivity."* No reasoning, summaries, or conclusions.
3. **Default to active issues only** — Always add `AND IssueLog.statuscode = 1` unless the user explicitly asks for inactive/mitigated issues.
4. **Always show feedback count** — Report the number of feedback items included in the analysis.
5. **Redact PII** — If potential PII (person names, email addresses) appears in feedback, redact it before sharing or linking.
6. **Regional availability / GCC** — Always separately summarize any feedback regarding "regional availability" or "GCC" in its own section.
7. **Call out data richness issues** — When the dataset is thin or skewed, say so explicitly.

## Data Sources (Priority Order)

1. **CAT CRM** (Primary) — Issue reports, escalations from Dataverse. Highest confidence because they are verified, tracked, and tied to specific customers
2. **NPS / CSAT** — Verbatim feedback from Dataverse. Good for sentiment trends and volume signals
3. **Enterprise Voice** — Interview records from Dataverse. Rich qualitative signal from direct customer conversations
4. **In-product Feedback** — User-submitted feedback from Dataverse. Self-selected, so interpret volume carefully

### Source Confidence Boundaries

Always be transparent about what each source can and cannot tell you:

| Source | Strengths | Limitations |
|--------|----------|-------------|
| CAT CRM | Verified, tracked, customer-linked | Only covers CAT-engaged customers |
| NPS | Broad reach, quantitative | Low response rate, self-selected |
| Enterprise Voice | Deep qualitative insight | Small sample, specific customers |
| In-product | In-context feedback | Skews toward frustrated users |

## Analysis Workflow

### Step 1: Scope the Analysis

Parse the user's request to determine the most specific scope provided:

| User Role | Scope Level | Filter Column | Example Value |
|-----------|-------------|----------------|----------------|
| PM for Connectors | Product Area | `pbicat_productareaname` | Connectors |
| PM for OneLake | Workload | `pbicat_workloadidname` | OneLake |
| PM for Microsoft IQ | Product | `pbicat_productidname` | Microsoft IQ |

- Use the **most specific** scope provided by the user.
- If feedback lacks scope metadata, exclude it but mention it was excluded.
- If feedback spans multiple scopes, mention explicitly and ensure it is covered.
- Exclude outdated feedback from trend analysis.

### Step 2: Gather Data — Base Query

Use the following base query via `mcp_dataverse_read_query`. Add exactly **one** scope filter to the `WHERE` clause based on Step 1:

- **Product Area**: `AND IssueLog.pbicat_productareaname = '<value>'`
- **Workload**: `AND IssueLog.pbicat_workloadidname = '<value>'`
- **Product**: `AND IssueLog.pbicat_productidname = '<value>'`

For time-scoped requests (e.g., "last 4 weeks"), also add: `AND IssueLog.createdon >= '<YYYY-MM-DD>'`

By default, add `AND IssueLog.statuscode = 1` to focus on active issues only.

```sql
SELECT
  IssueLog.createdon AS ReportedDate
  ,Issue.pbicat_issueid AS IssueId
  ,IssueLog.pbicat_issuereportid AS IssueLogId
  ,Issue.pbicat_name AS IssueName
  ,Issue.pbicat_description AS IssueDescription
  ,IssueLog.pbicat_customername AS CustomerName
  ,IssueLog.pbicat_issuereportnotes AS CustomerScenario
  ,IssueLog.pbicat_issuereportpriority AS FeedbackPriority
  ,IssueLog.pbicat_feedbacktypename AS FeedbackType
  ,IssueLog.pbicat_productareaname AS ProductArea
  ,IssueLog.pbicat_workloadidname AS Workload
  ,IssueLog.pbicat_productidname AS Product
  ,IssueLog.statuscode AS IssueStatusCode
FROM pbicat_issuereport AS IssueLog
JOIN pbicat_issue AS Issue
  ON IssueLog.pbicat_issue = Issue.pbicat_issueid
WHERE IssueLog.pbicat_issue IS NOT NULL
```

**IssueStatusCode Values:**
- `1` = Active (open, unresolved)
- `2` = Inactive / Mitigated

### Additional Data Sources (Optional)

**NPS/CSAT Feedback** (wait 1-2s between queries):
```
Retrieve feedback records for {product_area/workload/product}.
Query pbicat_feedback filtering by product area or workload.
Include: source, verbatim, score, customer, date.
```

**Enterprise Voice** (wait 1-2s between queries):
```
Retrieve interaction records mentioning {topic} with Enterprise Voice type.
Include: customer, date, summary, topics.
```

### Step 3: Extract Scenarios

Group individual issues/feedback into **usage scenarios** — the real-world workflows customers are trying to accomplish.

Example: Instead of listing 15 individual API throttling issues, group them into:
- **Scenario A**: "Automated governance pipeline exceeds API rate limits during nightly refresh"
- **Scenario B**: "CI/CD deployment scripts hit 429 errors during peak hours"
- **Scenario C**: "Admin monitoring dashboard can't poll status frequently enough"

Each scenario should describe:
- What the customer is trying to do
- What goes wrong
- How many customers are affected
- How severe the impact is

**Important grouping rules:**
- Organize feedback by scenario, not individual features
- Identify recurring issues and cluster by scenario, persona, and job-to-be-done
- Highlight high-impact blockers and satisfaction detractors
- Use customer language to illustrate scenarios
- Consolidate one-off requests only if they share a common theme
- **Always separately summarize feedback regarding "regional availability" or "GCC"**

### Step 4: Prioritize

Score each scenario using **Impact × Frequency**:

| | Widespread (5+) | Common (3-4) | Occasional (1-2) |
|---|---|---|---|
| **Critical** (blocking) | P0 | P1 | P2 |
| **High** (painful workaround) | P1 | P2 | P3 |
| **Medium** (workaround ok) | P2 | P3 | P4 |
| **Low** (nice-to-have) | P3 | P4 | P5 |

### Step 5: Prioritize What Matters

Prioritize based on:
- **Breadth**: Number of customers affected
- **Depth**: Severity of impact
- Highlight blockers and adoption inhibitors
- Link feedback to strategic goals and platform-wide impact

For each prioritized scenario, provide:
1. **What**: Clear description of the scenario
2. **Who**: Which customers and how many
3. **Evidence**: Specific CRM issue titles, NPS verbatims, EV quotes
4. **Impact**: Business impact (revenue, adoption, satisfaction)
5. **Recommendation**: What PM action to take (invest, investigate, defer, monitor)

### Step 6: Provide Suggestions (Clearly Labeled as Opinions)

Offer suggestions grounded in data. **Clearly label all suggestions as opinions** using phrases like:
- "Suggestion:"
- "Potential approach:"
- "We recommend..."

Align suggestions with scenario-first thinking and product principles.

### Step 7: Generate Output

Present in chat or write to a file (based on user preference). Use the output format below.

**Response structure rules:**
- Lead with the main point
- Adjust depth based on query specificity
- Use bullet points, numbered lists, and tables for clarity
- Include examples where helpful
- Be concise but complete
- Tailor responses to the PM's context
- Ask clarifying questions only when necessary

## Output Format

```markdown
# PM Feedback Analysis — {Scope}

**Date:** {YYYY-MM-DD}
**Scope:** {Product Area / Workload / Product}
**Sources:** CAT CRM ({n} issues), NPS ({n} responses), Enterprise Voice ({n} interviews)

---

## Executive Summary

{3-5 sentence summary: key finding, top scenarios, overall sentiment direction, investment recommendation}

---

## Scenario Analysis

### Scenario 1: {Scenario Title} — Priority: {P0-P5}

**What customers are trying to do:** {description}
**What goes wrong:** {description}
**Affected customers:** {list} ({n} total)
**Severity:** {Critical/High/Medium/Low}
**Frequency:** {Widespread/Common/Occasional}

**Evidence:**
- **CAT CRM**: {issue title} (Sev {X}, {customer}) — [CRM Link if available]
- **NPS**: "{verbatim excerpt}" — {customer}, {date}
- **Enterprise Voice**: {summary of relevant interview finding}

**Business Impact:** {revenue, adoption, satisfaction impact}

**Recommendation:** {Invest / Investigate further / Defer / Monitor}

---

### Scenario 2: {Scenario Title} — Priority: {P0-P5}

{same structure as above}

---

## Trend Analysis

### Sentiment Direction
- {Overall trend: improving, declining, stable}
- {Key inflection points}

### Volume Trends
- {Issue creation rate trend}
- {Feedback volume trend}

### Gap Analysis
- {Areas with high customer interest but low investment}
- {Areas where feedback is contradictory}

---

## Source Details

### CAT CRM Issues

| # | Customer | Title | Sev | Status | Type | Scenario | Date |
|---|----------|-------|-----|--------|------|----------|------|
| 1 | {customer} | {title} | {sev} | {status} | {type} | {scenario #} | {date} |

### NPS/CSAT Verbatims

| Source | Customer | Score | Verbatim (excerpt) | Date |
|--------|----------|-------|--------------------|------|
| NPS | {customer} | {score} | "{excerpt}" | {date} |

### Enterprise Voice Highlights

| Customer | Date | Key Finding | Link to Scenario |
|----------|------|------------|-----------------|
| {customer} | {date} | {finding} | Scenario {n} |

---

## Conclusions & Recommendations

1. **{Recommendation 1}**: {rationale grounded in data}
2. **{Recommendation 2}**: {rationale}
3. **{Recommendation 3}**: {rationale}

**Confidence level:** {High/Medium/Low} — based on evidence breadth and source diversity
**Next steps:** {suggested follow-up actions}
```

## Deep Link Convention

Whenever you return individual issue rows (for cleanup, quality gate failures, rewrite candidates, consolidation targets, or any per-row output), you **must** include a direct deep link to each row in the CRM.

Use this exact URL template, substituting the GUID from the `IssueLogId` field (`pbicat_issuereportid`):

```
https://pbicat.crm.dynamics.com/main.aspx?appid=3f6ba7be-e263-eb11-a812-00224805b06b&forceUCI=1&pagetype=entityrecord&etn=pbicat_issuereport&id=<GUID>
```

**Rules:**
- The entity type is always `pbicat_issuereport` (not `pbicat_issue`)
- The `appid` is fixed: `3f6ba7be-e263-eb11-a812-00224805b06b`
- The `id` must be the exact GUID from the `IssueLogId` field — never invented or approximated
- Format the link as a named Markdown hyperlink using the customer name and issue title as the display text, e.g.:
  `[Wells Fargo — Capacity planning is too hard](https://pbicat.crm...)`
- If multiple rows belong to the same issue, link each row individually
- If potential PII (person name, email address) appears in the display text, redact it

## Anti-Patterns to Avoid

1. **Listing issues without grouping** — Always group by scenario, not just dump a table
2. **Recommendations without evidence** — Every suggestion must cite specific data points
3. **Ignoring source limitations** — Always note confidence boundaries
4. **Over-counting** — The same customer issue in CAT CRM + NPS = 1 issue from 1 customer, not 2
5. **Fabricating data** — If evidence is thin, say so. Never invent supporting data points
6. **Prioritizing by loudest customer** — Weight by breadth × depth, not volume from a single customer
7. **Treating every feature request as a requirement** — Evaluate against scenarios and product principles
8. **Violating product principles** — Don't recommend approaches that conflict with platform-level design goals
9. **Overfitting to current architecture** — Think about the ideal scenario outcome, not just what's easy to build today
10. **Including sensitive customer data** — Redact PII from all outputs
11. **Providing generic responses without data** — Every claim must be backed by query results
