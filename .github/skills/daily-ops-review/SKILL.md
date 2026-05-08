---
name: daily-ops-review
description: "Full daily operations review: gather intelligence from ADO + Email + Teams, cross-reference findings, update local docs, propose ADO changes, draft outbound messages, and sync trackers. Use when asked to 'run daily review', 'check my status across everything', 'daily ops', 'morning review', 'what did I miss', or 'catch me up'. Orchestrates devops, comms, and analytics agents in sequence."
---

# Daily Ops Review

A 6-phase deterministic workflow that sweeps ADO, Email, and Teams for project-relevant updates, cross-references findings, proposes actions, and syncs all local tracking files.

## When to Use
- Start of day: "catch me up" / "what did I miss"
- End of day: "sync everything" / "daily review"
- After being away: "what happened while I was out"
- Before a status meeting: "prep me"

## Prerequisites
- Azure DevOps MCP connected
- WorkIQ CLI available (`npx -y @microsoft/workiq ask`)
- Local files current: `data/project-tracker.md`, `data/action-items.md`, `data/follow-ups.md`
- Project folders exist in `brain/projects/`

---

## Phase 1 — Gather Intelligence (Agent: `devops`)

**Goal:** Pull current state from all external sources.

### Step 1.1: ADO Status Sweep
1. Query all **active Features** assigned to me in IP Analytics
2. For each Feature, query all **child work items** (Stories, Tasks)
3. Capture: ID, Title, State, Assigned To, Priority, Last Updated
4. Query **comments** on every active item (per `ado-change-review.instructions.md`)

### Step 1.2: ADO Change Detection
1. Compare live ADO state against `data/project-tracker.md`
2. Flag: state changes, reassignments, priority shifts, new children, stale items (5+ days), new comments from others
3. Format changes as a diff table

### Step 1.3: Email Scan (WorkIQ CLI)
**Auth optimization:** Minimize WorkIQ invocations to reduce auth pop-ups. Combine all email questions into ONE broad query covering all active projects, key people, and the date range. Use a single terminal session so the token cache persists.

1. Run **one combined query** covering all projects and people:
```
npx -y @microsoft/workiq ask -q "Show me all emails from [date range] related to [Project1], [Project2], [Project3], or involving [Person1], [Person2], [Person3], etc. Include sender, date, subject, and key content for each."
```
2. If the combined query misses something specific, run **at most one follow-up** in the same terminal
3. Capture: subject, sender, date, key content, action items

### Step 1.4: Teams Chat Scan (WorkIQ CLI)
**Auth optimization:** Same terminal, one broad query covering both channels and DMs.

1. Run **one combined query** covering all channels and key people:
```
npx -y @microsoft/workiq ask -q "Show me Teams chats and channel messages from [date range] in [Channel1] or [Channel2], and any DMs with [Person1], [Person2], etc. about [Topic1], [Topic2]."
```
2. If a known conversation was missed, run **at most one targeted follow-up** in the same terminal
3. Always run WorkIQ commands in the **same terminal session** to reuse cached tokens

**Rule: Maximum 3 WorkIQ CLI invocations per daily review.** Combine aggressively.

### Step 1.5: ADO Comment Review
1. Surface new comments from others (not self-authored)
2. Flag comments that ask questions, request info, or need decisions
3. These are treated as **blockers** until addressed

---

## Phase 2 — Analyze & Cross-Reference (Agent: `analytics`)

**Goal:** Turn raw findings into actionable intelligence.

### Step 2.1: Cross-Source Analysis
For each project, compare findings across ADO + Email + Teams:
- Are there conversations about work items that aren't reflected in ADO state?
- Are there overdue items someone mentioned completing?
- Are there new blockers or decisions made outside ADO?
- Are there discrepancies between what people said and what ADO shows?

### Step 2.2: Identify Actions
Categorize every finding into one of:

| Action Type | Example |
|-------------|---------|
| **State fix** | Item discussed as active but ADO shows New |
| **New task** | Conversation revealed work not yet tracked |
| **Comment to post** | Status update or question to capture in ADO |
| **Follow-up needed** | Someone owes something or needs a nudge |
| **Meeting to schedule** | Alignment needed with a stakeholder |
| **No action** | FYI only — log in history |

### Step 2.3: Priority Sort
Order actions by: Urgency → Dependency blocking → Business impact

---

## Phase 3 — Update Local Docs (Auto-OK, no approval needed)

**Goal:** Sync all local tracking files with findings.

### Step 3.1: Project History
For each project with findings, append a dated entry to `brain/projects/<project>/history.md`:
- Source sections: Email Findings, Teams Findings, ADO Comment Review
- Outstanding Actions table
- ADO State Check

### Step 3.2: Action Items
Update `data/action-items.md`:
- Refresh Status at a Glance table
- Add new actions from Phase 2
- Mark completed items
- Update deadlines

### Step 3.3: Follow-ups
Update `data/follow-ups.md`:
- Add new follow-up entries (with person, topic, due date, ADO ref)
- Update status on existing entries
- Flag overdue items

### Step 3.4: Project Tracker
Update `data/project-tracker.md`:
- Sync states with live ADO
- Add new tasks discovered
- Update milestones

---

## Phase 4 — Propose ADO Changes (Requires approval)

**Goal:** Present a numbered, actionable list for user approval.

### Format
Present ALL proposed changes as a single numbered list:

```
Proposed ADO Changes:
1. [TYPE] #ID — Description (reason from findings)
2. [TYPE] #ID — Description
...
N. [TYPE] — New item description (parent: #ID)
```

Types: `STATE CHANGE`, `COMMENT`, `NEW TASK`, `ASSIGN`, `PRIORITY`

### Rules
- **Show all at once** — user approves/rejects per item
- **Never execute without approval**
- Wait for user to specify which numbers to execute (e.g., "all except 4")
- Execute approved changes in batch

---

## Phase 5 — Outbound Communication (Agent: `comms`)

**Goal:** Draft messages for people who need follow-ups, pings, or meeting briefs.

### Step 5.1: Identify Recipients
From Phase 2 actions, list everyone who needs a message:
- Overdue item owners → follow-up nudge
- New task assignees → assignment notification
- Meeting participants → talking points / brief

### Step 5.2: Draft Messages
For each recipient, draft to `data/drafts/`:
- **Follow-ups/pings:** `<name>-<topic>-<date>.draft.md`
- **Meeting briefs:** `<name>-<meeting-type>-<date>.draft.md`

Follow communication standards (`.github/instructions/communication.instructions.md`):
- Emails/DMs: friendly-professional, under 200 words, clear ask
- Meeting briefs: 5 numbered sections, collaborative tone, tables not prose

### Step 5.3: User Review & Send
- Present drafts for review
- User edits and sends manually (no Graph MCP yet)
- After user confirms sent → **delete the draft files**

---

## Phase 6 — Clean Up & Sync

**Goal:** Final consistency pass.

### Step 6.1: Delete Sent Drafts
After user confirms messages were sent, delete from `data/drafts/`

### Step 6.2: Final Tracker Sync
Re-read `data/project-tracker.md` and confirm it matches all ADO changes made in Phase 4

### Step 6.3: Session Summary
Output a brief summary:
- Sources scanned (ADO items count, email threads, Teams chats)
- Changes made (state fixes, comments posted, tasks created)
- Messages drafted and sent
- Open items for tomorrow

---

## Agent Routing

| Phase | Primary Agent | Skills Used | Tools |
|-------|--------------|-------------|-------|
| 1 — Gather | `devops` | `ado-change-review` | ADO MCP, WorkIQ CLI |
| 2 — Analyze | `analytics` | — | read files |
| 3 — Update docs | orchestrator | `follow-up-tracker`, `action-items` | file edit |
| 4 — ADO changes | `devops` | `work-item-creator` | ADO MCP |
| 5 — Communication | `comms` | — | file create |
| 6 — Clean up | orchestrator | — | file delete |

---

## Workflow vs Agent Decision Rule

| Step | Type | Why |
|------|------|-----|
| ADO query + change detection | **Workflow** | Deterministic, same every time |
| Email/Teams scan | **Workflow** | Repeatable query pattern |
| Cross-reference analysis | **Agent** | Requires reasoning about connections |
| History/tracker updates | **Workflow** | Append-only, structured format |
| Propose ADO changes | **Agent** | Requires judgment on what to propose |
| Draft messages | **Agent** | Requires tone/context adaptation |
| Delete drafts | **Workflow** | Simple cleanup |

---

## Error Handling

| Failure | Recovery |
|---------|----------|
| WorkIQ auth broken | Fall back to CLI (`npx -y @microsoft/workiq ask`). If CLI also fails, run re-auth protocol (see `/memories/repo/workiq-mcp-auth.md`) |
| ADO MCP disconnected | Retry once. If still down, report and skip to Phase 3 with stale data |
| No email/Teams findings | Log "no findings" in history, continue to ADO-only analysis |
| User rejects all ADO changes | Skip Phase 4, proceed to Phase 5 |

---

## Improvement Loop

After each run, ask:
1. Did I miss any source you expected me to check?
2. Were the proposed actions useful or noisy?
3. Any new people/channels to add to the scan list?

Log feedback to session memory for same-day re-runs, and to user memory for persistent improvements.
