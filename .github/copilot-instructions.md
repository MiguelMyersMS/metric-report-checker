# Project Guidelines

## What This Workspace Is
My-Ops-Hub is a personal PM command center powered by GitHub Copilot agents, skills, and MCP servers. It manages Azure DevOps workflows, outbound communication, analytics, and project tracking.

## Architecture
- `brain/` — Personal AI brain (AGENTS.md routing rules, projects, skills) aligned with Justin Martin's AI-DevOps pattern
- `.github/agents/` — Custom Copilot agents for specific roles
- `.github/skills/` — On-demand workflow skills with templates
- `.github/prompts/` — Quick-task prompt templates  
- `.github/instructions/` — File-specific guidance
- `data/` — Tracked follow-ups, action items, metrics

## Conventions
- Work items follow ADO hierarchy: Epic → Feature → User Story → Task
- Emails use friendly-but-professional tone
- Status reports adapt to audience (manager / stakeholders / team)
- All agent outputs reference `brain/AGENTS.md` for routing and conventions

## MCP Servers
- **Azure DevOps**: Work item CRUD, sprint queries, backlog management
- **Power BI (Fabric)**: Semantic model queries, report insights
- **Microsoft Graph**: Email, calendar (future)

## Key Commands
- `/weekly-summary` — Generate weekly status + productivity report
- `/follow-up-tracker` — Review and manage pending follow-ups
- `/work-item-creator` — Guided ADO work item creation
