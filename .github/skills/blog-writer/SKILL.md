---
name: blog-writer
description: "Use when writing, drafting, editing, or creating blog posts about Microsoft Fabric features or product announcements. Handles the full blog writing workflow: gathering requirements, researching the feature, planning an outline, writing content, applying Microsoft style guidelines, and validating the final output. Trigger when: user asks to write a blog, draft a post, create a feature announcement, or needs to review or update existing blog content for Fabric or Power BI."
---

# Blog Writer

## Quick Reference

| Phase | Description | Reference |
|-------|-------------|-----------|
| 1 | Gather requirements | Below |
| 2 | Research | Below |
| 3 | Plan & outline | [Blog structure](#blog-structure) |
| 4 | Write content | Below |
| 5 | Apply style guide | [style-guide.md](./references/style-guide.md) |
| 6 | Validate & deliver | [validation.md](./references/validation.md) |

## Blog Posts vs. Docs

A blog post links to the relevant docs to amplify what's been updated and highlights what's new, raising awareness for customers that they should explore the latest. Lengthy step-by-step guidance or tutorials belong in docs; a blog post is not a workaround for updating docs.

Standalone blog posts are intentionally timebound and may lose relevance as products evolve, but documentation remains the enduring, authoritative record that is maintained to reflect the current state of the service. Docs are the source of truth. Blogs are the conversation around that truth.

## Environment Detection

Before starting, detect your operating environment:

- **VS Code / Local IDE**: File creation tools are available (`edit`, `shell`, or `createFile`) — deliver the final blog as a `.docx` file suitable for direct submission to WordPress.
- **GitHub Web Interface**: File creation tools are unavailable or you're running in the GitHub web UI — output the final blog as formatted Markdown in chat, labeled "Blog Content (copy to Word)" so the user can copy it into a Word document.

To detect your environment: attempt to check if file creation capabilities are available. If you cannot create files, assume you're in the GitHub web interface and output text directly.

## Workflow

Use the task tracking tool to create and manage a task list at the start of the session. Create all phase todos upfront, mark them in-progress as you work on each phase, and mark them completed when done. Do NOT create task lists in the chat — always use the task tracking tool so the task list appears above the chat input.

---

### Phase 1: Gather Requirements

Ask the following questions **one at a time**, waiting for an answer before asking the next:

1. What is the feature or topic of the blog?
2. Does the user have specifications, related documentation, or other content for reference? (Can be pasted into chat.)
3. If no specifications exist, can the user describe the feature and the necessary elements for the blog content?

**Target lengths:**
- Standalone blog: ~1,140–1,285 words (enterprise guidance based on SEO research and engagement metrics)
- Industry standards suggest 1,500–2,500 words for optimal SEO and engagement, but quality and relevance matter more than length

Update the task list to reflect the completion of Phase 1.

---

### Phase 2: Research

Gather comprehensive context before writing. Do NOT write plans, implement code, or pause for user feedback during this phase. Use available resources:

- Specifications or content provided by the user
- Existing documentation within the repository
- Microsoft Docs
- Blogs at https://blog.fabric.microsoft.com/blog
- Other publicly available resources

Update the task list to reflect the completion of Phase 2.

---

### Phase 3: Plan the Work

Create a detailed outline specific to the provided subject. Present the plan to the user and **do not proceed until the user has explicitly approved**. If the user requests changes, update the outline and seek approval again.

## Blog Structure

All standalone posts (~1,140–1,285 words) should address these sections:

| Section | Purpose / What to Include |
|---------|---------------------------|
| Introduce the topic | State the feature, idea, scenario, or component the post is about. Don't use "We're excited/pleased to announce" — all blog posts are thrilled to announce something, so reduce redundancy for readers. |
| Explain why it matters | Highlight customer value, benefits, impact, or relevance. |
| Provide context | Briefly describe the challenge, direction, problem, or pattern being addressed. |
| Share the core model or idea | Give the high-level strategy, principle, or architecture. |
| Add an example or guidance | Include a practical illustration or best practices (brief and scannable). |
| Note boundaries or availability | Mention GA/Preview status, limitations, or what the solution doesn't do. |
| Close with a call to action | Guide the reader on what to do next (try it, explore docs, share feedback, etc.). |

Additional guidance:
- Tone: Explanatory, detailed, educational
- Audience: Users new to this area of the product
- Avoid: Marketing hype or pressure to adopt — focus on education and enablement
- Your blog post MUST feature at least one link to official documentation
- Links should be placed at the end of the feature, separated from the main paragraph

Update the task list to reflect the completion of Phase 3. Do not proceed to Phase 4 until the user has approved the outline.

---

### Phase 4: Write Content

Based on the approved outline, the user's requirements, and research findings, create the requested blog content. Present it to the user for review before proceeding to Phase 5.

Update the task list to reflect the completion of Phase 4.

---

### Phase 5: Apply Style Guide

Read [style-guide.md](./references/style-guide.md) and apply all guidelines. Mention what changes were made in the chat response.

Update the task list to reflect the completion of Phase 5.

---

### Phase 6: Validate and Deliver

Read [validation.md](./references/validation.md) and perform all validation checks before delivering.

Deliver based on detected environment:

**If in VS Code / Local IDE (file creation available):**
- Create and present the final content in `.docx` format suitable for direct submission to WordPress.

**If in GitHub Web Interface (no file creation):**
- Output the complete blog content as formatted Markdown text directly in the chat.
- Begin with a header: `## Blog Content (copy to Word)`
- Include all sections, formatting, and links in a format that can be easily copied into a Word document.
- Remind the user to copy the content into Word and adjust link settings (remove "en-us/").

For both environments:
- Provide a brief summary of the content
- Ask if the user would like any revisions

If revisions are requested:
- Clarify what needs to be changed
- Make the updates
- Re-validate before presenting again

Update the task list to reflect the completion of Phase 6.
