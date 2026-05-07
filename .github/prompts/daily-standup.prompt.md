---
description: "Morning standup — live project status, blockers, and follow-up suggestions from ADO."
agent: "ops-commander"
---

Run my daily standup check-in. Do this in order:

## 1. Pull Live ADO Status & Detect Changes
Query Azure DevOps (project: IP Analytics) for all **active Features and their child Tasks** assigned to me or where I'm involved. For each:
- Show: ID, Title, State, Assigned To, Priority
- Group by **Feature** (parent), then list child Tasks underneath
- Highlight anything **overdue** or approaching a deadline

**Run the ADO Change Review** (per `.github/instructions/ado-change-review.instructions.md`):
- Compare current ADO state against `data/project-tracker.md`
- Flag: state changes, reassignments, priority changes, new child items, stale items (5+ days no activity)
- Format detected changes as:

| Work Item | Change Type | Previous | Current | By Whom | When |
|-----------|-------------|----------|---------|---------|------|

If no changes, say "No changes since last review."

## 2. Morning Dashboard
Format as a table:

| Feature | Task | State | Owner | Priority | Deadline | Flag |
|---------|------|-------|-------|----------|----------|------|

Flags: 🔴 Overdue | 🟡 Due this week | 🟢 On track | ⚪ Not started

## 3. Check ADO Comments Requiring Response
For every **active Feature, User Story, and Task** surfaced in Step 1, query Azure DevOps for **comments** (use `list_work_item_comments`). Flag any comment that:
- Asks a question directed at me or the team
- Requests clarification, a decision, or additional info
- Is unresolved and blocks the item from progressing toward Closed

Format as:

| Work Item | Commenter | Date | Summary | Action Needed |
|-----------|-----------|------|---------|---------------|

This is **critical** — unresolved comments are blockers to closing work items.

## 4. Check Project Context
Read `brain/projects/` for all active projects. Cross-reference ADO tasks with project history files (e.g., `history.md`) to surface:
- Recent decisions that affect today's work
- Open action items from previous follow-ups

## 5. Check Follow-ups
Read `data/follow-ups.md` and `data/action-items.md` for anything due today or overdue.

## 6. Suggest Actions
Based on the above, recommend:
- **Comments to reply to** (work item ID, who asked, what to say)
- **Follow-ups to send** (who, about what, why it's urgent)
- **Blockers to escalate** (what's stuck, who to ping)
- **Items to close** (tasks that look done but haven't been marked closed)

## 7. Summary Paragraph
End with a 3-sentence paragraph I can use as my "latest status" if anyone asks.

Focus on: {{focus or "all active projects"}}
