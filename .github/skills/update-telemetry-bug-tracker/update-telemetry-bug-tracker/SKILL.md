---
name: update-telemetry-bug-tracker
description: 'Refreshes the telemetry bug tracking table in JTBD/telemetry-bug-tracking.md with live data from Azure DevOps. Use when asked to "update the telemetry tracker", "refresh bug statuses", "sync ADO status", or "update the bug table". Fetches current State and most recent comment for each work item using the ADO MCP server and overwrites the State and Most Recent Comment columns in the markdown table.'
---

# Update Telemetry Bug Tracker

Automates syncing the `JTBD/telemetry-bug-tracking.md` table with live Azure DevOps data. Refreshes the **State** and **Most Recent Comment** columns for every work item in the table.

## When to Use This Skill

- User says "update the telemetry tracker", "refresh the bug table", or "sync ADO status"
- User wants to know whether any bugs have changed state since the last update
- Before a standup, sprint review, or status check on telemetry bugs

## Prerequisites

- ADO MCP server must be running (project: **Trident**, org: **powerbi**)
- The file `JTBD/telemetry-bug-tracking.md` must exist in the workspace

## Step-by-Step Workflow

### Step 1: Read the tracking file

Read `JTBD/telemetry-bug-tracking.md` to extract all work item IDs from the **ADO Number** column.

The table uses this format:
```
| Associated Task | ADO Number | Link | Description | State | Most Recent Comment |
| Get data from Azure Event Hubs | 2027766 | ...
```

Parse each row and collect the numeric IDs from the **ADO Number** column (e.g., `[2027766, 2027778, ...]`).

### Step 2: Batch fetch work item states

Call `mcp_ado_wit_get_work_items_batch_by_ids` with:
- `project`: `Trident`
- `ids`: all work item IDs from Step 1
- `fields`: `["System.Id", "System.State", "System.Title"]`

Record the `System.State` for each ID.

Also note which items have a `commentVersionRef` in the response — these have at least one comment.

### Step 3: Fetch most recent comment for items that have comments

For each work item where the batch response included a `commentVersionRef`, call `mcp_ado_wit_list_work_item_comments` with:
- `project`: `Trident`
- `workItemId`: the item's ID

From the returned `comments` array, take the entry with the **highest `id`** value (most recent). Extract:
- `createdBy.displayName` — commenter name
- `createdDate` — date (format as `YYYY-MM-DD`)
- `text` — strip HTML tags, truncate to a readable single sentence if long

Format as: `**Display Name** (YYYY-MM-DD): <plain text of comment>`

For items with no `commentVersionRef`, use `—`.

### Step 4: Update the markdown table

For each row in the table, replace the **State** column value with the freshly fetched state, and replace the **Most Recent Comment** column value with the formatted comment string from Step 3.

Preserve all other columns (ADO Number, Link, Description) exactly as they are.

### Step 5: Confirm completion

After saving the file, report a brief summary of changes — which items changed state and which have new comments since the last update.

## Notes

- The table header row is: `| ADO Number | Link | Description | State | Most Recent Comment |`
- Items with no comments should show `—` in the Most Recent Comment column
- HTML in comment `text` fields must be stripped to plain text before writing to the markdown table
- Do not reorder rows or alter the Description column
