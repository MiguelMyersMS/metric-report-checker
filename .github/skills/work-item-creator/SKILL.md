---
name: work-item-creator
description: "Guided Azure DevOps work item creation. Use when creating features, user stories, tasks, or bugs in ADO. Follows team conventions for hierarchy, states, tags, and sprint assignment. Also use for the ADO workflow interview to set up team conventions."
argument-hint: "e.g., 'create a feature for dashboard redesign with 3 tasks'"
---

# Work Item Creator

## When to Use
- Creating new features, stories, tasks, or bugs in Azure DevOps
- Bulk-creating child tasks under a feature
- Running the ADO workflow interview to configure team conventions

## Procedure

### Creating Work Items
1. Read `brain/AGENTS.md` for ADO config (org, project, area path, conventions)
2. Ask the user for:
   - **Type**: Feature / User Story / Task / Bug
   - **Title**: Clear, descriptive title
   - **Parent**: Link to parent work item (if applicable)
   - **Description**: Acceptance criteria or details
   - **Assignment**: Who it's assigned to
   - **Tags**: Per team conventions
   - **Sprint**: Current or specific iteration
3. Use the [work item template](./templates/work-item-spec.md) to confirm details before creating
4. Create via Azure DevOps MCP tools
5. Confirm with work item ID and link

### ADO Workflow Interview (First-time Setup)
If `brain/AGENTS.md` has placeholder ADO conventions, run this interview:
1. What is your ADO organization URL?
2. What project and area path do you work in?
3. What hierarchy do you use? (Epic → Feature → Story → Task?)
4. What states does your team use? (New → Active → Resolved → Closed?)
5. What tags are standard?
6. What is your sprint cadence? (2 weeks? 3 weeks?)
7. Do you link PRs to work items?
8. What's your daily workflow? (standup → work → PR → update?)
9. Update `brain/AGENTS.md` with the answers

## Templates
- [Work item spec](./templates/work-item-spec.md)
