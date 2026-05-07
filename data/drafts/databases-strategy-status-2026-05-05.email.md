# Databases Strategy Metrics — Status Update & Urgent Data Validation

**Subject:** ACTION REQUIRED: Databases Strategy Metrics — Shireesh Has Access, Final Review Approaching

**To:** Nate Findley, Priya Sathy, Kirill Gavrylyuk, Charles Feddersen, Chris Hamill, Dhirendra Bhupati, Joe Muziki, Andrew Liu, Meredith Moore, Kalpana Gudimetla, Danyal Bukhari, Krishna Alaparthi

---

Hi team,

Quick update on the **"Getting to #1: Database Strategy Metrics"** report — and a few urgent asks before we reach the finish line.

## Shireesh Now Has Access

As of May 4, Shireesh has early access to the report and can see the data across all pillars. He is coordinating the formal review meeting with **Arza Maimon**. This means **any data inaccuracies or gaps are now visible to leadership** — please treat data validation as your top priority this week.

## Current Pillar Status & Open Items

### SQL — Partially Blocked
- Definitions complete. NPS and UX fixes shipped.
- **Remaining 4 parquet metrics status (per Dhirendra's Apr 24 email):**
  - **Arc Enabled SQL** — Access to T&I Datalake provided; Joe was able to view the data.
  - **Fabric CU** — Data exists in the HELIX model but not yet in parquet format.
  - **Fabric NPS** — Data exists in the HELIX model but not yet in parquet format.
  - **Migrated vCores** — Deferred; methodology to determine accurate metric not finalized yet.
- Delivery approach for Fabric CU/NPS parquets to be finalized when Joe returns from OOF.
- **Owners:** Priya, Dhirendra — please confirm timeline for Arc Enabled SQL parquet delivery and Fabric CU/NPS path forward.

### Postgres — Converging
- UX fixes applied.
- **DUM unit conversion in progress:** Krishna confirmed the data flow (Bytes → GB → TB → PB) and is converting parquet output to PB for consistency with SQL/Cosmos. Requires Decimal data type change + parquet regeneration.
- **Metric definitions:** Danyal is actively writing them and will update the DUM description to reflect PB.
- **Owners:** Charles, Danyal, Krishna — please notify Miguel when definitions and PB conversion are complete.

### Cosmos DB — Converging
- MongoDB vCore rename now displaying correctly. ✅
- Backfill complete — Kalpana confirmed parquet files checked, no drop/spike in the data. All metrics trending properly.
- Transaction Units (59.1T) confirmed valid — each CRUD/Query = 1 transaction unit.
- **Remaining issue:** Active Customers shows a discrepancy between parquet data (~60K) and what the report displays (~80K at spike, ~72K non-spike). Kalpana has opened an **active IcM with the Helix team** to investigate.
- **Owners:** Kirill, Andrew, Kalpana — IcM in progress; dev needs PBI report access.

## Cross-Pillar: Transaction Unit Definitions

Each pillar has confirmed their Transaction Unit definition, and these are now displayed in the dashboard. Cosmos defines a TU as 1 CRUD/Query (59.1T confirmed valid). All teams — please verify your TU definitions display correctly in the report.

## What I Need From Each Team — This Week

| Team | Action | Owner(s) |
|------|--------|----------|
| **SQL** | Confirm Arc Enabled SQL parquet delivery; clarify Fabric CU/NPS path (HELIX → parquet) | Priya, Dhirendra |
| **Postgres** | Send metric definitions today; confirm DUM unit fix plan | Danyal, Charles, Krishna |
| **Cosmos** | Validate backfilled data; investigate Active Customer drops | Kirill, Andrew, Kalpana |
| **All Teams** | Review your pillar's data in the report and flag any issues immediately | Everyone |

## Why This Is Urgent

The **final review meeting with Shireesh** is coming up very soon. After that session, this report goes to **Arun for the AmyH/SatyaN narrative**. There is no buffer left for post-deadline fixes — what Shireesh sees is what leadership sees. Please prioritize your open items accordingly.

If you have any blockers, reach out to me directly so we can resolve them before the review.

Thanks,
Miguel
