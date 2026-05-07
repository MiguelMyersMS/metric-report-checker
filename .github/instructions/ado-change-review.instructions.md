---
description: "Periodic ADO work item change review. Ensures the user stays up to date on state changes, new comments, reassignments, and priority shifts across active work items."
---

# ADO Change Review Protocol

When the user asks for a status check, standup, or project update — or when enough time has passed since the last review — run a **change review** across all active work items.

## What to Check

For every active Feature, User Story, and Task in the user's ADO project:

| Change Type | How to Detect | Why It Matters |
|-------------|---------------|----------------|
| **State changes** | Compare current `System.State` against last known state in `data/project-tracker.md` | A task may have moved to Active or Closed without the user knowing |
| **New comments** | Query `list_work_item_comments` and check for comments newer than the last review | Someone may be waiting on a reply (blocker) |
| **Reassignments** | Check `System.AssignedTo` against last known owner | Work may have shifted to someone else or back to the user |
| **Priority changes** | Check `Microsoft.VSTS.Common.Priority` against tracker | Escalations or de-prioritizations affect planning |
| **New child items** | Query work item with `expand: Relations` | Someone may have added tasks or stories under a Feature |

## Review Cadence

| Trigger | Action |
|---------|--------|
| **Daily standup** (morning) | Full review — all active items, all change types |
| **Mid-day check** | Quick review — comments and state changes only |
| **On-demand status request** | Full review for the requested scope |
| **Before weekly summary** | Full review + compare against prior week |

## Output Format

### Changes Detected
| Work Item | Change Type | Previous | Current | By Whom | When |
|-----------|-------------|----------|---------|---------|------|

### No Changes
If nothing changed, say: "No changes detected since last review on [date]."

### Sync Local Tracker
After every review, update `data/project-tracker.md` to reflect the current ADO state so the next review can detect deltas accurately.

## Rules
- **Always check comments** — unresolved comments are blockers (see devops agent instructions)
- **Always surface reassignments** — if a work item was reassigned away from or to the user, call it out explicitly
- **Never skip the review** when running a standup or status prompt — this is not optional
- **Flag staleness** — if a work item has been in the same state for 5+ days with no activity, flag it as potentially stale
