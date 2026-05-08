# Follow-ups Tracker

<!-- New entries go at the top. Use the template from .github/skills/follow-up-tracker/templates/follow-up-entry.md -->
<!-- Status: Pending | Done | Overdue -->

---
### LT Reliability Metrics
---

## 2026-05-07 — Shemesh Hamaoui: Intro 1:1 scheduled
- **Topic**: Introduction — get to know each other, understand his expectations, show how we work (DB Strategy as example)
- **Context**: Sonal identified Shemesh as the central reliability owner (the "how"). This is the first meeting. Goal is relationship-building and alignment on shared reliability objectives.
- **Action needed**: Review [talking points](../drafts/shemesh-intro-1on1-2026-05-07.draft.md) before the meeting.
- **Due date**: 2026-05-28 (10 AM)
- **Status**: Scheduled
- **Related project**: brain/projects/lt-reliability-metrics/

## 2026-05-07 — Miso Cilimidžić: 1:1 scheduled
- **Topic**: Discuss DW reliability metrics, align on Phase 1 scope, build collaborative relationship
- **Context**: Miso owns the "what" for Epic/CSX reliability. Meeting prep includes May 6-7 incident data, April reliability report, and Phase 1 scope proposal.
- **Action needed**: Review [talking points](../drafts/miso-1on1-talking-points-2026-05-07.draft.md) before the meeting.
- **Due date**: 2026-05-28 (12 PM)
- **Status**: Scheduled
- **Related project**: brain/projects/lt-reliability-metrics/

## 2026-04-29 — Follow-up with Sonal Bhargava (Reliability Metrics)
- **Topic**: Meeting threads and recordings from previous reliability discussions
- **Context**: Sonal shared all available materials: knowledge transfer call, CSX Teams chat history, reliability stakeholder doc, Connector Report Sync recording. Miguel will now record all future conversations about this project for ongoing documentation.
- **Status**: Done
- **Resolution**: All materials received. CSX chat extracted. Future context will come from Miguel's own meeting recordings.
- **Related project**: brain/projects/lt-reliability-metrics/

## 2026-04-29 — Follow up with DW team on connector telemetry drop
- **Topic**: Why did Fabric Datawarehouse downstream MAU drop?
- **Context**: Apr 24 sync confirmed: counting is uniform across connectors. DW team likely changed telemetry emission. Investigation: IDIA → Bhavesh → Data Creation team → suspected PG issue.
- **Action needed**: Contact DW team directly — ask what changed. Reference IcM-767077695.
- **Due date**: Mid-May (meeting moved from May 5)
- **Status**: Pending — deferred, team needs more time
- **ADO**: Task #2087032
- **Related project**: brain/projects/lt-reliability-metrics/

## 2026-04-29 — Ask connector/DI team about service + agentic event coverage
- **Topic**: Does the connector MAU system capture service-based and agentic connections?
- **Context**: System built ~5 years ago for Desktop-only. Need to verify service authoring and agentic flows emit events.
- **Action needed**: Reach out to DI team (owns all connectors).
- **Due date**: 2026-05-09
- **Status**: Pending
- **ADO**: Task #2087033
- **Related project**: brain/projects/lt-reliability-metrics/

---
### Databases Strategy Metrics
---

## 2026-05-07 — Mohammad Al Aqrabawi: Active Customers discrepancy investigation
- **Topic**: Report shows ~81K Active Customers but Kalpana's parquet/query returns ~60-70K
- **Context**: Mohammad identified possible **duplicates in the consolidated model**. Miguel confirmed report filters need adjustment (`MetricName = 'Active Customers'`). Quick call with Kalpana likely happened May 7. Mohammad committed to investigating on the data side. IcM still open with Helix team.
- **Action needed**: Follow up with Mohammad on findings. Apply correct filters to report. Close the gap before May 14 Shireesh review.
- **Due date**: Before May 14
- **Status**: In Progress — Mohammad investigating, Miguel checking filters
- **ADO**: #2079524
- **Related project**: brain/projects/databases-strategy/

## 2026-05-04 — Danyal Bukhari: Postgres metric definitions
- **Topic**: Send Postgres metric definitions, descriptions, and strategic relevance
- **Context**: Danyal reached out and will send the info tomorrow (May 5). Once received, Miguel will update the report so Shireesh sees complete descriptions across all pillars.
- **Action needed**: Receive from Danyal, update report, verify descriptions display correctly.
- **Due date**: 2026-05-05
- **Status**: Pending
- **ADO**: #2079522
- **Related project**: brain/projects/databases-strategy/

## 2026-05-04 — DUM unit consistency (PB vs GB)
- **Topic**: PGSQL DUM uses GB while SQL and Cosmos use PB — need all pillars consistent
- **Context**: Data flow: Bytes (Kusto) → GB (Fact table) → TB (parquet). Krishna Alaparthi is now converting to PB — requires Decimal data type + recalculation + parquet regeneration. Krishna has a pipeline issue to resolve first, then will complete. Danyal will update DUM description to reflect PB. Plan 1 (PGSQL team changes parquet) is underway.
- **Action needed**: Wait for Krishna to complete PB conversion and regenerate parquets. Danyal to update description.
- **Due date**: TBD (Krishna working pipeline issue first)
- **Status**: In Progress — Plan 1 confirmed, conversion underway
- **Related project**: brain/projects/databases-strategy/

## 2026-05-04 — Kalpana Gudimetla: Cosmos data fix in progress
- **Topic**: Cosmos parquet data issues — rename, backfill, and data discrepancies
- **Context**: Backfill **complete** (May 5). Kalpana checked parquet files — no drop/spike, Active Customers averages ~60K. However, report shows ~80K at spike and ~72K non-spike — discrepancy is report-side, not parquet. MongoDB Vcore rename now displays correctly. All other metrics trending properly. Active IcM opened with Helix team to investigate. Dev awaiting access to PBI report.
- **Action needed**: Monitor IcM progress on Active Customers discrepancy. Dev access granted.
- **Due date**: TBD (IcM in progress)
- **Status**: In Progress — backfill done, dev has access, report discrepancy under investigation
- **ADO**: #2079524, #2079525
- **Related project**: brain/projects/databases-strategy/

## 2026-05-05 — Cross-pillar Transaction Unit definition alignment
- **Topic**: Confirm each pillar defines "Transaction Unit" the same way for comparability
- **Context**: Andrew Liu confirmed Cosmos TU = 1 CRUD/Query (59.1T is valid). All pillar teams have since provided their TU definitions, and they are now displayed in the dashboard.
- **Status**: Done
- **Resolution**: Definitions received from all teams and integrated into the report.
- **Related project**: brain/projects/databases-strategy/

## 2026-04-22 — Follow-up with Priya Sathy & Dhirendra Bhupati (SQL)
- **Topic**: Deliver remaining parquet metrics + finalize metric definitions
- **Context**: SQL definitions document created (May 4). NPS bug fixed (May 4). Joe Muziki (who took over delivery) is OOF as of May 4. Dhirendra clarified (Apr 24 email): Arc Enabled SQL has access via T&I Datalake; Fabric CU and Fabric NPS exist in HELIX model (not parquet); Migrated vCores deferred (methodology not finalized). Three delivery options: (1) Joe pulls from our DB and converts to parquet, (2) complex DAX from HELIX model, (3) Dhirendra creates parquet files (Miguel's preferred). Will discuss with Joe when he returns.
- **Action needed**: Discuss 3 delivery options with Joe when back. Preferred: Option 3 (Dhirendra creates parquets).
- **Due date**: When Joe returns from OOF
- **Status**: In Progress — data sources identified, delivery approach pending
- **ADO**: #2079520, #2079521
- **Related project**: brain/projects/databases-strategy/

## 2026-04-22 — Follow-up with Charles Feddersen, Danyal Bukhari & Krishna Alaparthi (Postgres)
- **Topic**: Complete metric documentation + validate dashboard data + resolve UX feedback
- **Context**: UX fixes applied (May 4). Danyal will send metric definitions May 5. Dashboard data validation pending once descriptions are in.
- **Action needed**: Receive Danyal's definitions, update report, validate.
- **Due date**: 2026-05-05
- **Status**: In Progress — UX done, definitions incoming
- **ADO**: #2079522, #2079523
- **Related project**: brain/projects/databases-strategy/

---
### Completed
---

## 2026-04-29 — Nate 1:1: LT Dash Connectors Report Decision
- **Topic**: Keep or remove PBI Connector Authoring report from LT dashboard
- **Resolution**: Nate confirmed — **keep it.** We own the integrator role.
- **Status**: Done
