# Action Items

<sub>Last updated: May 7, 2026</sub>

&nbsp;

---

### Status at a Glance
| Project | Health | Next Critical Date | Headline |
|---------|--------|-------------------|----------|
| Databases Strategy | 🟡 At Risk | May 14 (Shireesh review) | SQL parquet path pending Joe's return; Postgres defs overdue; Cosmos IcM open |
| LT Reliability | 🟡 Shifted | Mid-May | Meeting deferred; Helix incidents May 6-7 reinforce reliability narrative |
| PLG Key Metrics | ⚪ Not Started | TBD | Feature assigned; need to break down tasks and clarify scope with Nate |

&nbsp;

---

## This Week (May 5–9)
| Due | Owner | Action | Project |
|-----|-------|--------|---------|
| ⚠️ Overdue | Danyal | Send Postgres metric definitions (was May 5-6) | DB Strategy |
| ASAP | Miguel | Follow up with Danyal on definitions | DB Strategy |
| TBD | Krishna | Convert DUM parquet to PB | DB Strategy |
| After Danyal | Miguel | Update report with Postgres descriptions | DB Strategy |
| This week | Miguel | Discuss parquet delivery options with Joe (if back) | DB Strategy |
| Before May 12 | Miguel | Coordinate Shireesh review with Arza Maimon | DB Strategy |
| May 28, 12 PM | Miguel | 1:1 with Miso Cilimidžić (build trust, share DB Strategy case study) | LT Reliability |
| May 28, 10 AM | Miguel | Intro 1:1 with Shemesh Hamaoui (get to know each other, show how we work) | LT Reliability |
| This week | Miguel | Clarify PLG scope with Nate — new build vs integration? | PLG Metrics |
| This week | Miguel | Create child tasks under #2069070 | PLG Metrics |

&nbsp;

---

## Databases Strategy Metrics

🟡 **At Risk** — SQL parquet delivery path clarified (3 options pending Joe's return); Cosmos backfilling

**SQL Parquet Delivery Options** (discuss with Joe when back):
1. Joe pulls from our DB → converts to parquet
2. Complex DAX measures from HELIX model (disconnected)
3. ⭐ Dhirendra creates parquet files (Miguel's preferred — keeps process straightforward)

**Remaining SQL Parquet Status:**
| Metric | Data Source | Status |
|--------|------------|--------|
| Arc Enabled SQL | T&I Datalake (access provided) | ✅ Data accessible |
| Fabric CU | HELIX model | ⚠️ Needs parquet conversion |
| Fabric NPS | HELIX model | ⚠️ Needs parquet conversion |
| Migrated vCores | TBD | 🔴 Deferred — methodology not finalized |

| Owner | Action | Due | Status |
|-------|--------|-----|--------|
| Joe Muziki | Deliver remaining SQL parquets — see delivery options below | When back | 🔄 In progress |
| Miguel | Discuss 3 parquet delivery options with Joe (prefer Option 3: Dhirendra creates) | When Joe returns | 📋 Planned |
| Danyal | Send Postgres metric definitions + descriptions | May 6 | 🔄 In progress |
| Miguel | Update report with Postgres descriptions | After Danyal delivers | ⏳ Waiting |
| Krishna | Convert DUM parquet from TB → PB (Decimal type + recalculation + regeneration) | TBD (pipeline issue first) | 🔄 In progress |
| Kalpana | ~~Cosmos backfill~~ — Complete, parquet data stable (~60K Active Customers) | May 5 | ✅ Done |
| Kalpana | Investigate Active Customers report discrepancy (parquet ~60K vs report ~80K) — IcM opened with Helix | TBD | 🔄 In progress |
| Miguel | ~~Grant dev access to PBI report (Kalpana's team)~~ | May 5 | ✅ Done |
| Kalpana | ~~Investigate Transaction Units 59.1T~~ — Confirmed valid (1 CRUD/Query = 1 TU) | May 5 | ✅ Done |
| Miguel | ~~Align cross-pillar Transaction Unit definitions (SQL/Postgres/Cosmos)~~ — Definitions received and displayed in dashboard | May 9 | ✅ Done |
| Jacob Knightley | ~~Revert schema columns (Display Name, Desc, Importance)~~ — Closed. Sanjana confirmed flat-column approach doesn't work (context-dependent). DAX measures correct. PR #964529 abandoned. | May 5 | ✅ Done |
| Miguel | Coordinate Shireesh formal review with Arza Maimon | Before May 12 | 📝 Planned |

&nbsp;

---

## LT Reliability Metrics

� **Shifted** — Meeting moved to mid-May; team needs more time

| Owner | Action | Due | Status |
|-------|--------|-----|--------|
| Miguel | Follow up with DW team on MAU drop | Mid-May | 📅 Deferred |
| Miguel | Verify access to 6 reliability tables | Mid-May | 📅 Deferred |
| Miguel | 1:1 with Miso Cilimidžić — build trust, share DB Strategy as case study | May 28, 12 PM | ✅ Scheduled |
| Miguel | Intro 1:1 with Shemesh Hamaoui — get to know each other, show how we work | May 28, 10 AM | ✅ Scheduled |
| Miguel | Ask connector/DI team about coverage gaps | Mid-May | 📅 Deferred |
| Miguel | Document connector metric definitions | TBD | 📋 Planned |

&nbsp;

---

## PLG Key Metrics Dashboard

⚪ **Not Started** — Received May 5, awaiting details

| Owner | Action | Due | Status |
|-------|--------|-----|--------|
| Miguel | Clarify scope with Nate — new build or integrating existing reports? | This week | 📋 Planned |
| Miguel | Create child tasks under #2069070 (data inventory, stakeholders, sprint plan) | This week | 📋 Planned |
| Miguel | Verify which related feature IDs are still valid (some repurposed in ADO) | This week | 📋 Planned |

&nbsp;

---

### Recently Completed (last 7 days)
| Date | Owner | Action | Project |
|------|-------|--------|---------|| May 7 | Miguel | ADO state fix: 4 items corrected New→Active (#2079498, #2079522, #2079524, #2079525) | DB Strategy |
| May 5 | Sanjana | Closed #2079558 — flat-column approach abandoned, DAX measures correct | DB Strategy |
| May 5 | Kalpana | Cosmos backfill complete, parquet stable | DB Strategy |
| May 5 | Miguel | Cross-pillar TU definitions resolved and displayed | DB Strategy || May 4 | Miguel | Shared early access report with Shireesh | DB Strategy |
| May 4 | Miguel | NPS Response count bug fixed | DB Strategy |
| May 4 | Miguel | Applied UX fixes (labels, tooltips, graphs) | DB Strategy |
| May 4 | Miguel | Created SQL definitions document | DB Strategy |
| Apr 29 | Miguel | Nate confirmed: keep connectors report | LT Reliability |
| Apr 29 | Miguel | ADO work items created (#2087007 hierarchy) | LT Reliability |

<details><summary>ADO References</summary>

- DB Strategy: Feature #2079452 | Tasks #2079495–2079501, #2079520–2079526 | Story #2079558
- LT Reliability: Feature #2087007 | Story #2087023 | Tasks #2087032–2087035
- PLG Key Metrics: Feature #2069070

</details>
