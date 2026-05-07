---
name: customer-360-queries
description: "DAX query patterns for the Azure Data Insights Power BI semantic model. Contains metric definitions, query templates, growth calculations (MoM%, YoY%), and data interpretation guidance for Customer 360 lookups."
---

# Customer 360 Queries

DAX query patterns and metric definitions for the Azure Data Insights Power BI semantic model. This skill provides the `@customer-360` agent with ready-to-use query templates, growth calculation patterns, and output formatting guidance.

## Semantic Model Reference

- **Model Name**: Azure Data Insights
- **Artifact ID**: `27b59ca8-3fcf-47ee-9db3-f05f0f2b4188`
- **MCP Server**: `powerbi-remote` (HTTP)
- **Execute Tool**: `mcp_powerbi-remot_ExecuteQuery`
- **Schema Tool**: `mcp_powerbi-remot_GetSemanticModelSchema`

## Before You Query

1. **Discover the schema first**: On first use or when encountering column errors, run `mcp_powerbi-remot_GetSemanticModelSchema` with the artifact ID to get available tables and columns.
2. **Use the `account` field from `customer-engagement/customers.yaml`**: The model uses legal/official account names, not common names. Always check `customer-engagement/customers.yaml` for the correct `account` value.
3. **TPID is the primary key**: Filter by TPID (Top Parent ID) wherever possible for accurate results.

## Core DAX Query Patterns

### Account Lookup (TPID Resolution)

Use this when you have a customer name but need the TPID, or to verify the account exists in the model.

```dax
EVALUATE
SUMMARIZECOLUMNS(
  'Account'[Account],
  'Account'[TPID],
  FILTER('Account', SEARCH("{account_name}", 'Account'[Account], 1, 0) > 0)
)
```

Note: The `Account` table uses `Account` (not `AccountName`) for the display name and `TPID` for the top parent ID. The surrogate key is `DIM_TPID`. There is also an `Account TPID` column formatted as "Account Name (TPID)".

If the customer name doesn't match, try the `account` field from `customer-engagement/customers.yaml` (legal name may differ from common name).

### Fabric MAU (28-day)

Monthly Active Users for Fabric, with MoM and YoY context.

```dax
EVALUATE
SUMMARIZECOLUMNS(
  'Calendar'[Fiscal Month],
  'Calendar'[Fiscal Year],
  TREATAS({{"{{tpid}}"}}, 'Account'[TPID]),
  "MAU", [Fabric MAU (28d)]
)
ORDER BY 'Calendar'[Fiscal Year] DESC, 'Calendar'[Fiscal Month] DESC
```

**Important**: `SUMMARIZECOLUMNS` requires a measure (like `[Fabric MAU (28d)]`) for cross-table `TREATAS` to work. Do not use `TREATAS` with only calculated columns — it will fail silently or return empty results.

Note: The date dimension table is `Calendar` (not `Date`). Use `Fiscal Month` and `Fiscal Year` for time-series grouping. Use `FiscalMonthId` for sorting if needed.

### Fabric MAU (non-rolling)

```dax
EVALUATE
SUMMARIZECOLUMNS(
  'Calendar'[Fiscal Month],
  'Calendar'[Fiscal Year],
  TREATAS({{"{{tpid}}"}}, 'Account'[TPID]),
  "MAU", [Fabric MAU]
)
ORDER BY 'Calendar'[Fiscal Year] DESC, 'Calendar'[Fiscal Month] DESC
```

Additional MAU measures available: `[Fabric MAU PM]` (prior month), `[Fabric MAU YoY %]` (year-over-year percentage).

### Capacity Unit Hours (28-day)

```dax
EVALUATE
SUMMARIZECOLUMNS(
  'Calendar'[Fiscal Month],
  'Calendar'[Fiscal Year],
  TREATAS({{"{{tpid}}"}}, 'Account'[TPID]),
  "CU_Hours", [CU Hours (28d)]
)
ORDER BY 'Calendar'[Fiscal Year] DESC, 'Calendar'[Fiscal Month] DESC
```

Additional CU measures: `[CU Hours]` (total), `[CU Hours (7d)]` (7-day rolling), `[Interactive CU Hours]`, `[Background CU Hours]`.

### Revenue / ARR (MTD)

```dax
EVALUATE
SUMMARIZECOLUMNS(
  'Calendar'[Fiscal Month],
  'Calendar'[Fiscal Year],
  TREATAS({{"{{tpid}}"}}, 'Account'[TPID]),
  "ARR_MTD", [ARR (MTD)]
)
ORDER BY 'Calendar'[Fiscal Year] DESC, 'Calendar'[Fiscal Month] DESC
```

Additional revenue measures: `[ARR]` (annualized run rate), `[ARR (YTD)]` (year-to-date), `[Workload ARR]` (per-workload).

### NPS Scores (28-day)

The model has NPS in two tables — `Survey` (general) and `Fabric Survey` (Fabric-specific):

```dax
EVALUATE
SUMMARIZECOLUMNS(
  TREATAS({{"{{tpid}}"}}, 'Account'[TPID]),
  "NPS", [NPS (28d)],
  "Fabric_NPS", [Net Promoter Score (28d)]
)
```

Note: `[NPS (28d)]` comes from the `Survey` table. `[Net Promoter Score (28d)]` comes from the `Fabric Survey` table. There is also `[Feedback NPS (28d)]` in the `Feedback` table.

### Support Cases

The model has two support tables — `Fabric Support` and `Support`:

```dax
EVALUATE
SUMMARIZECOLUMNS(
  TREATAS({{"{{tpid}}"}}, 'Account'[TPID]),
  "Fabric_SR_Count", [Fabric Support Service Request Count],
  "Active_SRs", [Active Service Requests],
  "Created_CM", [Created Cases (CM)],
  "Closed_CM", [Closed Cases (CM)]
)
```

Note: `[Fabric Support Service Request Count]`, `[Created Cases (CM)]`, `[Closed Cases (CM)]` are from `Fabric Support`. `[Active Service Requests]` and `[Service Request Count]` are from `Support`.

### Workload-Level Breakdown (for EBC depth)

Per-workload breakdown of CU hours. Uses the `Fabric Capacity Units` fact table:

```dax
EVALUATE
SUMMARIZECOLUMNS(
  'Fabric Capacity Units'[Workload Type],
  TREATAS({{"{{tpid}}"}}, 'Account'[TPID]),
  "CU_Hours", [CU Hours (28d)]
)
ORDER BY [CU Hours (28d)] DESC
```

For product-level grouping, use `Usage Fabric Product` dimension:

```dax
EVALUATE
SUMMARIZECOLUMNS(
  'Usage Fabric Product'[Fabric Product],
  TREATAS({{"{{tpid}}"}}, 'Account'[TPID]),
  "MAU", [Fabric MAU (28d)],
  "CU_Hours", [CU Hours (28d)]
)
ORDER BY [CU Hours (28d)] DESC
```

Note: `Workload Type` values include "OneLake", "Data Integration", "Power BI", "Real Time Intelligence", "Data Warehousing Core", etc. `Fabric Product` values include "Data Engineering", "Data Warehousing Core", etc. For component-level grouping (e.g., "Analytics", "Data Factory"), use `'Fabric Customer Count'[Component]`.

## Growth Calculations (MoM%, YoY%)

When you retrieve monthly data, calculate growth context:

### Month-over-Month (MoM%)

```
MoM% = ((Current Month Value - Prior Month Value) / Prior Month Value) × 100
```

Pull the last 2 months of data from the query results. If the prior month value is 0 or null, report "N/A" instead of dividing by zero.

### Year-over-Year (YoY%)

```
YoY% = ((Current Month Value - Same Month Last Year Value) / Same Month Last Year Value) × 100
```

Pull at least 13 months of data to have the same month from last year. If the prior year value is 0 or null, report "N/A".

### Trend Indicator

Based on MoM%:
- `↑` — MoM% > +1%
- `↓` — MoM% < -1%
- `→` — MoM% between -1% and +1%

## Known Account Mappings

Some customers have legal names that differ from how PMs refer to them:

| Common Name | Account Name (in model) | TPID |
|-------------|------------------------|------|
| KPN | Koninklijke Kpn N.V. | 1877635 |

This table grows as new mappings are discovered. Always check `customer-engagement/customers.yaml` for the authoritative mapping — the `account` field contains the model name, the `name` field is the PM-friendly name.

## Common Failure Modes

| Problem | Cause | Fix |
|---------|-------|-----|
| Empty result set | TPID not found in model | Verify TPID in `customer-engagement/customers.yaml`, try account name search |
| `TREATAS` returns nothing | Using with calculated column instead of measure | Ensure a measure is included in `SUMMARIZECOLUMNS` |
| Column not found | Schema change in model | Run `GetSemanticModelSchema` to discover current names |
| Partial data (some months missing) | Account joined recently | Report available data, note coverage gap |
| Wrong account matched | Legal name ambiguity | Use TPID filter instead of name search |

## Output Formatting

Present results in the standard metrics table format:

```markdown
| Metric | Current | MoM% | YoY% | Trend |
|--------|---------|------|------|-------|
| Fabric MAU | 12,450 | +3.2% | +18.7% | ↑ |
```

- Format large numbers with commas (e.g., 12,450)
- Format currency with $ and commas (e.g., $1,234,567)
- Format percentages to one decimal (e.g., +3.2%)
- Include sign for all percentages (+ or -)
- Use trend indicators (↑/↓/→)
