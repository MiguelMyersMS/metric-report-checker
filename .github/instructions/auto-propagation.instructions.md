---
description: "Apply when editing brain or data files. Suggests propagating updates to related documents and systems. Does NOT auto-write to ADO or external systems without user approval."
applyTo: ["brain/**", "data/**"]
---

# Auto-Propagation Rule

When the user shares new project information — a status change, a decision, a data correction, a blocker resolved, or any other project-relevant fact — **suggest propagating that information to related locations** and proceed only with local file updates automatically. ADO and external systems require user approval.

## Checklist (evaluate every item on every update)

### Local Files (auto-OK)
- [ ] **Project history** (`brain/projects/<project>/history.md`) — append a dated entry with the new information
- [ ] **Project README** (`brain/projects/<project>/README.md`) — update decisions log, metrics, status, or acceptance criteria as applicable
- [ ] **Follow-ups tracker** (`data/follow-ups.md`) — create, update, or close follow-up entries
- [ ] **Action items** (`data/action-items.md`) — add, update, or mark done
- [ ] **Email drafts** (`data/drafts/`) — update any open draft that references the changed information
- [ ] **Project tracker** (`data/project-tracker.md`) — update if milestone or timeline changed

### Azure DevOps (ask first)
- [ ] **Work item comments** — suggest adding a comment to affected ADO work items
- [ ] **Work item state** — suggest state change (New → Active → Closed) if warranted
- [ ] **Work item fields** — suggest updates to description, tags, or assigned-to if relevant

### Engagement Files (ask first)
- [ ] **Customer files** (`customer-engagement/customers/`) — suggest update if customer-facing info changed
- [ ] **Feature files** (`customer-engagement/features/`) — suggest update if feature status changed

## Rules

1. **Local files (brain/, data/)**: update automatically and report what changed.
2. **ADO and external systems**: propose changes and wait for approval before executing.
3. **Show a summary** of all files updated and all external changes proposed.
4. **If information contradicts** something already recorded, flag the contradiction and update to the latest information.
5. **Cross-reference** — when updating one document, check if the same fact appears in other documents and update those too.
6. **Date-stamp** all new entries in history and follow-up files.
