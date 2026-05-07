---
description: "Generate a formatted status report for stakeholders. Adapts detail level based on audience."
agent: "analytics"
---

Generate a status report for my current projects.

1. Query Azure DevOps for all active work items in my project
2. Group by: Completed, In Progress, Blocked
3. Read `brain/projects.md` for project context
4. Format the report for the specified audience:
   - **Manager**: Focus on progress, blockers, and asks
   - **Stakeholders/Leadership**: Executive summary, milestone progress, risks
   - **Team**: Detailed task-level breakdown

Audience: {{audience or "mixed — include all sections"}}

Include a 3-sentence executive summary at the top regardless of audience.
