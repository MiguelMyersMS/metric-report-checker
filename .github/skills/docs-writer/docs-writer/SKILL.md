---
name: docs-writer
description: "Full end-to-end technical documentation writing workflow for Microsoft Fabric docs. Use when writing, drafting, editing, or creating documentation such as how-to guides, tutorials, conceptual articles, quickstarts, or overviews. Covers all phases: gathering requirements, researching features via Microsoft Learn and existing docs, planning an approved outline, selecting the right template, writing content in Microsoft style, inserting images with alt text, validating links and TOC, and opening a pull request. Trigger when: user asks to write docs, create documentation, draft a how-to guide, tutorial, conceptual article, quickstart, overview, update existing docs, add a new article, or document a feature."
---

# Docs Writer

End-to-end workflow for writing and editing Microsoft Fabric technical documentation.

## Quick Reference

| Phase | Description | Reference |
|-------|-------------|-----------|
| 1 | Gather requirements | [Below](#phase-1-gather-requirements) |
| 2 | Research | [Below](#phase-2-research) |
| 3 | Plan & outline | [Below](#phase-3-plan-the-work) |
| 4 | Write or edit | [Microsoft Learn templates](https://learn.microsoft.com/en-us/help/patterns/level4/) |
| 5 | Apply style guide | [STYLE-GUIDE.md](./references/STYLE-GUIDE.md) |
| 5.5 | Validate | [VALIDATION.md](./references/VALIDATION.md) |
| 6 | Open pull request | [Below](#phase-6-open-pull-request) |

## Task Tracking

Use the task tracking tool to create and manage a task list at the start of the session. Create all phase todos upfront, mark them in-progress as you work on each phase, and mark them completed when done. Do NOT create task lists in the chat — always use the task tracking tool so the task list appears above the chat input.

---

## Phase 1: Gather Requirements

Ask the following questions **one at a time**, waiting for an answer before asking the next:

1. Do you want to create a new document or edit an existing one?
2. What is the feature or subject the documentation covers?
3. Do you have specifications, related documentation, or other reference content? (Paste into chat or share a link.)
4. If no specifications exist: can you describe the feature and the necessary elements to cover?
5. (New docs only) Which document type do you want?
   - **How-to**: Goal-oriented, task-based steps
   - **Tutorial**: Learning-oriented, end-to-end scenario
   - **Conceptual**: Understanding-oriented, explains why/how something works
   - **Quickstart**: Time-bounded, get-started experience (< 10 minutes)
   - **Overview**: High-level introduction to a feature area
6. Are there existing documents in the repo that are ideal examples of this type?
7. Where should the document be placed in the repository?

Update the task list to reflect completion of Phase 1.

---

## Phase 2: Research

Gather comprehensive context before writing. Do NOT write content, create files, or pause for user feedback during this phase.

Use these sources in order of preference:
1. Specifications or content provided by the user
2. Existing documentation within the repository (search for related files)
3. Microsoft Docs / Microsoft Learn — use the `microsoft_docs_search` MCP tool to search, and `microsoft_docs_fetch` to retrieve full page content when needed
4. [Microsoft Fabric blog](https://blog.fabric.microsoft.com/blog)
5. Other publicly available Microsoft resources

Capture:
- Feature name, description, and current GA/Preview status
- Related features and how they connect
- Existing articles that should be linked or cross-referenced
- Any images, diagrams, or screenshots referenced in existing docs

Update the task list to reflect completion of Phase 2.

---

## Phase 3: Plan the Work

Create a detailed work plan including:

- **Document title** (sentence-style capitalization)
- **Document type** and the appropriate template from [Microsoft Learn templates](https://learn.microsoft.com/en-us/help/patterns/level4/)
- **Outline**: all major H2 and H3 headings with a one-line summary of each section
- **TOC file** that needs updating (path relative to the document)
- **Related documents** to link to (3–5 internal links)
- **Images needed**: list any screenshots, diagrams, or charts with a brief description of each

Present the plan to the user. **Do not proceed until the user has explicitly approved.** If changes are requested, update the plan and seek approval again.

Update the task list to reflect completion of Phase 3.

---

## Phase 4: Write or Edit the Document

### Branch management

- Check out a new working branch from `main`
- Use a descriptive branch name (for example, `add-feature-overview`, `update-quickstart-guide`)

### Writing the document

- Fetch the template for the selected document type from [Microsoft Learn templates](https://learn.microsoft.com/en-us/help/patterns/level4/) using the `microsoft_docs_fetch` MCP tool or web fetch. Retrieve the specific template page for the chosen document type (how-to, tutorial, conceptual, quickstart, or overview).
- Follow the approved outline exactly — do not add sections beyond those in the template
- Follow the voice, tone, and structure rules in [STYLE-GUIDE.md](./references/STYLE-GUIDE.md)

### Images

When the user needs images added to the document, load and follow `.github/skills/docs-image/SKILL.md` for the full image workflow. You are responsible for writing the alt text for each image based on the image content and where it's referenced in the document. The image skill handles all file operations.

- Reference each image using this syntax:

  ```markdown
  :::image type="content" source="./media/document-name/image-name.png" alt-text="Alt text description.":::
  ```

- Alt text guidelines:
  - State the image type first: "Screenshot of...", "Diagram showing...", "Chart illustrating..."
  - Describe the key content concisely
  - End with a period
  - Do not repeat the surrounding text verbatim

- Place image files under `media/<document-name>/` relative to the document

### TOC update (critical)

If creating a new document, you **must** update the relevant `toc.yml` file:

```yaml
- name: Your Document Title
  href: your-file-name.md
```

Place the entry in a logical location within the TOC hierarchy.

After completing the draft, present it to the user for review before proceeding to Phase 5.

Update the task list to reflect completion of Phase 4.

---

## Phase 5: Apply Style Guide

Read [STYLE-GUIDE.md](./references/STYLE-GUIDE.md) and apply all guidelines to the document. Report what you changed in the chat response.

After applying STYLE-GUIDE.md, fetch and review relevant sections from the full [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/) using the `microsoft_docs_fetch` MCP tool or web fetch. Focus on sections relevant to the document type and content. Apply any additional rules found. Report what changes were made from the full style guide.

Update the task list to reflect completion of Phase 5.

---

## Phase 5.5: Validate

Read [VALIDATION.md](./references/VALIDATION.md) and run all checks. Fix any issues found before proceeding.

Update the task list to reflect completion of Phase 5.5.

---

## Phase 6: Open Pull Request

### Commit changes

- Stage all modified files (document, TOC, images)
- Write a descriptive commit message explaining the changes

### Create the PR

- Create a PR from your branch against the `main` branch
- Use a clear PR title (for example, `Add access control overview documentation`)
- Include in the PR description:
  - **Summary**: What was added or changed
  - **Document type**: Conceptual, how-to, tutorial, etc.
  - **Key topics covered**: Bulleted list
  - **Related issues**: Link any related GitHub issues
  - **Standards**: Note that it follows Microsoft style guide

### Confirm delivery

- Provide the PR URL
- Confirm all files are included
- Note any follow-up actions needed

Update the task list to reflect completion of Phase 6.
