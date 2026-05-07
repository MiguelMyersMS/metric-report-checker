# My Development Brain

## How to Help Me

When I ask for help, follow this process:

### 1. Figure Out What I Need

| Type of Work | How to Handle |
|-------------|---------------|
| Data question (metrics, usage, revenue) | Use the ADIA skill to query semantic models |
| Fabric workspace work (notebooks, warehouses) | Use Fabric Skills |
| ADO work tracking (stories, tasks, sprints) | Use ADO MCP tools |
| Report request (Power BI, semantic model change) | Draft request for engineering, track in `data/metrics/requests.md` |
| Email, follow-up, or message drafting | Draft in friendly-but-professional tone |
| Status report or weekly summary | Query ADO for updates, format using templates |
| Meeting action items or follow-ups | Check `data/action-items.md` and `data/follow-ups.md` |

### 2. Check Project Context

Before making changes in any project, check if there's an `AGENTS.md` or
`.github/copilot-instructions.md` in that repo and read it first.

### 3. ADO Tracking

- **ADO org:** `powerbi` | **Project:** `IP Analytics`
- **Area Path:** (to be assigned — will update once created)
- **My email:** `miguelmyers@microsoft.com`
- When I mention a work item or story, help me track it in ADO
- For ad-hoc work, skip ADO unless I ask

## ADO Work Item Conventions

### Hierarchy
Epic → Feature → User Story → Task
- **Epic**: Large strategic initiative spanning multiple sprints
- **Feature**: PM-owned planning artifact — scopes a deliverable or capability
- **User Story**: A sprint-sized unit of work (what gets picked up and delivered)
- **Task**: Granular sub-work within a story
- **Who creates**: Everyone creates everything (PMs, engineers, analysts)

### Work Item Creation Rules
- **Always respect the hierarchy.** When creating a User Story, ensure a parent Feature exists (or create one). When creating Tasks, ensure a parent User Story exists.
- **Always confirm before creating.** Show the user the full spec (type, title, parent, tasks, assignments) and get approval before calling ADO APIs.
- **One Feature per project.** Each project in `brain/projects/` should map to a Feature in ADO. Store the Feature ID in the project's README.md.
- **Tag consistently.** Use a project-level tag (e.g., `Databases-Strategy`, `LT-Reliability`) on all items under that Feature.

### States & Workflow
- **States**: New → Active → Closed
- **Active means**: Someone has started working on it
- **Done/Closed means**: PM or stakeholder has accepted the work
- **Blocked**: No dedicated state — use tags or comments to flag blocks

### Tags & Priority
- **Tags**: Priority tags (P0 / P1 / P2)
- **Priority tracking**: Use the Priority field for formal prioritization
- **Prioritization framework**: Urgency + dependency blocking + business/stakeholder impact

### Sprints
- **Cadence**: Weekly sprints
- **Assignment**: Self-assigned — pick highest-priority unblocked item
- **Unfinished work**: Re-evaluated and re-prioritized (not auto-rolled forward)

### Collaboration
- **Engineer model**: I write specs, engineers implement
- **PR linking**: Automatic via branch naming conventions
- **Board usage**: ADO Boards / Kanban views (primary)
- **Communication**: Microsoft Teams, Outlook, VS Code (skills + agents)
- **Reports**: Power BI

### Standard Delivery Flow
1. **Requirements definition** — Clarify business needs, expected metrics, use cases
2. **Data modeling** — Define required data structures, fields, calculations
3. **Engineering alignment** — Partner with engineers for data availability + correctness
4. **Report development** — Build Power BI reports (DAX measures, visuals, interactivity)
5. **Validation** — Data validation, ensure metrics align with business definitions
6. **Deployment** — Publish reports, validate refresh pipelines
7. **Post-deployment monitoring** — Track performance/usage, iterate on feedback

### Data Ownership
- Deep understanding of metric definitions and calculations
- Interpret trends, detect anomalies, identify insights
- Support stakeholders with analysis and data validation
- Monitor KPIs: verify refreshes, detect spikes/drops, flag inconsistencies

### Daily Flow
1. **Start**: Check ADO board for assigned/active work items — catch up on status
2. **Prioritize**: Urgency → dependency impact → business value
3. **Execute**: Work through highest-priority items, update ADO states as I go
4. **Communicate**: Update work items with status, flag blockers in Teams/ADO comments
5. **Monitor**: Check owned reports and KPIs for data quality issues
6. **End**: Review progress, re-prioritize for next day

### Documentation
- Metric definitions, DAX logic, data lineage, interpretation notes
- Structured as deliverables, not optional add-ons
- Enables scale, AI copilot context, and team onboarding

### Operating Principles
- ADO is the single source of truth (not mental tracking)
- Every task = work item; every update = status/log in ADO
- Centralize decisions in ADO or docs (avoid "decision buried in chat")
- Continuously refine workflows for automation and efficiency

## Quick Reference: Natural Language Commands

| What You Want | Example Prompt |
|--------------|----------------|
| See your active work | "What am I working on? Catch me up." |
| Create a feature | "Create a new Feature: Dashboard Redesign with 3 child tasks" |
| Query sprint status | "Show me all items in the current sprint for IP Analytics" |
| Find blockers | "What work items are tagged P0 or blocked?" |
| Update a work item | "Move story #12345 to Active" |
| Weekly summary | "Generate my weekly summary from ADO" |
| Create a task | "Create a task under Feature #12345: Review data model changes" |
| Check assignments | "What's assigned to me that's still New?" |

## My Projects

See `projects.md` for a list of projects and their details.

## Communication Preferences
- **Email tone**: Friendly but professional
- **Status reports**: Adaptable for mixed audiences (manager, stakeholders, team)
- **Follow-up style**: Concise, action-oriented, with clear deadlines

## Meetings
- Weekly team syncs
- Monthly stakeholder reviews
- Ad-hoc as needed
