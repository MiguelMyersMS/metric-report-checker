# LT Reliability Metrics

## ADO Work Items
- **Feature:** [#2087007](https://dev.azure.com/powerbi/IP%20Analytics/_workitems/edit/2087007) — LT Reliability Metrics
- **User Story:** [#2087023](https://dev.azure.com/powerbi/IP%20Analytics/_workitems/edit/2087023) — Investigate and resolve Fabric DW connector MAU data quality issue (IcM-767077695)
- **Tasks:**
  - [#2087032](https://dev.azure.com/powerbi/IP%20Analytics/_workitems/edit/2087032) — Resolve DW connector telemetry drop (IcM-767077695)
  - [#2087033](https://dev.azure.com/powerbi/IP%20Analytics/_workitems/edit/2087033) — Investigate service-based + agentic event coverage gaps
  - [#2087034](https://dev.azure.com/powerbi/IP%20Analytics/_workitems/edit/2087034) — Build DW reliability view from semantic model
  - [#2087035](https://dev.azure.com/powerbi/IP%20Analytics/_workitems/edit/2087035) — Document connector metric definitions

## What This Is
A cross-product reliability dashboard for Arun's Leadership Team (LT), consolidating reliability and perceived reliability metrics from multiple Fabric workloads into a single view.

**Our role is integrator** — each product team owns their metrics and speaks to them. We bring them together in a central place so Arun can compare reliability across products without visiting 10 different reports.

## Scope

### Phase 1 — Data Warehouse (Now → July 2026)
Focus on **Fabric Datawarehouse** reliability metrics first:
- Total queries, success, failure (at different grains)
- **Reliability** = system errors / total
- **Perceived Reliability** = (system errors + user errors) / total

### Phase 2 — Pipeline & Spark (July 2026+)
Expand to additional workloads once DW is stable:
- Pipeline reliability
- Spark job / Notebook reliability

### Future (TBD)
- Kusto reliability
- Semantic model reliability
- SQL endpoint reliability

## Key Context

### Data Architecture
- 6 reliability tables identified in the current semantic model:
  1. `Fabric Feature Reliability`
  2. `Fabric Service Reliability`
  3. `Reliability Fabric Pipeline`
  4. `Reliability Fabric Spark`
  5. `Reliability And Security`
  6. `Fabric Capacity Reliability`
- Data comes from **different systems with different schemas** — some have error-level details, others don't
- Two reliability types tracked: system-only (reliability) vs. system + user errors (perceived reliability)
- Each product team provides data from their own DW instance

### Data Sources (from CSX working group, Sep 2025)
| Source | Description | Key Contact |
|--------|-------------|-------------|
| WSR model (DCP) | Drill-down info with correlation ID | Yoram Atir |
| Spark reliability report | Lisa Liu's report (6 capacities) | Lisa Liu |
| Pipeline Reliability - Runs | Dashboard shared by Ravs | Ajay Arora |
| PBI WSR report | Commonly used for PBI WSR; Parthiv & Joshua realigning scenarios | Christian Wade / Kay Unkroth |
| PBI semantic query execution | Needed right "feature name" for data — was outstanding as of Sep 2025 | Sonal |

### Monitoring & Alerting Architecture
- **Decision:** Use **KAS/MDM** (standardized tools), NOT Data Activator standalone alerts (Yoram Atir, Sep 2025)
- Scaling requires standardized events and thresholds
- Design for all customers, not just CSX
- Each scenario owner sets their own thresholds
- **Dor** (suggested by Yoram) should be involved for alerting scale work

### Existing Report — Connector Authoring & Downstream MAU
- **Report:** PBI Connector Authoring and Downstream MAU (on LT dashboard)
- Previously owned by Kimberlee → transferred to Andreas Weber (no context retained)
- **Data quality concern:** Svetlana Gershaft flagged incorrect data (IcM Incident-767077695)
- Fabric Datawarehouse connector shows ~93.5% YoY drop in Downstream Connector MAU and 141.1% YoY increase in Connector Authoring Occurrences

**How the metrics work:**
- **Connector Authoring MAU** (top of funnel) — counts "Get Data" clicks in Power BI Desktop per connector. Measures intent, not successful connections. Same logic across all connectors.
- **Downstream Connector MAU** (end of funnel) — counts all users who query a published model, credited to every connector source in that model.
- Built ~5 years ago for Desktop-only era. Does **not** capture service-based or agentic connections.

**Investigation status:**
1. Svetlana filed IcM → IDIA confirmed not their issue
2. Bhavesh confirmed issue in data creation data
3. Data Creation team investigating
4. Likely root cause: PG/DW team changed telemetry emission (data generation issue, not data processing)

**Decision (Apr 29):** Nate confirmed — **keep the connectors report on the LT Dash.** We own the integrator role. Next steps: investigate DW telemetry drop + service/agentic coverage gaps.

### Open Questions
- Who owns the DW connector telemetry investigation — DCP, PG team, or us?
- Does the connector system capture service-based and agentic connections? (likely no — needs modernization)
- What will reliability teams provide in the future vs. what they provide today?
- Transition plan from old telemetry system to new system

## People

### Core Team
| Person | Alias | Role |
|--------|-------|------|
| **Miguel Myers** | miguelmyers@ | Project lead (integrator) |
| **Sonal Bhargava** | sonalb@ | Previous owner, knowledge transfer partner |
| **Nate Findley** | natefin@ | Manager, oversight |
| **Arun** | | Executive stakeholder — needs single-pane reliability view |

### Reliability Stakeholders (from Sonal)
| Person | Alias | Area | Notes |
|--------|-------|------|-------|
| **Ravs Kaur** | | Uber stakeholder | Asked for all reliability views; drives working group |
| **Shemesh Hamaoui** | | Central Rel team | **Central reliability owner** — the key stakeholder to align with. Works with each product team. Sonal flagged as the "hard partner." Miso has already worked with him. |
| **Miso Cilimidžić** | | DW Reliability | PM on the product side. Responsible for answering questions about metric changes. Defined what's most important to measure for Epic/CSX. Meeting moved to mid-May. |
| **Ajay Arora** | | Pipeline | Pipeline reliability contact (Phase 2) |
| **Lisa Liu** | | Spark Job | Spark reliability contact (Phase 2); owns 6 Spark capacities |

### CSX Working Group (Sep 2025)
| Person | Alias | Role |
|--------|-------|------|
| **Christian Wade** | | PBI Engineering lead; transitioned to Kay Unkroth Sep 8 |
| **Kay Unkroth** | | Took over PBI side from Christian |
| **Yoram Atir** | | Alerting/monitoring architect; pushed for KAS/MDM standardization |
| **David Browne** | | Data/infra; provided CSX prod/QA capacity breakdown |
| **Kim Manis** | | Capacity context |
| **Dor** | | Yoram suggested adding for alerting scale work |

### LT Dashboard / Connectors Report
| Person | Alias | Role |
|--------|-------|------|
| **Svetlana Gershaft** | | Flagged data quality issue on LT dash connectors report |
| **Andreas Weber** | | Current owner of connectors report (transferred from Kimberlee) |
| **Bhavesh** | | Confirmed issue in data creation data (IDIA investigation) |
| **DI team** | | Owns all connectors — can answer connector-level questions |
| **Tamas's team** | | Potential new home for analytics/reporting coverage |

## Principles (from Sonal)
1. **We are integrators, not owners** — each team owns their metrics. We centralize them.
2. **Don't step on toes** — frame as "bringing together in one place," not replacing anyone's reporting.
3. **Accept what teams give** — schemas differ; work with what's available rather than demanding uniformity.
4. **Keep communications on** — ensure reports reflect current systems, not legacy ones.

## Documentation Protocol
As this project progresses, all new information (metric definitions, schema details, stakeholder decisions, meeting outcomes) should be captured as project documentation. Before adding any new documentation:
1. Surface the proposed content to Miguel for review
2. Show exactly what will be stored and where
3. Only commit after approval

This ensures documentation accuracy and prevents storing incorrect or sensitive information.

## Decisions Log
| Date | Decision | Context |
|------|----------|---------|
| 2025-09-04 | Start with CSX, design to scale to all customers | Ravs directed; Ajay asked scope question |
| 2025-09-04 | Use KAS/MDM for alerting, not Data Activator standalone | Yoram Atir pushed for standardized tools |
| 2025-09-08 | Christian Wade → Kay Unkroth PBI ownership transition | Outstanding: semantic query feature name, monitoring/alerting, remove Premium publish |
| 2026-04-08 | Data quality concern raised on LT dash connectors report | Svetlana flagged IcM-767077695; Nate suggested moving to Tamas's team |
| 2026-04-28 | Project created, DW first | Sonal knowledge transfer: focus DW now, Pipeline/Spark not until July |
| 2026-04-29 | Keep connectors report on LT Dash | Nate confirmed; we own integrator role |
| 2026-05-05 | LT Reliability meeting moved to mid-May | Team needs a few more weeks. Gives Miguel time for 1:1 with Miso first. |
| 2026-05-05 | Shemesh Hamaoui is the key partner to manage | Sonal clarified: Shemesh (central reliability owner) is the hard partner, not Miso. Miso is PM on product side. |
| 2026-04-29 | ADO Feature #2087007 + Story #2087023 created | 4 tasks: IcM resolution, coverage gaps, DW view, metric docs |
