# Databases Strategy Metrics — Project History

> This is the running log of actions, decisions, and status changes. When asked for a summary, reference the most recent entry.

---

## May 7, 2026 — ADO Review: State Corrections + Outstanding Actions

### Email Findings (May 5-7)
1. **"Re: Review the latest on Data Dashboards"** (May 5) — Miguel sent a critical alignment email to Nate, Shireesh, Joe, Danyal, Kalpana, Dhirendra, Krishna, Sonal, Arza Maimon, and others. Confirms Shireesh has early access. Flags missing parquets, definitions, and data discrepancies. Assigns ownership by pillar.
2. **"Re: Miguel:Nate 1-1s"** (May 6) — Comprehensive status update to Nate covering Databases Strategy (at risk: SQL parquet + Cosmos dependencies), LT Reliability (shifted to mid-May), and PLG (not started). Includes action table with owners.

### Teams Findings (May 6-7)
- **May 6 — Helix Data Triage chat:** Memory allocation error hit ("maximum allowable memory allocation for your tier"). Justin Martin acknowledged team-caused. Nate and Sonal both present in thread.
- **May 7 — Helix Data Semantic Model Alerts:** Major performance degradation — P90 latencies 8-65x slower than normal. Joe Muziki reported PBI Desktop stuck idling. Chris Hamill confirmed recovery. **Justin escalating to Arun & Nico** (demo was impacted). Jacob Knightley, Nate, Sonal all present.
- Impact: These incidents directly affect the Databases Strategy dashboard reliability and exec-facing demos.

### Teams: Active Customers Discrepancy Deep-Dive (May 6-7) — KEY
**"Cosmos, data model" group chat** (May 6):
- **Kalpana**: Backfill complete, parquet files look clean (~60K avg). But report shows ~80K at spike, ~72K non-spike. IcM open with Helix. Dev (Mohammad Al Aqrabawi) awaiting PBI report access.
- **Miguel** asked who needs access → Kalpana confirmed `malaqrabawi@microsoft.com`

**1:1 with Mohammad Al Aqrabawi** (May 7):
- Mohammad asked if Miguel owns the report — someone asking about the numbers
- Kalpana's query returned 70K but report shows ~81K
- Miguel explained the parquet → consolidated table pipeline
- **Mohammad's hypothesis: possible duplicates in the model**
- Mohammad committed to investigating

**3-way chat: Miguel + Mohammad + Kalpana** (May 7):
- Mohammad asked Miguel to check report filters (apply `MetricName = 'Active Customers'`)
- Miguel confirmed he can see where the problem is — **needs special filters to match their numbers**
- Miguel asked Kalpana for a quick call to figure out what filters to apply
- **Kalpana agreed** — call likely happened

**Root cause direction:** Likely duplicate rows in the consolidated model or missing filter conditions. Mohammad investigating on the data side; Miguel checking report filters.

### ADO Sync (Review)
- **#2079558 (Revert columns)** → **Closed** (May 5). Sanjana confirmed flat-column approach doesn't work (context-dependent MetricName). DAX measures are the correct path. PR #964529 abandoned. Reassigned to Sanjana Chauhan.
- **#2079498, #2079522, #2079524, #2079525** — Were stuck in "New" state in ADO while actively worked. Fixed → **Active**.
- **Feature #2079452** — ADO shows "New" (not "Active" as tracker had). Left as-is since children are Active.

### Outstanding Blockers & Actions

| # | Action | Owner | Deadline | Priority |
|---|--------|-------|----------|----------|
| 1 | Follow up with Joe/Dhirendra on parquet delivery path — confirm Option 3 (Dhirendra creates files) | Miguel → Joe/Dhirendra | This week | HIGH |
| 2 | Grant PBI report access to Cosmos dev (for Active Customers discrepancy investigation) | Miguel | ASAP | HIGH |
| 3 | Check if Krishna completed PB conversion (pipeline fix first, then Decimal type change) | Miguel → Krishna | Check May 8 | MEDIUM |
| 4 | Confirm Danyal sent Postgres definitions — if not, follow up | Miguel → Danyal | Overdue (was May 5) | HIGH |
| 5 | Coordinate May 14 formal review with Arza Maimon | Miguel → Arza | Before May 12 | MEDIUM |
| 6 | Track IcM with Helix team on Active Customers discrepancy (60K parquet vs 80K report) | Miguel | Mid-May | MEDIUM |

### Email/Teams Status
- WorkIQ authentication broken — could not pull emails or Teams chats. Need to re-authenticate interactively (`npx -y @microsoft/workiq ask` in terminal, complete browser login).

---

## May 6, 2026 — Postgres Definitions In Progress + DUM Unit Conversion to PB

### Danyal & Krishna Update (May 6)
- **Danyal** is actively writing Postgres metric definitions
- **DUM unit data flow clarified by Krishna:**
  - Bytes in Kusto → GB in Fact table → TB in parquet files
  - Krishna is now **converting to PB** — requires Decimal data type change + recalculation + parquet regeneration
  - Krishna has a bigger pipeline issue for their BI right now; will complete PB conversion after
- **Danyal** will update the DUM description to reflect PB once conversion is done
- **Danyal** asked where to write descriptions — Miguel directed him to the table and asked to match format of other pillars for consistency

---

## May 5, 2026 — Cosmos Backfill Complete + Active Customers Discrepancy

### Kalpana's Update (May 5, 3:33 PM)
- **Backfill complete** — all parquet files checked on their end, no drop or spike in the data
- **Active Instances, MongoDB Vcore** — rename now displaying correctly in the report ✅
- **All other Cosmos metrics** — trending properly
- **Active Customers discrepancy found:**
  - Parquet data shows ~60K average (stable, no spike/drop)
  - Report shows ~80K at the spike, ~72K at non-spike
  - This is a **report-side discrepancy**, not a parquet issue
- **IcM opened** with Helix team to investigate the discrepancy
- **Dev awaiting access** to the PBI report — Miguel needs to grant

### Status
- The Active Customer drops previously seen (Apr 28: -24.6%, Apr 30: -52.1%) were the old data before backfill. Post-backfill, parquet data is stable. The remaining issue is why the report shows higher numbers than parquet (~60K vs ~80K).

---

## May 5, 2026 — SQL Parquet Delivery Options (Dhirendra Email)

### Dhirendra's Update (Apr 24 email, reviewed May 5)
Dhirendra clarified the status of the 4 remaining SQL parquet metrics:

| # | Metric | Status | Source |
|---|--------|--------|--------|
| 1 | Arc Enabled SQL | ✅ Access provided | T&I Datalake — Joe was able to view the data |
| 2 | Fabric CU | ⚠️ Not in parquet | Available in existing HELIX model |
| 3 | Fabric NPS | ⚠️ Not in parquet | Available in existing HELIX model |
| 4 | Migrated vCores | 🔴 Deferred | Methodology not finalized — will provide in the future |

**Key insight:** Only Arc Enabled SQL has a direct data path. Fabric CU and Fabric NPS exist in the HELIX model but not as parquet files. Migrated vCores is deferred entirely.

### Three Delivery Options Under Consideration
1. **Joe pulls from our database** — We have access to these metrics; Joe converts them to parquet files to feed the database.
2. **Complex DAX measures** — Miguel integrates the values from the HELIX model using disconnected DAX measures (more brittle).
3. **Dhirendra creates the parquet files** ⭐ (Miguel's preferred) — Keep the process straightforward and consistent with the other metrics.

**Decision:** Discuss all 3 options with Joe when he returns from OOF. Preferred approach is Option 3.

---

## May 4, 2026 — Shireesh Early Access + Data Fixes

### Report Shared
- **Shared "Getting to #1: Database Strategy Metrics" report** with Shireesh via Teams
- Shireesh confirmed (Apr 14): coordinate formal review with **Arza Maimon**
- Report link sent with note about pending items (Postgres descriptions, Cosmos data corrections)
- Report last refreshed: May 4, 2026

### Completed Today
1. **NPS Response count bug fixed** — report now shows correct values (SQL: NPS = 35, NPS Responses = 101)
2. **UX fixes applied** (from Danyal's feedback) — labels, tooltips, Active Customer graph all resolved
3. **SQL metric definitions document created** (Databases Metrics Info.xlsx) — SQL definitions complete
4. **Report shared with Shireesh** for early access review

### Cosmos Data Issues (Kalpana Chat, May 4)
- **ActiveInstances_MongoDBVCore rename** confirmed done by Kalpana — renamed to "Active Instances, MongoDB Vcore" under Migrations
- **Data duplication found**: both `ActiveInstances_MongoDBCore` (5,087) and `ActiveInstances_MongoDBVCore` (12,531) appearing — old + new data coexisting. System only displays metrics matching the official name list.
- **Kalpana's fix**: Deleted all parquet files, backfilling from scratch. Data flowing in phases, complete by May 5 morning.
- **Transaction Units (59.1T) confirmed valid** — Andrew Liu confirmed each CRUD/Query = 1 transaction unit for Cosmos DB. Number is legitimate.
- **Cross-pillar TU definitions resolved**: All pillar teams provided their Transaction Unit definitions. Definitions now displayed in the dashboard.
- **Active Customers drop** (Apr 28: -19,594 / -24.6%; Apr 30: -37,655 / -52.1%) — needs investigation once backfill completes.
- **Joe Muziki is OOF** — SQL parquet delivery (Migrations, Arc, Fabric CU, NPS) still blocked.
- **Data changes take ~24hrs** to become visible in Miguel's report after Kalpana's refresh.

### DUM Unit Consistency (New Ask)
- **Issue**: PGSQL uses **GB** for DUM; SQL and Cosmos use **PB**. Need consistency.
- **Plan 1 (preferred)**: Ask PGSQL team to change parquet output to PB units.
- **Plan 2 (fallback)**: DAX measures to convert GB → PB in the report.
- **Enhancement needed**: Once units are consistent, update page views to display unit clearly.

### Postgres Update
- Danyal will send metric definitions/descriptions tomorrow (May 5)
- Once received, Miguel will update the report so Shireesh sees complete info across all pillars

### Dashboard Snapshot (May 4, 28d MoM)

**Strategic Outcomes:**
| Pillar | Active Instances | Active Customers | DUM | Transaction Units |
|--------|-----------------|------------------|-----|-------------------|
| SQL | — | 238.8K (+1.8%) | 140.2bn (-1.1%) | 759.2M (+4.0%) |
| PGSQL | 285.5K (+7.7%) | 55.3K (+6.7%) | 11.7K (+53.4%) | 1.2M (+3.5%) |
| Cosmos | 289.8K (+1.7%) | 81.1K (+12.2%) | 76.1M (+10.4%) | 59.1T (+1.7%) ⚠️ |

**SQL additional:** Active Databases 9.2M (+1.2%), NPS 35 (+16.7%), NPS Responses 101 (-85.8%)
**PGSQL additional:** AI Enabled Servers 16.9K (+14.3%)
**Cosmos additional:** Active Apps OAI+CDB 61.5K (+1.9%), Whale >$100K ARR 374 (+1977%⚠️)

### Pillar Status (as of May 4)

**SQL — Partially Blocked**
- Definitions complete. NPS fixed. UX done.
- 4 parquet metrics still undelivered (Migrations, Arc, Fabric CU, Fabric NPS). Joe OOF.

**Postgres — Converging**
- UX fixes done. Definitions incoming tomorrow (Danyal).
- DUM unit (GB) needs conversion to PB.

**Cosmos — In Progress / Data Fix**
- Kalpana deleted old parquets, backfilling. Transaction Units needs investigation.
- Rename done. Data duplication resolved via full backfill.

### Key People Updates
- **Arza Maimon** — Shireesh's point person for coordinating the formal review meeting

---

## April 22, 2026 — Project Kickoff & Follow-Up Email

### Actions Taken
1. **Created Feature #2079452** — "Databases Strategy Metrics" in ADO (IP Analytics), Priority 0, assigned to Miguel Myers.
2. **Created 7 child Tasks** under the Feature aligned to the standard delivery flow:
   - #2079495 — Requirements & Alignment
   - #2079496 — Data Modeling & Engineering Alignment
   - #2079497 — Report Development (Power BI)
   - #2079498 — Data Validation & QA
   - #2079499 — Monitoring & Reliability Setup
   - #2079500 — Documentation
   - #2079501 — Stakeholder Review & Publish
3. **Sent follow-up email** (RE: Review the latest on Data Dashboards) to all pillar teams with status updates from Teams chats and firm deadlines.

### Key Dates Communicated
| Date | Milestone |
|------|-----------|
| Before May 1 | All teams: final data delivery and validation complete |
| May 4 | Early access to report shared with Shireesh |
| May 14 | Shireesh's final approval review (20 min) before engaging Arun |

### Pillar Status (as of Apr 22)

**SQL — Converging**
- Pipeline issue (stalled since Apr 5) fixed; next refresh will catch up.
- NPS Response count bug — PR submitted.
- Metric definitions spreadsheet shared; finalizing next week.
- **Blockers:** Migrations, Arc Enabled SQL, Fabric CU, Fabric NPS parquet metrics not started.
- **Owners:** Priya Sathy, Dhirendra Bhupati

**Postgres — Converging**
- Metric calculation logic finalized (Primary, AsyncReplica, GeoAsyncReplica only).
- Data delivery via parquet confirmed; aligning to schema.
- Dashboard UX feedback from Danyal being addressed.
- **Blockers:** Metric documentation (definitions, calculations, strategic relevance) in progress.
- **Owners:** Charles Feddersen, Danyal Bukhari, Krishna Alaparthi

**Cosmos DB — In Progress**
- Decision: Fabric metrics split into native Fabric vs. mirroring (separate files).
- Meredith + Jai identifying data sources; follow-up with Kalpana pending.
- ActiveInstancesMongoDBVCore → rename to "Active Instances, MongoDB vCore" under Migrations.
- Fabric Active Instances delivery still pending.
- Cosmos100 TPID alignment complete (Kalpana updated); backfill in progress.
- **Owners:** Kirill Gavrylyuk, Andrew Liu

### Accountability (from email)
| Team | Ask | Deadline | Owner |
|------|-----|----------|-------|
| SQL | Finalize metric definitions; deliver remaining parquet metrics (Migrations, Arc, Fabric CU/NPS) | Before May 1 | Priya, Dhirendra |
| Postgres | Complete metric documentation; validate final dashboard data | Before May 1 | Charles, Danyal, Krishna |
| Cosmos | Deliver split Fabric metric files; deliver Fabric Active Instances; finalize metric renames | Before May 1 | Kirill, Andrew |

### Email Recipients
**To:** Nate Findley, Priya Sathy, Kirill Gavrylyuk, Charles Feddersen, Chris Hamill, Dhirendra Bhupati, Joe Muziki, Andrew Liu, Meredith Moore, Kalpana Gudimetla, Danyal Bukhari, Krishna Alaparthi

### Decisions Made
- Extra month buffer for parquet refinement is final — end-of-April deadline is firm.
- Shireesh gets early access May 4 to pre-review before the 20-min formal session on May 14.
- All teams must validate data before May; no margin for post-deadline changes.

---

## April 22, 2026 — User Story: FabricDatabases Schema Enhancement

### Actions Taken
1. **Created User Story #2079558** — "Add Display Metric Name, Description, and Importance Columns to FabricDatabases Table" as child of Feature #2079452.
2. **Assigned to Jacob Knightley** — per conversation, one of his engineers will pick up implementation.

### Details
- Three new **Text** columns: `Display metric name`, `Description`, `Importance`
- Purpose: Add human-readable context to each metric — what it is, how it's calculated, and why it matters strategically
- Enables downstream analysis tying raw metric values to strategic rationale
- Priority: 2 (High) | Tags: Databases-Strategy

### Acceptance Criteria
- Three columns added to FabricDatabases as Text type
- Existing rows unaffected (columns nullable)
- Column names match spec exactly
- Schema change deployed and validated

---
