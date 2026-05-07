---
description: "Use when editing or viewing follow-up and action item data files. Ensures consistent formatting and prevents data loss."
applyTo: "data/**"
---

# Data File Conventions

- Always append new entries — never overwrite existing ones
- Use the templates from `.github/skills/follow-up-tracker/templates/`
- Mark completed items with `Status: Done` instead of deleting them
- Include dates in YYYY-MM-DD format
- Keep entries in reverse chronological order (newest first)

## Cross-Project Data Sync Rule

Whenever a project is created, updated, or receives new information (emails, transcripts, meetings, ADO changes), **always check and update all three data files** without being asked:

1. **`data/action-items.md`** — Every project must have its own action items section. Add/update items as new tasks, decisions, or deliverables emerge.
2. **`data/follow-ups.md`** — Every person or team you're waiting on must have a follow-up entry. Add new follow-ups as they arise from any project.
3. **`data/project-tracker.md`** — Every project with ADO work items must have a tracker section showing current task states, milestones, and health.

**Trigger:** Any time you process project-related information (emails, transcripts, ADO updates, new work items, stakeholder conversations), scan all three files and update them. Do not wait to be reminded.
