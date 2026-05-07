# My-Ops-Hub — AI Context

## What This Is
Personal PM command center for Miguel Myers (miguelmyers@microsoft.com), IP Analytics team, Power BI org.

## Trust Levels
- **Auto-OK:** Update local files (brain/, data/), track follow-ups, summarize meetings
- **Ask first:** Create ADO items, draft emails, modify code, update engagement files
- **Never auto:** Send emails, publish reports, change shared resources

## How to Help Me

| Type of Work | How to Handle |
|---|---|
| Data question (metrics, usage, revenue) | Use ADIA skill to query semantic models |
| Fabric workspace work | Use Fabric Skills |
| ADO work tracking | Use ADO MCP tools — always confirm before creating |
| Report request | Draft for engineering, track in `data/metrics/requests.md` |
| Email / follow-up / message | Draft in friendly-but-professional tone |
| Status report or weekly summary | Query ADO, format using `.github/prompts/` templates |
| Meeting action items | Check `data/action-items.md` and `data/follow-ups.md` |

## Workspace Layout
- `brain/` — Projects, routing, AI context
- `brain/projects.md` — All registered projects and how they connect
- `.github/agents/` — Copilot agents (specific roles)
- `.github/skills/` — On-demand workflow skills
- `.github/prompts/` — Quick-task templates
- `.github/instructions/` — File-scoped guidance
- `data/` — Follow-ups, action items, metrics, drafts
- `customer-engagement/` — Customer and feature tracking (ask first)

## ADO Config
- **Org:** powerbi | **Project:** IP Analytics
- **Hierarchy:** Epic → Feature → User Story → Task
- **States:** New → Active → Closed
- **Sprints:** Weekly, self-assigned
- **Tags:** Project-level (e.g., `Databases-Strategy`, `LT-Reliability`)
- **Rule:** One Feature per project in `brain/projects/`. Store Feature ID in project README.

## Work Item Creation Rules
1. Respect the hierarchy — ensure parent exists before creating children.
2. Show full spec (type, title, parent, tasks) and get approval before calling ADO APIs.
3. Tag consistently with project-level tag.

## Standard Delivery Flow
Requirements → Data modeling → Eng alignment → Report development → Validation → Deploy → Monitor

## MCP Servers
- **Azure DevOps:** `mcp.dev.azure.com/powerbi` — work items, sprints, backlog
- **Power BI:** `msitapi.fabric.microsoft.com` — semantic model queries
- **WorkIQ, Learn, Dataverse:** workspace-level (see `.vscode/mcp.json`)

## Operating Principles
- ADO is the single source of truth — not mental tracking.
- Execute + suggest next steps for approval.
- When updating one document, cross-reference and update related docs too.
- Date-stamp all history and follow-up entries.
