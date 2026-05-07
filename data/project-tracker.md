# Project Tracker

> Persistent view of all features and tasks across projects. Updated after each ADO action.
> Last updated: **May 4, 2026**
> Last review: **May 4, 2026** — Shireesh early access shared; NPS bug fixed; UX fixes done; Cosmos backfill in progress; DUM unit consistency issue identified

---

## Databases Strategy Metrics
**Feature #2079452** | State: **Active** | Priority: 0 | Assigned: Miguel Myers
[Open in ADO](https://dev.azure.com/powerbi/IP%20Analytics/_workitems/edit/2079452)

### Delivery Tasks (Standard Flow)

| ID | Task | State | Priority | Notes |
|----|------|-------|----------|-------|
| 2079495 | Requirements & Alignment | ✅ Closed | P0 | Metrics framework defined across 4 pillars |
| 2079496 | Data Modeling & Engineering Alignment | 🔵 Active | P0 | Parquet delivery in progress across all teams |
| 2079497 | Report Development (Power BI) | 🔵 Active | P0 | Dashboard live; shared with Shireesh May 4 |
| 2079498 | Data Validation & QA | 🔵 Active | P1 | SQL done; Postgres pending Danyal; Cosmos backfill in progress |
| 2079499 | Monitoring & Reliability Setup | ⚪ New | P1 | After validation |
| 2079500 | Documentation | 🔵 Active | P1 | SQL definitions done; Postgres incoming May 5 |
| 2079501 | Stakeholder Review & Publish | ⚪ New | P1 | May 14 — coordinate with Arza Maimon |

### Open Action Items (by Pillar)

| ID | Task | State | Owner | Deadline | Pillar |
|----|------|-------|-------|----------|--------|
| 2079520 | Deliver remaining parquet metrics (Migrations, Arc, Fabric CU/NPS) | 🔵 Active | Joe Muziki | ⚠️ Overdue (May 1) | SQL 🔷 |
| 2079521 | Finalize metric definitions & NPS bug fix | ✅ Closed | Miguel | Done May 4 | SQL 🔷 |
| 2079522 | Complete metric documentation | 🔵 Active | Danyal | May 5 | Postgres 🟩 |
| 2079523 | Validate dashboard data & resolve UX feedback | ✅ Closed | Miguel | Done May 4 | Postgres 🟩 |
| 2079524 | Deliver split Fabric metric files (native vs. mirroring) | 🔵 Active | Kalpana | Backfilling | Cosmos 🟠 |
| 2079525 | Finalize metric renames & Cosmos100 TPID backfill | 🔵 Active | Kalpana | Backfilling | Cosmos 🟠 |
| 2079526 | Prepare Shireesh early access package | ✅ Closed | Miguel | Done May 4 | All 🗖 |
| 2079558 | Revert Display Metric Name, Description & Importance columns from FabricDatabases | 🔵 Active | Jacob Knightley | TBD | All 🗖 |

### Key Milestones

| Date | Milestone | Status |
|------|-----------|--------|
| Before May 1 | All teams: final data delivery and validation | ⚠️ Partial — SQL parquet overdue (Joe OOF), Cosmos backfilling |
| May 4 | Early access to report shared with Shireesh | ✅ Done |
| May 14 | Shireesh's final approval review (20 min) | ⏳ Pending — coordinate with Arza Maimon |
| TBD | Arun engagement | ⏳ Pending (after Shireesh approval) |

### Pillar Health

| Pillar | Status | Key Risk |
|--------|--------|----------|
| SQL 🔷 | ⚠️ Blocked | 4 parquet metrics overdue; Joe Muziki OOF; NPS bug fixed; definitions done |
| Postgres 🟩 | Converging | UX fixes done; Danyal sending definitions May 5; DUM unit needs PB conversion |
| Cosmos 🟠 | In Progress | Kalpana backfilling after deleting old parquets; Transaction Units (59.1T) suspicious; IcM requested |

---

## LT Reliability Metrics
**Feature:** [#2087007](https://dev.azure.com/powerbi/IP%20Analytics/_workitems/edit/2087007) | State: **New** | Priority: 2 | Assigned: Miguel Myers
**Related:** IcM-767077695 (connectors report data quality)

### Scope
- **Phase 1 (now):** DW Reliability — build reliability view from Sonal's semantic model
- **Phase 2 (July 2026+):** Pipeline (Ajay Arora) and Spark (Lisa Liu) reliability
- **Connectors report:** **Keeping on LT Dash** — Nate confirmed Apr 29. Own the integrator role.

### Key Data Assets
| Table | Status |
|-------|--------|
| Fabric Feature Reliability | ⚪ Access TBD |
| Fabric Service Reliability | ⚪ Access TBD |
| Reliability Fabric Pipeline | ⚪ Phase 2 |
| Reliability Fabric Spark | ⚪ Phase 2 |
| Reliability And Security | ⚪ Access TBD |
| Fabric Capacity Reliability | ⚪ Access TBD |

### User Story & Tasks

**User Story [#2087023](https://dev.azure.com/powerbi/IP%20Analytics/_workitems/edit/2087023):** Investigate and resolve Fabric DW connector MAU data quality issue

| ID | Task | State | Owner | Due |
|----|------|-------|-------|-----|
| 2087032 | Resolve DW connector telemetry drop (IcM-767077695) | ⚪ New | Miguel | May 5 |
| 2087033 | Investigate service + agentic event coverage gaps | ⚪ New | Miguel | May 9 |
| 2087034 | Build DW reliability view from semantic model | ⚪ New | Miguel | ~May 8 |
| 2087035 | Document connector metric definitions | ⚪ New | Miguel | TBD |

### Open Action Items

| Action | Owner | Deadline | Status |
|--------|-------|----------|--------|
| Verify access to all 6 reliability tables | Miguel | May 5 | ⏳ Pending |
| Follow up with DW team on telemetry drop | Miguel | May 5 | ⏳ Pending |
| Schedule meeting with Miso Cilimidžić (DW Reliability) | Miguel | ~May 8 | ⏳ Pending |
| Ask connector/DI team about service + agentic coverage | Miguel | May 9 | ⏳ Pending |

### Key Milestones

| Date | Milestone | Status |
|------|-----------|--------|
| Apr 30 | Nate 1:1 — connectors report decision | ✅ Keep it |
| ~May 8 | DW Reliability team meeting (Miso Cilimidžić) | ⏳ Pending |
| July 2026+ | Pipeline & Spark reliability (Phase 2) | ⏳ Future |

### Stakeholder Health

| Area | Contact | Status |
|------|---------|--------|
| DW Reliability | Miso Cilimidžić | Meeting TBD (~May 8) |
| Central Reliability | Shemesh Hamaoui | Not yet engaged |
| Uber Stakeholder | Ravs Kaur | Requestor |
| Pipeline | Ajay Arora | Phase 2 (July+) |
| Spark | Lisa Liu | Phase 2 (July+) |
| Connectors Data | Svetlana Gershaft | IcM filed, investigating |
| Connectors Report | Andreas Weber | Current report owner |

---

## Legend
- ✅ Closed — Done
- 🔵 Active — In progress
- ⚪ New — Not started
- 🔴 Blocked — Needs attention
- ⏳ Pending — Future milestone

---

<!-- Add new projects below this line -->
