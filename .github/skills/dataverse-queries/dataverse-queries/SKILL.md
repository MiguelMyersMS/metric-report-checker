---
name: dataverse-queries
description: "Dataverse query patterns for the PBI CAT CRM org. Contains entity schemas, FetchXML/OData patterns, rate-limiting rules, and field mappings for issue reports, escalations, interactions, and account metadata."
---

# Dataverse Queries

Entity schemas, query patterns, and operational rules for querying the PBI CAT Dataverse CRM. This skill provides the `@dataverse-analyst` agent with entity/field references, query templates, and rate-limiting guidance.

## Dataverse Connection

- **Org URL**: `pbicat.crm.dynamics.com`
- **MCP Server**: `dataverse` (HTTP)
- **Query Tool**: `mcp_dataverse_read_query` — structured SQL-style queries
- **Fetch Tool**: `mcp_dataverse_fetch` — record lookups by ID or key

## Rate-Limiting Rules (Critical)

**Space all Dataverse queries approximately 1-2 seconds apart.**

- Execute queries sequentially, never in parallel
- If you receive a `SearchRateLimitExceeded` error, wait 3-5 seconds before retrying
- Group related data into fewer, broader queries where possible
- Minimize the number of round-trips by requesting all needed fields in a single query

## Key Entities

### Accounts (`account`)

The account entity contains customer/organization records.

| Field (Schema Name) | Display Name | Type | Description |
|---------------------|-------------|------|-------------|
| `name` | Account Name | String | Primary name of the organization |
| `accountid` | Account ID | GUID | Unique identifier |
| `pbicat_catlead` | CAT Lead | Lookup | Primary CAT team lead for this account |
| `pbicat_catou` | CAT OU | OptionSet | CAT organizational unit |
| `pbicat_accountmanager` | Account Manager | Lookup | Microsoft account manager |
| `industrycode` | Industry | OptionSet | Industry vertical |
| `pbicat_segment` | Segment | OptionSet | Customer segment |
| `pbicat_issuecount` | Issue Count | Int | Count of open issues |
| `pbicat_blockercount` | Blocker Count | Int | Count of open blockers |
| `pbicat_dcrcount` | DCR Count | Int | Count of open DCRs |
| `pbicat_ndastatus` | NDA Status | OptionSet | NDA status with the customer |

> **Note**: There is no `pbicat_tpid` column on the account entity. TPID is tracked in the Power BI semantic model (`Account[TPID]`), not in Dataverse. Use `customer-engagement/customers.yaml` to map between customer names and TPIDs.

### Issue Reports (`pbicat_issuereport`)

Issue reports track customer-reported problems and feature asks.

| Field (Schema Name) | Display Name | Type | Description |
|---------------------|-------------|------|-------------|
| `pbicat_issuereportid` | Issue Report ID | GUID | Unique identifier |
| `pbicat_name` | Title | NVARCHAR(500) | Issue title (format: `ACCOUNT \| Issue Title`) |
| `pbicat_feedbackpriority` | Priority | Choice | Low (0), Normal (1), High (2), Blocker (347870003) |
| `statecode` | State | State | Active (0), Inactive (1) |
| `pbicat_productarea` | Product Area | Lookup (GUID) | Affected product area (lookup to `pbicat_productarea`) |
| `pbicat_workloadid` | Workload | Lookup (GUID) | Affected workload (lookup to `pbicat_featureclass`) |
| `pbicat_customer` | Customer | Lookup (GUID) | Related account (lookup to `account`) — **NOT** `pbicat_account` |
| `pbicat_issuereportnotes` | Notes | Text Area | Detailed description — **NOT** `pbicat_description` |
| `pbicat_feedbacktype` | Feedback Type | Choice | Product (347870000), Satisfaction Detractor (347870001) |
| `pbicat_reportdate` | Report Date | Date | When the issue was reported |
| `pbicat_issue` | Issue | Lookup (GUID) | Related issue record (lookup to `pbicat_issue`) |
| `pbicat_mauimpact` | MAU Impact | Int | Estimated MAU impact |
| `pbicat_fabricflag` | Fabric Flag | Bit | Whether this is a Fabric-related issue |
| `pbicat_issuemitigated` | Issue Mitigated | Bit | Whether the issue has been mitigated |
| `createdon` | Created On | DateTime | When the report was filed |
| `modifiedon` | Modified On | DateTime | Last update |

> **Common mistakes**: The field is `pbicat_feedbackpriority` not `pbicat_severity`. The field is `pbicat_issuereportnotes` not `pbicat_description`. The lookup is `pbicat_customer` not `pbicat_account` or `_pbicat_account_value`. The type field is `pbicat_feedbacktype` not `pbicat_type`. The status is `statecode` not `pbicat_status`.

### Escalations (`pbicat_escalation`)

Escalation records track formally escalated customer issues.

| Field (Schema Name) | Display Name | Type | Description |
|---------------------|-------------|------|-------------|
| `pbicat_escalationid` | Escalation ID | GUID | Unique identifier |
| `pbicat_name` | Title | NVARCHAR(850) | Escalation title |
| `pbicat_escalationseverity` | Severity | Choice | Sev 3 - moderate (347870000), Sev 2 - major (347870001), Sev 1 - critical (347870002) |
| `pbicat_escalationstatus` | Status | Choice | Request under review (347870004), Redirected (347870005), Pre-escalation (347870000), Active (347870001), Contained (347870002), Transitioning off (347870003), Closed (347870006) |
| `pbicat_customer` | Customer | Lookup (GUID) | Related account (lookup to `account`) — **NOT** `pbicat_account` |
| `pbicat_executivesummary` | Executive Summary | Multiline Text | Detailed description — **NOT** `pbicat_description` |
| `pbicat_customerimpact` | Customer Impact | Choice | Blocking product selection/POC (347870000), Blocking production (347870001), Production impacts (347870002) |
| `pbicat_startdate` | Start Date | Date | When escalation began |
| `pbicat_enddate` | End Date | Date | When escalation ended |
| `pbicat_catescalationlead` | CAT Escalation Lead | Lookup | Lead from CAT team |
| `pbicat_fieldescalationlead` | Field Escalation Lead | Lookup | Lead from field team |
| `pbicat_product` | Product | Lookup (GUID) | Related product (lookup to `pbicat_product`) |
| `pbicat_escalationdoc` | Escalation Doc | URL | Link to escalation document |
| `pbicat_ongoingengagement` | Ongoing Engagement | Choice | No (347870000), Yes (347870001) |
| `statecode` | State | State | Active (0), Inactive (1) |
| `createdon` | Created On | DateTime | When escalation was raised |
| `modifiedon` | Modified On | DateTime | Last update |

> **Common mistakes**: The field is `pbicat_escalationseverity` not `pbicat_severity`. The field is `pbicat_escalationstatus` not `pbicat_status`. The description field is `pbicat_executivesummary` not `pbicat_description`. There is no `pbicat_resolution` field. The lookup is `pbicat_customer` not `pbicat_account`.

### Interactions (`pbicat_interaction`)

Interaction records capture meetings, calls, and Enterprise Voice interviews.

| Field (Schema Name) | Display Name | Type | Description |
|---------------------|-------------|------|-------------|
| `pbicat_interactionid` | Interaction ID | GUID | Unique identifier |
| `pbicat_name` | Title | NVARCHAR(150) | Interaction title (format: `YYYYMMDD - Type - ACCOUNT - Contact`) |
| `pbicat_interactiontype` | Interaction Type | Choice | Enterprise Voice Interview (768190001), Partner Voice (768190002), ISV Voice (768190003), Escalation (347870001), Customer Meeting (347870002), Interview (347870000), Email (347870003), Private Preview Feedback (768190004), Go Big Interview (347870004), and others |
| `pbicat_customer` | Customer | Lookup (GUID) | Related account (lookup to `account`) — **NOT** `pbicat_account` |
| `pbicat_date` | Date | Date | When it occurred |
| `pbicat_description` | Description | Text Area | Short description of the interaction |
| `pbicat_detailnotes` | Detail Notes | Multiline Text | Detailed notes from the interaction |
| `pbicat_pbicatproduct` | Product | Lookup (GUID) | Related product (lookup to `pbicat_product`) |
| `pbicat_contactid` | Contact | Lookup (GUID) | Customer contact (lookup to `contact`) |
| `pbicat_meetingrecording` | Meeting Recording | URL | Link to recording |
| `pbicat_onenotelink` | OneNote Link | URL | Link to OneNote page |
| `new_customerengagementtype` | Engagement Type | Choice | Various engagement types |
| `pbicat_cabscore` | CAB Score | Int | Customer Advisory Board score |
| `statecode` | State | State | Active (0), Inactive (1) |
| `createdon` | Created On | DateTime | Record creation date |

> **Common mistakes**: The type field is `pbicat_interactiontype` not `pbicat_type`. The lookup is `pbicat_customer` not `pbicat_account`. There are no `pbicat_participants`, `pbicat_summary`, or `pbicat_topics` fields. Use `pbicat_description` and `pbicat_detailnotes` instead.

**Enterprise Voice interviews** are stored in this entity with `pbicat_interactiontype = 768190001`. Flag these prominently when retrieving interactions.

### Feedback (`pbicat_feedback`)

Customer feedback records (NPS, CSAT, in-product).

| Field (Schema Name) | Display Name | Type | Description |
|---------------------|-------------|------|-------------|
| `pbicat_feedbackid` | Feedback ID | GUID | Unique identifier |
| `pbicat_source` | Source | OptionSet | NPS/CSAT/In-Product/Enterprise Voice |
| `pbicat_account` | Account | Lookup | Related account |
| `pbicat_verbatim` | Verbatim | Memo | Customer's own words |
| `pbicat_score` | Score | Int | Numeric score (NPS: -100 to 100) |
| `pbicat_productarea` | Product Area | OptionSet | Affected product area |
| `pbicat_workload` | Workload | OptionSet | Affected workload |
| `createdon` | Created On | DateTime | When feedback was received |

## Common Query Patterns

### CAT Lead Lookup

Find the CAT lead for a customer account:

```sql
SELECT name, pbicat_catlead, pbicat_catou, pbicat_accountmanager,
       industrycode, pbicat_segment, pbicat_issuecount,
       pbicat_blockercount, pbicat_dcrcount, pbicat_ndastatus
FROM account
WHERE name = '{customer_name}'
```

If exact name doesn't match, try a `LIKE` filter:

```sql
SELECT name, accountid, pbicat_issuecount, pbicat_blockercount, pbicat_dcrcount
FROM account
WHERE name LIKE '%{customer_name}%'
```

### Issue Reports for a Customer

Retrieve all active issue reports ordered by priority and date:

```sql
SELECT TOP 20 pbicat_name, pbicat_feedbackpriority, statecode,
       pbicat_productarea, pbicat_issuereportnotes,
       pbicat_reportdate, modifiedon
FROM pbicat_issuereport
WHERE pbicat_customer = '{account_id}' AND statecode = 0
ORDER BY modifiedon DESC
```

### Issue Reports by Product Area (for Feature Insight / PM Analysis)

```sql
SELECT TOP 20 pbicat_name, pbicat_feedbackpriority, statecode,
       pbicat_productarea, pbicat_issuereportnotes, createdon
FROM pbicat_issuereport
WHERE pbicat_productarea = '{product_area_guid}' AND statecode = 0
ORDER BY createdon DESC
```

### Escalations for a Customer

```sql
SELECT pbicat_name, pbicat_escalationseverity, pbicat_escalationstatus,
       pbicat_executivesummary, pbicat_startdate, modifiedon
FROM pbicat_escalation
WHERE pbicat_customer = '{account_id}'
ORDER BY modifiedon DESC
```

### Interactions for a Customer (Including Enterprise Voice)

```sql
SELECT TOP 10 pbicat_name, pbicat_interactiontype, pbicat_date,
       pbicat_description
FROM pbicat_interaction
WHERE pbicat_customer = '{account_id}'
ORDER BY pbicat_date DESC
```

### Feedback by Product Area (for Feature Insight)

> **Note**: Verify `pbicat_feedback` field names with `mcp_dataverse_describe_table` before querying — this entity has not been validated against the live schema yet.

```sql
SELECT pbicat_source, pbicat_verbatim, pbicat_score,
       pbicat_productarea, pbicat_workload, createdon
FROM pbicat_feedback
WHERE pbicat_productarea = '{product_area_guid}'
ORDER BY createdon DESC
```

### Feedback by Customer

```sql
SELECT pbicat_source, pbicat_verbatim, pbicat_score,
       pbicat_productarea, pbicat_workload, createdon
FROM pbicat_feedback
WHERE pbicat_customer = '{account_id}'
ORDER BY createdon DESC
```

## Account ID Resolution

Most queries filter by `pbicat_customer` (the lookup field to the account entity). To get the account ID:

1. First query the `account` entity by name to get the `accountid`:
   ```sql
   SELECT accountid, name, pbicat_issuecount, pbicat_blockercount, pbicat_dcrcount
   FROM account
   WHERE name LIKE '%{customer_name}%'
   ```
2. Then use that `accountid` as `pbicat_customer` in subsequent queries
3. Remember to wait 1-2 seconds between these queries

> **Important**: The lookup field is `pbicat_customer` in SQL queries, not `_pbicat_account_value`. The `_pbicat_account_value` syntax is for OData/FetchXML, not SQL.

## Result Formatting

### Issue Report Table

```markdown
| # | Title | Severity | Status | Product Area | Created | Last Updated |
|---|-------|----------|--------|-------------|---------|-------------|
| 1 | {title} | {sev} | {status} | {area} | {date} | {date} |
```

### CAT Lead Card

```markdown
| Field | Value |
|-------|-------|
| CAT Lead | {name} |
| CAT OU | {ou} |
| Account Manager | {name} |
| Industry | {industry} |
| Segment | {segment} |
| Open Issues | {count} |
| Open Blockers | {count} |
| Open DCRs | {count} |
| NDA Status | {status} |
```

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| `SearchRateLimitExceeded` | Too many queries too fast | Wait 3-5 seconds, then retry with spacing |
| Empty results | Account name mismatch | Try `contains` filter, check `customer-engagement/customers.yaml` for aliases |
| Field not found | Schema name incorrect | Verify with `mcp_dataverse_fetch` on a known record |
| Lookup field empty | Related record not linked | Query the related entity directly |
