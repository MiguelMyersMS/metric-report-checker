---
name: weekly-summary
description: "Generate a weekly productivity and status summary. Use when asked for weekly report, weekly update, end-of-week summary, or progress review. Queries Azure DevOps for work item status and compiles into a formatted report."
argument-hint: "Optional: specify date range or focus area"
---

# Weekly Summary Generator

## When to Use
- End of week status reporting
- Preparing for weekly team syncs
- Manager check-ins
- Stakeholder updates

## Procedure
1. Query Azure DevOps for work items updated this week (resolved, active, new)
2. Check `data/action-items.md` for completed and pending action items
3. Check `data/follow-ups.md` for overdue follow-ups
4. Read `brain/projects.md` for active project context
5. Format using the [weekly template](./templates/weekly-report.md)
6. Adapt detail level based on audience (ask if unclear)

## Data Sources
- Azure DevOps MCP: work item queries
- `data/action-items.md`: meeting action items
- `data/follow-ups.md`: pending follow-ups
- `brain/projects.md`: project context

## Output
A formatted weekly summary ready to paste into email or Teams.
