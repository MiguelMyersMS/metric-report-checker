# Databases Strategy Metrics

## ADO Work Items
- **Feature:** [#2079452](https://dev.azure.com/powerbi/IP%20Analytics/_workitems/edit/2079452) — Databases Strategy Metrics
- **Tasks:**
  - [#2079495](https://dev.azure.com/powerbi/IP%20Analytics/_workitems/edit/2079495) — Requirements & Alignment
  - [#2079496](https://dev.azure.com/powerbi/IP%20Analytics/_workitems/edit/2079496) — Data Modeling & Engineering Alignment
  - [#2079497](https://dev.azure.com/powerbi/IP%20Analytics/_workitems/edit/2079497) — Report Development (Power BI)
  - [#2079498](https://dev.azure.com/powerbi/IP%20Analytics/_workitems/edit/2079498) — Data Validation & QA
  - [#2079499](https://dev.azure.com/powerbi/IP%20Analytics/_workitems/edit/2079499) — Monitoring & Reliability Setup
  - [#2079500](https://dev.azure.com/powerbi/IP%20Analytics/_workitems/edit/2079500) — Documentation
  - [#2079501](https://dev.azure.com/powerbi/IP%20Analytics/_workitems/edit/2079501) — Stakeholder Review & Publish

## Goal
Build an executive Power BI scorecard providing a unified view of Microsoft's Databases and Analytics strategy execution across four core pillars: **SQL Migrations, Postgres, NoSQL (Cosmos DB), and Fabric**.

The report serves as the **single source of truth for executive stakeholders** — enabling visibility into growth drivers, migration progress, and market share expansion. Supports Arun's strategy narrative to AmyH/SatyaN.

## Pillars & Metrics Framework

Each pillar tracks metrics across 5 standardized categories:

### 1. SQL
| Category | Metrics |
|----------|---------|
| Outcomes | Active Customers, Active Instances, DUM, Transaction Units, NPS, NPS Response Volume |
| AI / New Workloads | Azure OpenAI Attached Applications |
| Migrations | vCores Ready in Arc, vCores Migrated |
| Fabric Integration | Consumption Units (Fabric CU), Fabric NPS |

### 2. Postgres
| Category | Metrics |
|----------|---------|
| Outcomes | Active Instances, Active Customers, DUM, Transaction Units |
| Migrations | Addressable Install Base (Arc), Addressable Install Base (AzMigrate), Oracle Migration Tooling |
| AI / New Workloads | AI-Enabled Servers |
| Strategic Signals | Segment Type on Active Customers |

### 3. NoSQL (Cosmos DB)
| Category | Metrics |
|----------|---------|
| Outcomes | Active Instances, Active Customers, DUM, Transaction Units |
| AI / New Workloads | Active Applications (incl. OpenAI-integrated workloads) |
| Migrations | Active Instances (MongoDB vCore) |
| Fabric Integration | Fabric Active Instances |
| Customer / Strategic Wins | Cosmos DB Whale Customers (>$100K ARR) |

## Execution Plan

```
Phase 1 — Foundation (Week 1)     → Task 1: Requirements & Alignment
Phase 2 — Data Layer (Week 2)     → Task 2: Data Modeling & Eng Alignment
Phase 3 — Build (Weeks 3-4)       → Task 3: Report Development (Power BI)
Phase 4 — Harden (Week 5)         → Tasks 4, 5, 6 (Validation, Monitoring, Docs)
Phase 5 — Ship (Week 6)           → Task 7: Stakeholder Review & Publish
```

**Critical path:** Task 1 → 2 → 3 → 4 → 7

## Acceptance Criteria

### Data & Modeling
- All defined metrics sourced, validated, and documented
- Data model supports cross-pillar comparison and drill-down
- Metrics aligned with business definitions and approved by stakeholders

### Report Experience
- Executive summary view (top KPIs across pillars)
- Drill-down views per pillar
- Trend analysis for key metrics
- Visual design supports clear storytelling

### Data Quality & Reliability
- Data refresh validated and monitored
- Anomaly detection for key metrics
- Known limitations documented

### Documentation
- Each metric: Definition, DAX calculation logic, Data source
- Accessible and maintained

### Stakeholder Alignment
- Report reviewed and signed off by key stakeholders
- Feedback incorporated before final publish

## Strategic Context

Source: Arun's strategy excerpt to AmyH/SatyaN

**Key market signals:**
- SQL: Selling 2x more on-prem than Azure SQL — need to flip this via AI-ready DB, Arc migrations, Copilot-assisted migration, and Sybase ($3B+ TAM)
- Postgres: $701M ARR, 51% YoY growth, but only 1/8 of AWS Postgres revenue — accelerate via on-prem/AWS/Oracle migrations and Horizon DB
- NoSQL: Cosmos DB powers OpenAI + Teams + Walmart; Document DB opens Mongo migration funnel
- Fabric: 32.7K customers, $2.2B ARR, 64% YoY — drive toward 100% YoY via Power BI standardization ($4B unlock), platform consolidation ($4-5B), RTI ($1-2B), D365 attach ($1B), Foundry attach ($1-2B)

## Decisions Log
<!-- Record key decisions as they're made -->
| Date | Decision | Context |
|------|----------|---------|
| 2026-05-04 | Schema enhancement reverted — remove Display Metric Name, Description, Importance columns | Sanjana implemented, Miguel determined approach won't work. #2079558 updated to track revert. |
| 2026-05-05 | Cosmos Transaction Units (59.1T) confirmed valid | Andrew Liu confirmed: 1 CRUD/Query = 1 TU. Cross-pillar TU definition alignment needed (SQL/Postgres). |
| 2026-05-05 | SQL remaining parquets: 3 sourced, 1 deferred | Dhirendra email: Arc SQL via T&I Datalake, Fabric CU/NPS via HELIX model, Migrated vCores deferred. 3 delivery options — preferred: Dhirendra creates parquets. Discuss with Joe when back. |
| 2026-05-04 | DUM must use PB as unit across all pillars | PGSQL currently uses GB; SQL/Cosmos use PB. Plan 1: ask PGSQL team to change parquet. Plan 2: DAX conversion. |
| 2026-05-04 | Arza Maimon is Shireesh's delegate for formal review | Shireesh directed coordination through Arza for the May 14 approval session. |
| 2026-04-22 | Created Feature #2079452 with 7 child tasks | Initial project setup based on Arun's strategy email |
