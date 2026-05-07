# Action Items

<sub>Last updated: May 5, 2026</sub>

&nbsp;

---

### Status at a Glance
| Project | Health | Next Critical Date | Headline |
|---------|--------|-------------------|----------|
| Databases Strategy | 🟡 At Risk | May 5 (Postgres defs) | Cosmos backfilling; SQL parquet path clarified |
| LT Reliability | 🟡 Shifted | Mid-May | Meeting moved; Shemesh = key partner; 1:1 with Miso planned |
| PLG Key Metrics | ⚪ Not Started | TBD | Project received May 5; awaiting context |

&nbsp;

---

## This Week (May 5–9)
| Due | Owner | Action | Project |
|-----|-------|--------|---------|
| May 6 | Danyal | Send Postgres metric definitions | DB Strategy |
| TBD | Krishna | Convert DUM parquet to PB | DB Strategy |
| After Danyal | Miguel | Update report with Postgres descriptions | DB Strategy |
| Before mid-May | Miguel | 1:1 with Miso (build trust, share DB Strategy case study) | LT Reliability |
| Mid-May | Miguel | Follow up with DW team on MAU drop | LT Reliability |
| Mid-May | Miguel | Verify access to 6 reliability tables | LT Reliability |
| Mid-May | Miguel | Ask connector/DI team about coverage gaps | LT Reliability |

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
| Jacob Knightley | Revert schema columns (Display Name, Desc, Importance) | TBD | 📋 Planned |
| Miguel | Coordinate Shireesh formal review with Arza Maimon | May 14 | 📋 Planned |

&nbsp;

---

## LT Reliability Metrics

� **Shifted** — Meeting moved to mid-May; team needs more time

| Owner | Action | Due | Status |
|-------|--------|-----|--------|
| Miguel | Follow up with DW team on MAU drop | Mid-May | 📅 Deferred |
| Miguel | Verify access to 6 reliability tables | Mid-May | 📅 Deferred |
| Miguel | 1:1 with Miso Cilimidžić — build trust, share DB Strategy as case study | Before mid-May meeting | 📋 Planned |
| Miguel | Prepare stakeholder approach for Shemesh Hamaoui (hard partner) | Before mid-May meeting | 📋 Planned |
| Miguel | Ask connector/DI team about coverage gaps | Mid-May | 📅 Deferred |
| Miguel | Document connector metric definitions | TBD | 📋 Planned |

&nbsp;

---

## PLG Key Metrics Dashboard

⚪ **Not Started** — Received May 5, awaiting details

_No action items yet._

&nbsp;

---

### Recently Completed (last 7 days)
| Date | Owner | Action | Project |
|------|-------|--------|---------|
| May 4 | Miguel | Shared early access report with Shireesh | DB Strategy |
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
