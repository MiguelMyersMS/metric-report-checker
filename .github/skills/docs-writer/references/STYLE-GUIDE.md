# Microsoft Documentation Style Guide

Condensed reference for Microsoft Fabric technical docs. Full guidance at [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/).

---

## Voice and Tone

| Rule | Do | Don't |
|------|----|-------|
| Use second person | "You configure the network." | "The network is configured." |
| Use active voice | "Select **Save**." | "**Save** should be selected." |
| Use present tense | "This feature lets you..." | "This feature will let you..." |
| Use contractions | "It's", "don't", "you're" | "It is", "do not" (except error messages) |
| Be concise | "Configure the setting." | "You can configure the setting." |

### Avoid these words

Remove marketing and filler language:

- cutting-edge, state-of-the-art, industry-leading, revolutionary, unparalleled
- streamline, leverage, robust, powerful, seamlessly
- simply, easily, just, quickly (unless it's genuinely quick)
- "In order to" → use "To"
- "Utilize" → use "Use"
- "Extract" → use "Remove" or "Get"
- "e.g." → use "for example"
- "i.e." → use "that is"

---

## Capitalization

- **Sentence-style** for headings, TOC entries, UI labels, table headers: capitalize only the first word and proper nouns.
- **Title-style** only for product/service names and formal titles (Microsoft Fabric, Azure Data Factory).
- Do not use ALL CAPS for emphasis.

---

## Sentence and Paragraph Length

- Aim for 15–20 words per sentence maximum.
- Keep paragraphs to 1–3 sentences.
- Front-load the key information — put the most important point first.

---

## Punctuation

- Use the **Oxford comma**: "tables, views, and functions"
- One space after a period.
- Use colons to introduce lists.
- Avoid semicolons — rewrite as two sentences or a list.
- Do not use slashes for alternatives: use "or" instead.

---

## Numbers

- Spell out zero through nine; use numerals for 10 and above.
- Always use numerals for measurements, percentages, time, and technical values.
- Use commas in numbers with four or more digits: 1,000; 10,000.

---

## Acronyms and Abbreviations

- Spell out on first use with the acronym in parentheses: "real-time intelligence (RTI)".
- Don't spell out if the acronym is widely known to the audience (SQL, API, UI).
- Use "a" or "an" based on pronunciation: "an ISP", "a SQL database".

---

## UI References

- Bold UI element names in procedures: Select **Save**, open the **Settings** page.
- Use **select** not "click" or "tap" (input-neutral).
- Use **open** not "launch".
- Use **enter** not "type".
- Provide context for where the action occurs: "On the **Design** tab, select **New column**."

---

## Lists

| Type | When to use |
|------|-------------|
| Numbered | Sequential steps, ranked items |
| Bulleted | Unordered items, feature lists, options |

- Keep lists to 2–7 items; break longer lists into subsections.
- Keep list items parallel in structure.
- Capitalize the first word of each item.
- Use periods only if items are complete sentences.

---

## Procedures (Step-by-step)

- No more than seven steps per procedure; break longer tasks into sub-procedures.
- Use imperative verbs: Select, Enter, Open, Clear.
- One action per step.
- Include navigation context when needed: "In the left pane, select **Workspaces**."

---

## Headings

- Use sentence-style capitalization.
- Keep headings short — ideally one line.
- Add a heading every 3–5 paragraphs to aid scanning.
- Front-load keywords in headings.
- Don't skip heading levels (H2 → H4).

---

## Images

- Use images to clarify complex concepts, not for decoration.
- All images require descriptive alt text.
- Alt text format: `"Screenshot of the workspace settings page showing the Manage access panel."` — State the image type, describe the content, end with a period.
- Embed images using:

  ```markdown
  :::image type="content" source="./media/<document-name>/<image-name>.png" alt-text="<Alt text>.":::
  ```

---

## Links

- Use descriptive link text that describes the destination: `[Create a workspace](how-to-create-workspace.md)` not `[click here]`.
- Use relative paths for internal links.
- Verify all links are accessible before submitting.

---

## Tables

- Use tables when comparing two or more attributes.
- Include a header row with specific column labels.
- Use sentence-style capitalization in headers and cells.
- Keep cell content brief — ideally one line per cell.
- Keep column entries parallel.

---

## Accessibility and Inclusivity

- Use gender-neutral language; use "they" as a singular pronoun.
- Avoid idioms, humor, and cultural references that won't translate globally.
- Use plain, inclusive language.
