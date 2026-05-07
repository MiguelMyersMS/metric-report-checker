# Report Requests Skill

## Purpose
Help PMs create, track, and follow up on Power BI report requests and semantic model change requests to engineering.

## When to Use
- Creating a new report request or semantic model change request
- Tracking status of existing requests
- Drafting follow-up communication for stale requests

## Context
- The user does NOT modify databases or semantic models directly — they request changes from the engineering team.
- Requests are logged in `data/metrics/requests.md`.
- Use Power BI MCP (`powerbi-remote/*`) to query current model state for context if needed.

## Constraints
- DO NOT suggest direct database modifications.
- DO NOT assume access to semantic models — always frame as a request to engineering.

## Workflow
1. Understand what report/data change is needed.
2. Draft a clear, specific request for the engineering team (what, why, expected outcome).
3. Log the request in `data/metrics/requests.md` with date, status, and assignee.
4. Draft follow-up communication if a request is stale.

## Request Format

```markdown
### {Request Title}
- **Date**: {YYYY-MM-DD}
- **Type**: Semantic model change / New report / Report modification / Data fix
- **Details**: What needs to change and why
- **Priority**: High / Medium / Low
- **Requested From**: Team or person
- **Status**: Submitted / In Progress / Completed / Blocked
```
