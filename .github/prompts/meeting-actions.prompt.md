---
description: "Extract action items from meeting notes. Logs them to the follow-up tracker and optionally creates ADO work items."
agent: "comms"
---

Extract action items from the following meeting notes.

1. Identify all action items with owner, description, and due date
2. Log each to `data/action-items.md`
3. Check `data/follow-ups.md` for duplicates before adding
4. Ask if any action items should become Azure DevOps work items
5. Summarize what was logged

Meeting: {{meeting name or paste notes below}}
Date: {{meeting date}}
