# Validation Checklist

Run all checks before opening a pull request. Fix any issues found before proceeding.

---

## Technical validation

### Links

- [ ] All internal links use relative paths (not absolute URLs)
- [ ] All linked files exist in the repository
- [ ] All external links use `https://` and are accessible
- [ ] No broken anchor links (`#section-id` fragments)

### Images

- [ ] All images are in the correct `media/<document-name>/` folder
- [ ] All image filenames are lowercase with hyphens (no spaces, no camelCase)
- [ ] All images are referenced with the correct `:::image:::` syntax
- [ ] Every image has meaningful, non-empty alt text

### Markdown

- [ ] No broken markdown syntax (unclosed bold, italic, code fences)
- [ ] Code blocks include the language identifier (` ```json `, ` ```kusto `, etc.)
- [ ] Tables are properly formatted with header rows

### TOC

- [ ] New documents are added to the relevant `toc.yml` file
- [ ] The `href` path in `toc.yml` is correct relative to the TOC file
- [ ] The TOC entry uses sentence-style capitalization

### Metadata (front matter)

- [ ] `title` is present and uses sentence-style capitalization
- [ ] `description` is 100–160 characters and summarizes the document
- [ ] `ms.topic` is set to the correct value (`how-to`, `tutorial`, `conceptual`, `quickstart`, or `overview`)
- [ ] `ms.date` reflects today's date

---

## Content validation

### Structure

- [ ] Document follows the correct template for its type (see [TEMPLATES.md](./TEMPLATES.md))
- [ ] All H2 and H3 headings match the approved outline
- [ ] No sections were added beyond those in the template without approval
- [ ] The opening paragraph answers: what does this cover and what does the reader get?

### Related content

- [ ] 3–5 related links are included in the Related content section
- [ ] Related links point to real, accessible files
- [ ] Link text is descriptive (not "click here" or "this article")

### Code and commands

- [ ] All code samples are syntactically correct
- [ ] Code blocks use the correct language identifier for syntax highlighting
- [ ] Commands and paths use the correct casing for the target platform

---

## Style validation

### Voice and tone

- [ ] Written in second person ("you/your")
- [ ] Active voice throughout (flag passive constructions)
- [ ] Present tense (`lets you`, not `will let you`)
- [ ] No marketing language: cutting-edge, robust, seamlessly, leverage, streamline, etc.

### Capitalization

- [ ] All headings use sentence-style capitalization
- [ ] Product and service names are correctly capitalized (Microsoft Fabric, Azure)
- [ ] No ALL CAPS used for emphasis

### Acronyms

- [ ] All acronyms are spelled out on first use with the acronym in parentheses
- [ ] No undefined acronyms for the target audience

### Word choice

- [ ] "Select" used instead of "click" or "tap"
- [ ] "Enter" used instead of "type"
- [ ] "Open" used instead of "launch"
- [ ] "Use" used instead of "utilize"
- [ ] "For example" used instead of "e.g."
- [ ] "That is" used instead of "i.e."
- [ ] Oxford comma used in all series

### Images and alt text

- [ ] Every image has alt text that starts with the image type: "Screenshot of...", "Diagram showing...", "Chart illustrating..."
- [ ] Alt text ends with a period
- [ ] Alt text describes the image content, not what the image is for

---

## Pre-submit checklist

Before creating the pull request, confirm:

- [ ] Document draft reviewed and approved by user
- [ ] All style guide changes applied and reported
- [ ] All validation items above checked and resolved
- [ ] Branch is up to date with `main`
- [ ] Commit message is descriptive
