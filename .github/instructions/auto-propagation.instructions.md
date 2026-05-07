---
description: "ALWAYS APPLY when receiving any new project information, status update, decision, or data point from the user. Ensures every relevant document and system is updated automatically without waiting for explicit instructions."
applyTo: ["**"]
---

# Auto-Propagation Rule

When the user shares **any** new information — a status change, a decision, a data correction, a conversation insight, a blocker resolved, a new blocker, a person update, or any other project-relevant fact — **immediately propagate that information to ALL affected locations** without being asked.

## Checklist (evaluate every item on every update)

### Local Files
- [ ] **Project history** (`brain/projects/<project>/history.md`) — append a dated entry with the new information
- [ ] **Project README** (`brain/projects/<project>/README.md`) — update decisions log, metrics, status, or acceptance criteria as applicable
- [ ] **Follow-ups tracker** (`data/follow-ups.md`) — create, update, or close follow-up entries
- [ ] **Action items** (`data/action-items.md`) — add, update, or mark done; update the "Status at a Glance" table if project health changed
- [ ] **Email drafts** (`data/drafts/`) — update any open draft that references the changed information
- [ ] **Project tracker** (`data/project-tracker.md`) — update if milestone or timeline changed

### Azure DevOps
- [ ] **Work item comments** — add a comment to any ADO work item affected by the update
- [ ] **Work item state** — change state (New → Active → Closed) if the update warrants it
- [ ] **Work item fields** — update description, tags, or assigned-to if relevant

### Engagement Files (if applicable)
- [ ] **Customer files** (`customer-engagement/customers/`) — update if customer-facing info changed
- [ ] **Feature files** (`customer-engagement/features/`) — update if feature status changed

## Rules

1. **Do not ask permission** to propagate. Just do it and report what was updated.
2. **Show a summary** of all files and systems updated after propagation is complete.
3. **If a work item should be closed**, confirm with the user before changing state to Closed (state changes are hard to reverse).
4. **If information contradicts** something already recorded, flag the contradiction and update to the latest information.
5. **Cross-reference** — when updating one document, check if the same fact appears in other documents and update those too.
6. **Date-stamp** all new entries in history and follow-up files.
