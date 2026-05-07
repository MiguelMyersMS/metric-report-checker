---
name: follow-up-tracker
description: "Track, review, and manage follow-ups with coworkers. Use when logging a follow-up, checking overdue items, reviewing what's pending, or generating follow-up reminders. Covers meeting action items and conversation threads."
argument-hint: "e.g., 'log follow-up with Sarah about data model' or 'show overdue'"
---

# Follow-up Tracker

## When to Use
- After meetings to log action items
- When you need to check what's overdue
- Before 1:1s to prepare talking points
- When drafting follow-up messages

## Procedure

### Logging a New Follow-up
1. Ask: Who? What? By when?
2. Append to `data/follow-ups.md` using the [follow-up template](./templates/follow-up-entry.md)
3. Confirm the entry was added

### Reviewing Pending Follow-ups
1. Read `data/follow-ups.md`
2. Highlight overdue items (past due date)
3. Group by person or project
4. Suggest which to prioritize

### Logging Meeting Action Items
1. Ask for meeting name/date and the action items
2. Append to `data/action-items.md` using the [action item template](./templates/action-item-entry.md)
3. Cross-reference with existing follow-ups to avoid duplicates

### Generating Reminders
1. Read `data/follow-ups.md` for items due soon or overdue
2. Draft a concise follow-up message per item
3. Use friendly-but-professional tone

## Data Files
- `data/follow-ups.md` — All tracked follow-ups
- `data/action-items.md` — Meeting-sourced action items
