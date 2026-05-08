# LT Reliability Metrics — Project History

> Running log of actions, decisions, and status changes. When asked for a summary, reference the most recent entry.

---

## May 7, 2026 — ADO Review: Timeline Shifted to Mid-May

### Email Findings (May 5-7)
1. **"Helix Platform Reliability Update - April 2026"** (May 6) — Kiefer Sheldon sent monthly update: 11 product IcMs in April (+38% MoM), all resolved. Orchestration success rate 96.61% across ~6k jobs. **Semantic model performance regressed** (P90 latency +30.3% MoM). Forward risk: capacity pressure as LLM/agent usage scales.
2. **"Re: Miguel:Nate 1-1s"** (May 6) — Status to Nate: LT Reliability shifted to mid-May, all DW follow-ups deferred. Plan: use Databases Strategy as case study for Miso 1:1.

### Teams Findings (May 6-7) — **Live reliability incidents**
- **May 6 — Helix Data Triage:** Memory allocation limit hit. Justin Martin acknowledged team-caused. Sonal engaged despite OOF.
- **May 7 — Helix Data Semantic Model Alerts:** **Severe** — query response times 8-65x slower, P90 latencies >100s. Joe Muziki hit it (PBI Desktop stuck). Justin escalating to Arun & Nico (hit during a demo). Eventually stabilized.
- **Relevance to LT Reliability project:** These incidents are live examples of the reliability gaps this project aims to address. Use as talking points in Miso 1:1.

### ADO Comment Review (from May 5-6 updates)
- **LT Reliability meeting moved** from May 5 to **mid-May** — Sonal's team needs a few more weeks
- **Stakeholder clarification from Sonal:**
  - **Shemesh Hamaoui** = hard partner (central reliability owner, works with each product team)
  - **Miso Cilimidžić** = PM on product side (responsible for metric changes, defines what's most important for Epic/CSX)
- **Strategy:** Use Databases Strategy project as a case study to build trust with Miso before the rescheduled meeting
- **All DW follow-ups deferred to mid-May:** MAU drop (#2087032), table access, connector gaps

### Outstanding Actions

| # | Action | Owner | Deadline | Priority |
|---|--------|-------|----------|----------|
| 1 | ~~Schedule meeting with Miso Cilimidžić~~ — **Scheduled May 28, 12 PM** | Miguel | May 28 | ✅ Done |
| 2 | Verify access to 6 reliability tables (deferred) | Miguel | Mid-May | MEDIUM |
| 3 | Follow up on DW connector telemetry drop (IcM-767077695) after Miso 1:1 | Miguel | Mid-May | MEDIUM |
| 4 | Investigate service + agentic event coverage gaps (#2087033) | Miguel | After Miso meeting | LOW (deferred) |
| 5 | Build DW reliability view from semantic model (#2087034) | Miguel | After access confirmed | LOW (deferred) |

### ADO State Check
- Feature #2087007 — New (correct, not started yet)
- All 4 tasks (#2087032-35) — New (correct, all deferred to mid-May)
- No comments from external stakeholders — all self-authored status notes

### Email/Teams Status
- WorkIQ authentication broken — could not pull emails or Teams chats. Need to re-authenticate.

---

## September 3–8, 2025 — CSX Reliability Dashboard Sprint (Original Working Group Chat)

### Source
- **Teams chat:** "Next Steps: Customer Focused Quality - CSX"
- **Participants:** Ravs Kaur, Sonal Bhargava, Christian Wade, Miso Cilimidžić, Lisa Liu, Ajay Arora, Yoram Atir, David Browne, Kim Manis, Kay Unkroth
- **Context:** CSX (major customer) had an expert escalation going to production. Arun wanted reliability numbers. Team built a unified reliability dashboard in ~1 week.

### CSX Environment
- **4 F512 capacities** (David Browne provided prod/QA breakdown)
- **6 capacities** pulled from Spark side (Lisa Liu)
- Tenant ID available as **report-level filter**

### Dashboard Built by Sonal (Sep 3–4)
| Element | Detail |
|---------|--------|
| Navigation | Left nav panel, consistent structure |
| Time window | 4-week rolling view |
| Filtering | Tenant ID at report level |
| Drill-through | Added for error investigation |
| Metrics | Renamed for cross-workload consistency |
| Visuals | Charts removed, replaced with summary tables |
| Enhancements | Color coding, sorting, null/empty handling |

### Data Sources Identified
| Source | Description | Contact |
|--------|-------------|---------|
| **WSR model (DCP)** | Drill-down info with correlation ID | Yoram Atir |
| **Spark reliability** | Lisa Liu's report (6 capacities); 2 system errors caused dip but didn't impact execution | Lisa Liu |
| **Pipeline Reliability - Runs** | Dashboard shared by Ravs | Ajay Arora |
| **PBI WSR report** | Commonly used for Power BI WSR; Parthiv & Joshua realigning scenarios | Christian Wade |
| **PBI semantic query execution** | Needed right "feature name" for data — still outstanding as of Sep 8 | Sonal |

### Key Technical Points
- **Smoothing** in the report explains why certain dips (e.g., Aug 14) didn't appear in Sonal's dashboard
- **Spark reliability dip** (Sep 3): caused by 2 system errors, did not impact execution, backlog item created
- **Miso's point**: "If meeting SLAs, debugging user errors may not be high priority. Products should allow customers to log errors like Log Analytics."
- **Schema inconsistency**: Each team provides data differently; Sonal built consistency on top

### Monitoring & Alerting Decisions
- **Sonal proposed:** Data Activator alerts — each scenario owner sets thresholds
- **Yoram pushed back:** Must use **KAS/MDM** (standardized tools), not standalone alert logic. Scaling requires standardized events and thresholds. Suggested adding **Dor** to the effort.
- **Ajay asked:** Should alerts apply only to CSX or all customers?
- **Ravs decided:** Start with CSX but **design to scale to all customers**

### Action Items from Sep 3–4 Sessions
1. Sonal: Make left column consistent ✅ (done Sep 4)
2. Debug Aug 14 reliability dip — smoothing explained it
3. Identify reliability causes per workload
4. Remove charts, add summary table ✅ (done Sep 4)
5. Align thresholds across workloads
6. Add CSX-specific monitoring
7. Color coding, sorting, null handling ✅ (done Sep 4)
8. Validate dashboard data across all workloads
9. Define monitoring/alerting strategy (KAS/MDM per Yoram)

### Ownership Transition (Sep 8)
- **Christian Wade** transitioned PBI side to **Kay Unkroth**
- Outstanding items at transition:
  1. PBI semantic query execution — need right feature name for data
  2. Monitoring & alerting setup (all workloads)
  3. Remove "Publish Model Premium" option from report
- Kay asked for list of outstanding items
- Sonal confirmed: PBI needs feature name for semantic query + monitoring/alerting still open

---

## April 28, 2026 — Project Created

### Source Material
- **Transcript:** Knowledge transfer call with Sonal Bhargava (previous owner)
- **Teams chat:** Svetlana Gershaft, Andreas Weber, Nate Findley (+2), Apr 8 2026

### Background (from Sonal)
About 1.5 years ago, CSX had an expert escalation going to production. Arun wanted to see reliability numbers because CSX complained reliability wasn't good enough for production.

The team started tracking a small group of scenarios that were critical for key customers:
- **Spark jobs / Notebooks** — are they reliable?
- **Data Warehouse** — is DW reliable?
- **Semantic models** — are they reliable?

At the time, no central place existed to get this data. Sonal's team worked with each product team individually (e.g., DW team's Misho) and pulled data into their model. This resulted in 3-4 different reliability tables with inconsistent schemas because each team provided data differently.

### Reliability Metric Definitions
- **Reliability** = system errors / total queries (system-only failures)
- **Perceived Reliability** = (system errors + user errors) / total queries (includes user-caused failures)
- Metrics tracked at different grains depending on what each team provides

### Sonal's Key Advice
1. We are **integrators**, not metric owners — each team owns and explains their own metrics. We bring them together.
2. Frame positioning carefully: "We're centralizing so Arun sees everything in one place" — not "we're taking over your reporting."
3. Some friction expected from reliability teams who feel protective of their space.
4. Focus on keeping communications open and ensuring reports reflect current telemetry systems (not legacy ones).

### Current Priority
- **Immediate focus:** Fabric Datawarehouse (DW) reliability only
- **Pipeline and Spark:** Not until July 2026+ — no ETA yet, not urgent
- Sonal will share meeting threads and recordings from previous discussions

### LT Dashboard Issue (from Teams chat, Apr 8)
Svetlana Gershaft raised a concern about the **PBI Connector Authoring and Downstream MAU** report on the LT dashboard:
- Data is "clearly wrong" for Fabric Datawarehouse connector
- Downstream Connector MAU shows ~93.5% YoY drop, Connector Authoring Occurrences shows 141.1% YoY increase
- Svetlana created **IcM Incident-767077695** — problem appears to be the actual data, not their team's report
- Two options proposed: (1) keep report and investigate root cause (DCP or PG), (2) remove from LT dash entirely
- Nate's response: suggested Andreas Weber onboard and potentially move this to Tamas's analytics/reporting team for full coverage

### Open Items
- [ ] Sonal to share meeting threads and recordings for additional context
- [ ] Meet with DW reliability team (Miso Cilimidžić and team) to understand current data pipeline and schema
- [ ] Determine ownership of the connectors report data quality issue (DCP vs. PG vs. us)
- [x] Decide: keep connectors report on LT dash or remove? **→ Keep it (Nate, Apr 29)**
- [x] Create ADO work items once scope is confirmed **→ Feature #2087007, Story #2087023 (Apr 29)**

---

## May 5, 2026 — Sonal Chat: Meeting Moved + Stakeholder Roles Clarified

### Meeting Rescheduled
- Sonal moved the LT Reliability Metrics meeting from May 5 to **mid-May** (exact date TBD)
- Reason: The team mentioned it will take them **a few more weeks**
- Miguel's take: This gives time to have a 1:1 with Miso first to build trust

### Stakeholder Role Clarifications (from Sonal)
- **Shemesh Hamaoui is the hard partner** — he is the central owner who owns reliability and works with each product team. Sonal emphasized: "Miso is not the hard partner here — it's Shemesh."
- **Miso Cilimidžić's role** — PM on the product side. Responsible for answering questions about metric changes on the reliability side. He defined what the most important things to measure are for Epic/CSX etc. Miso has already worked with Shemesh.

### Miguel's Plan
- Use the **Databases Strategy project as a case study** to show Miso how Miguel collaborates with his team and the expected outcomes
- Goal: Assure Miso that Miguel is here to partner and support his success
- Do this **before the rescheduled mid-May meeting**

---

## April 29, 2026 — Stakeholders Identified + Tables Discovered

### Reliability Stakeholders (shared by Sonal, Apr 24)
From Sonal's "Reliability Metrics Stakeholders" doc:
| Person | Area | Notes |
|--------|------|-------|
| **Ravs Kaur** | Uber stakeholder | Asked for all the reliability views |
| **Shemesh Hamaoui** | Central Rel team | Central reliability team contact |
| **Miso Cilimidžić** | DW Reliability | DW team lead — meeting scheduled ~2 weeks from Apr 24 |
| **Ajay Arora** | Pipeline | Pipeline reliability contact (Phase 2, July+) |
| **Lisa Liu** | Spark Job | Spark job reliability contact (Phase 2, July+) |

### Reliability Tables Discovered in Semantic Model
6 tables identified (vs. Sonal's "3-4" estimate):
1. `Fabric Feature Reliability`
2. `Fabric Service Reliability`
3. `Reliability Fabric Pipeline`
4. `Reliability Fabric Spark`
5. `Reliability And Security`
6. `Fabric Capacity Reliability`

**Note:** Need to verify which of these are actively used vs. legacy, and confirm access to all.

### Context on DW Reliability Meeting (Point 4)
Sonal worked directly with Miso Cilimidžić's team for the DW reliability data. They have their own data warehouse instance from which Sonal pulled data. The key things to understand from this meeting:
- **Current schema:** What columns, grains, and error classifications does their DW reliability table expose?
- **Data freshness:** How often does the data update, and what's the latency?
- **Future plans:** Are they migrating to a new telemetry system? Sonal warned that reports need to reflect new systems, not legacy ones.
- **What's missing:** Sonal mentioned some teams had error-level details and others didn't — need to confirm what DW provides.
- **Schema mismatch risk:** The 6 tables have inconsistent schemas because each team provided data differently. Understanding DW's schema first sets the baseline.

### Pipeline & Spark (Point 7)
Tracked for awareness but not urgent — Ajay Arora (Pipeline) and Lisa Liu (Spark) are the contacts. No ETA, not expected until July 2026+. Will revisit after DW reliability is stable.

### Action Items
- [ ] Follow up with Sonal for meeting threads and recordings (asked, not yet received)
- [ ] Ask Nate in 1:1 (Apr 30): keep connectors report on LT dash or remove? Get direction.
- [ ] After Nate's decision: create ADO user story for LT Reliability Metrics + IcM-767077695 resolution
- [ ] Verify access to all 6 reliability tables in the semantic model
- [ ] Schedule meeting with Miso Cilimidžić's DW Reliability team (Sonal said ~2 weeks from Apr 24 = ~May 8)

---

## April 29, 2026 — Connector Report Sync (Apr 24 recording reviewed)

### Meeting: Connector Report Sync — April 24, 2026
**Attendees:** Miguel Myers, Sonal Bhargava, Svetlana Gershaft

### How Connector Metrics Work (explained by Sonal)

**Connector Authoring MAU (top of funnel):**
- Counted when a user clicks "Get Data" in Power BI Desktop and selects a connector (e.g., SQL Server, SharePoint, Oracle)
- Measures **intent** — the click itself is counted regardless of whether the connection succeeds
- A single user connecting to 5 different sources in one model = counted as a user for all 5 connectors
- Same counting logic across all connectors — no per-connector custom process
- Originally built for Power BI Desktop only — does **not** capture service-based or agentic connections

**Downstream Connector MAU (end of funnel):**
- Once a model is published to the service, the system knows which connectors are part of that model (model ID → source list)
- Every user who sends a query to that model is counted as a downstream user of **all** connectors in the model
- Example: 1 creator publishes a model with SQL + SharePoint + PDF → 1,000 report viewers = 1,000 downstream users for each of those connectors

### Root Cause Investigation (IcM-767077695)

**Investigation path so far:**
1. Svetlana filed IcM against her team (IDIA)
2. IDIA confirmed it's not a platform issue, not data ingestion
3. Bhavesh confirmed the same issue occurs in **data creation data**
4. Investigation moved to **Data Creation team**

**Sonal's assessment:** Likely not a data processing issue — it's a **data generation issue**, meaning the PG (product group / DW team) probably changed something on their end. The counting process is the same across all connectors, so if DW numbers dropped while others are fine, the DW team likely changed how they emit telemetry events.

**Svetlana's position:** Two paths — either someone truly owns this report and is ready to act when things go wrong, or remove it from the LT Dash.

**Sonal's framing:** Same principle as databases — you don't own the platform, but you're the integrator. When something breaks, people come to you because they don't know who else to ask. You need to follow up with the DW team to ask why numbers dropped.

### New Questions to Ask DW / Connector Teams
Sonal raised forward-looking questions for Miguel to investigate:
1. **Service-based connections:** Does the current system capture when users connect to a connector in the service (not just Desktop)?
2. **Agentic experience:** When a user creates a report via an agentic experience and says "connect to SQL Server" — does that emit the same event as the Desktop "Get Data" flow?
3. **Relevance check:** Is this metric still valuable as originally built (Desktop-only era), or does it need updating for the current world?

### Key Insight
The connector authoring/downstream system was built ~5 years ago when Power BI Desktop was the only way to build reports. The world has changed significantly (service authoring, agentic AI, etc.). The metric may need modernization beyond just fixing the current data issue.

### Action Items from This Meeting
- [x] Miguel: Ask Nate in 1:1 (Apr 30) — own it or drop it from LT Dash? **→ Keep it (confirmed Apr 29)**
- [ ] Miguel: Follow up with DW team — why did Fabric Datawarehouse downstream MAU drop? What changed in their telemetry? (Task #2087032)
- [ ] Miguel: Ask connector/DI team about service + agentic event coverage (Task #2087033)

---

## April 29, 2026 — ADO Work Items Created + Nate Decision

### Decision
Nate confirmed: **keep the connectors report on the LT Dashboard.** We own the integrator role.

### ADO Items Created
| Type | ID | Title |
|------|-----|-------|
| Feature | #2087007 | LT Reliability Metrics |
| User Story | #2087023 | Investigate and resolve Fabric DW connector MAU data quality issue (IcM-767077695) |
| Task | #2087032 | Resolve DW connector telemetry drop (IcM-767077695) |
| Task | #2087033 | Investigate service-based + agentic event coverage gaps |
| Task | #2087034 | Build DW reliability view from semantic model |
| Task | #2087035 | Document connector metric definitions |

All items: New state, Priority 2, tagged `LT-Reliability`, assigned to Miguel Myers.
