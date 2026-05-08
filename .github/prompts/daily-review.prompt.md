---
description: "Run the full daily operations review — sweep ADO, Email, Teams, cross-reference, update docs, propose changes, draft messages. Use for 'daily review', 'catch me up', 'what did I miss', 'morning review'."
---

Run the **daily-ops-review** skill (`.github/skills/daily-ops-review/SKILL.md`).

Execute all 6 phases in order:
1. **Gather** — ADO status + change detection, Email scan, Teams scan, ADO comments
2. **Analyze** — Cross-reference findings, identify actions, priority sort
3. **Update docs** — history.md, action-items.md, follow-ups.md, project-tracker.md
4. **Propose ADO changes** — Present numbered list, wait for approval
5. **Draft messages** — Follow-ups, pings, meeting briefs to data/drafts/
6. **Clean up** — Delete sent drafts, final sync, session summary

Scope to all active projects in `brain/projects/`.
Use WorkIQ CLI for email/Teams if MCP auth is broken.
