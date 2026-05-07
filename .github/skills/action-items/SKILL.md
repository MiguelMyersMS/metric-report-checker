---
name: action-items
description: "Patterns for extracting action items from emails, meetings, documents, and engagement notes. Converts unstructured content into TODO checkboxes with owners and dates."
---

# Action Items

Patterns and heuristics for extracting action items from unstructured content — emails, meeting notes, documents, and engagement materials. This skill converts natural-language commitments into standardized TODO checkboxes with owners and dates.

## When to Use

Load this skill when:
- Extracting action items from emails, meetings, or documents
- Processing engagement content into TODO lists
- Updating a customer's `TODO.md` file
- The `@engagement-orchestrator` is completing Step 7 (Update Customer Files)
- Summarizing M365 content with action items via `workiq` MCP

## Output Format

All action items use this checkbox format:

```markdown
- [ ] {Action description} — {Owner} — {Due date if available}
```

Examples:
```markdown
- [ ] Send updated capacity report to customer — Sarah Chen — 2026-04-01
- [ ] Schedule follow-up call with engineering team — PM — next week
- [ ] Share Direct Lake migration guide with customer DBA — unassigned
```

### Fields

| Field | Required | Notes |
|-------|----------|-------|
| Action description | Yes | Clear, specific, actionable verb phrase |
| Owner | If identifiable | Person's name, role, or "unassigned" |
| Due date | If mentioned | ISO 8601 date, or relative ("next week", "by EOW") |

### Source Attribution

When extracting from a specific source, add attribution:

```markdown
- [ ] Send updated capacity report — Sarah Chen — 2026-04-01 *(from: 2026-03-25 email re: Nokia capacity review)*
```

## Extraction Heuristics

### Keyword Triggers

Look for these patterns in text that signal an action item:

| Category | Keywords/Patterns |
|----------|------------------|
| **Commitments** | "I will", "I'll", "we will", "we'll", "let me", "I can" |
| **Requests** | "can you", "could you", "please", "would you mind" |
| **Assignments** | "action on", "assigned to", "{name} to", "take the action" |
| **Deadlines** | "by {date}", "before {event}", "deadline", "due", "EOD", "EOW", "EOM" |
| **Follow-ups** | "follow up", "circle back", "reach out", "get back to", "loop in" |
| **Next steps** | "next step", "going forward", "action item", "TODO", "to-do" |
| **Scheduling** | "schedule", "set up", "book", "arrange", "plan" |

### Context Clues

Beyond keywords, look for:
- **Imperative verbs at paragraph start**: "Send the report", "Update the config"
- **Future tense commitments**: "We're going to review this with engineering"
- **Conditional actions**: "If the data shows X, we'll need to Y"
- **Meeting agenda follow-ups**: Items marked "discussed" or "decided" that need execution

### What is NOT an Action Item

- Observations ("NPS dropped by 5 points")
- Decisions already completed ("We decided to use Direct Lake")
- Background context ("The customer has been using Fabric since Q2")
- Questions without assigned follow-up ("What's the timeline?")

## Priority Inference

When the source text signals urgency, tag the action item:

| Priority | Signals | Prefix |
|----------|---------|--------|
| **Urgent** | "ASAP", "immediately", "critical", "blocking", "today" | `🔴` |
| **High** | "this week", "priority", "important", "soon" | `🟡` |
| **Normal** | No urgency signals, reasonable deadline | (none) |

Example:
```markdown
- [ ] 🔴 Escalate capacity issue to engineering — PM — today *(from: Sev A escalation email)*
- [ ] 🟡 Prepare competitive analysis for EBC — PM — by Friday
- [ ] Review customer's migration timeline — PM — next sync
```

## De-duplication Rules

When extracting from multiple sources (emails, meetings, documents), the same action item may appear multiple times:

1. **Exact duplicates**: Same action, same owner → keep one, note all sources
2. **Evolved duplicates**: Same action refined over time → keep the most recent/specific version
3. **Related but distinct**: Similar actions with different scopes → keep both, clarify distinction

Example of de-duplication:
```markdown
# Before (duplicates from email + meeting):
- [ ] Send capacity report to Nokia — Sarah
- [ ] Share the capacity report with Nokia team — Sarah

# After (de-duplicated):
- [ ] Send capacity report to Nokia team — Sarah *(from: email 3/25 + meeting 3/26)*
```

## Integration with Customer TODO.md

When updating a customer's `TODO.md` file:

### File Structure

```markdown
# {Customer Name} — TODO

Action items across all engagements for this customer.

## In Progress
- [ ] {Active items being worked on}

## Up Next
- [ ] {Items queued for near-term action}

## Someday
- [ ] {Lower priority items without deadlines}

## Done
- [x] {Completed items with completion date}
```

### Placement Rules

- **Urgent / High priority**: Add to "In Progress"
- **Normal priority with deadline**: Add to "Up Next"
- **No deadline, no urgency**: Add to "Someday"
- **Previously open, now resolved**: Move to "Done" with `- [x]` and date

### Carry-Forward

When preparing a new engagement:
1. Read the customer's `TODO.md`
2. Carry unchecked items from "In Progress" and "Up Next" into the engagement's Open Items section
3. Mark the source: `(carried from TODO.md)`
4. After the engagement, update `TODO.md` with any new items and mark completed ones

## Processing Large Content

When processing long emails, meeting transcripts, or documents:

1. **Scan for action-oriented sections first**: "Next Steps", "Action Items", "Follow-ups", "Decisions"
2. **Then scan body text**: Look for keyword triggers and context clues
3. **Attribute each item**: Note which section/paragraph it came from
4. **De-duplicate**: Remove overlaps between explicit action sections and body text mentions
5. **Validate**: Ensure each extracted item is genuinely actionable (not an observation or decision already made)
