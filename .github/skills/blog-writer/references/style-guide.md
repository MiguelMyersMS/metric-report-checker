# Blog Style Guide

Apply all guidelines below when reviewing blog content in Phase 5.

---

## Content Guidelines

- Be concise. Do not restate information in more than one place.
- Follow [Microsoft documentation style guidelines](https://learn.microsoft.com/style-guide/welcome/).
- Use [tone and voice guidance](https://learn.microsoft.com/style-guide/top-10-tips-style-voice).
- Follow [accessibility guidelines](https://learn.microsoft.com/writing-style-guide-msft-internal/accessibility/accessibility-guidelines-requirements).
- **Use plain, inclusive language** — avoid gender-specific terms, use neutral examples.
- **Use present tense** — "This feature lets you..." not "This feature will let you..."
- **Be conversational but professional** — use contractions (it's, you're, don't) for friendliness.
- **Avoid marketing language** — no hype, flowery language, or product advertisements. Language should be neutral, functional and instructional.

---

## Terminology Requirements

| Use | Instead of |
|-----|------------|
| item | artifact |
| SQL analytics endpoint | SQL endpoint |
| OneLake | Onelake |
| Pipelines | Data pipelines |
| SharePoint | Sharepoint |

---

## Input-Agnostic Verbs

Customers use keyboards, mice, touch, voice, and more. Use verbs that work for any input method.

- **Use**: select, choose, open, go to
- **Avoid**: click, swipe, tap, press

---

## Formatting Guidelines

- Use **bullets** for lists (avoid letters or numbers unless indicating a sequence).
- Use **bold text** for emphasis and UI labels — do not use quotes.

---

## Words to Avoid

The following marketing words must be removed:

- "cutting-edge", "state-of-the-art", "industry-leading"
- "unparalleled", "revolutionary", "game-changing"
- "streamline", "leverage", "robust"
- "powerful", "innovative", "seamless"

**Examples:**
- ❌ "This revolutionary feature lets you leverage cutting-edge technology"
- ✅ "This feature lets you control access with role-based permissions"

- **Avoid idioms and clichés** — write for a global audience.
- **Avoid pressure tactics** — don't use "Try it now!", "Don't miss out!", "Get started today!"
  - ✅ Acceptable: "Learn more", "See documentation", "Explore the feature"

---

## Accessibility Guidelines

### Link Accessibility

Links should make sense without the surrounding text, so be descriptive. Don't just list URLs at the end of a sentence. It's always an option to simply use the title of the page you're linking to. For example, "To learn more, refer to our documentation [hyperlink title of page]."

AVOID 'docs', 'here', 'below', 'read', 'blog', 'see below', 'click here', which are not accessible for people using screen readers.

**Examples:**
- ✅ "Learn more about reading and ingesting JSONL files in the [Query and ingest JSONL files in Data Warehouse and SQL Analytics Endpoint for Lakehouse](https://...) blog post."
- ✅ "Refer to the [Add MongoDB CDC source to an eventstream](https://...) documentation."
- ✅ "Refer to the [Maximize editing space with focus mode](https://...) documentation to learn more."

### Images and Media

- All images, screenshots, and tables must include both a **caption** and **alt text**.
- **Caption**: Visible label describing what the image shows. Keep it short and meaningful.
- **Alt text**: Screen-reader description of the image's meaning/purpose. 1–2 sentences. Do not start with "image of…"
- Screenshots should be clear, zoomed in to the area being referenced, and easy to view. Use red boxes to highlight the area.
- GIFs must have a written description in the blog body.

## Next Steps Section

Include a Next Steps section at the end of your blog post to give the reader the next steps to follow. Options to consider:
- Learn More
- Sign up
- Submit ideas
- Provide feedback

---

## Titling Sequence

If applicable, use this sequence:
- `Your blog post title (Preview)`
- `Your blog post title (Generally Available)`

Do not specify "Public" — only public previews are released. Always place the status at the end of the title.

---

## Headings

- **H1** — Reserved for the blog post title only
- **H2** — Section headers (e.g., Fabric Platform, Databases, OneLake)

---

## Link Settings

Ensure your Learn, docs, or blog post links are accessible. In your Word doc and in WordPress, adjust the settings of your links to ensure they:
- Exclude location info (e.g., delete "en-us/")
- Do not link to MSIT or other internal pre-production environments

Add your link to the end of the feature. For features that don't include an image, the link should also be separated from the main paragraph and at the end of the feature.

---

## Your blog post MUST include at least one link to official documentation.

---

## Categories and Tags

Include at least one category and 3–5 meaningful tags at the end of the post. Tags and categories are important for SEO.

### Available Fabric Categories
AI, Announcements, Apache Iceberg, Apache Spark, Community, Community Challenge, Data Engineering, Data Factory, Data Lake, Data Science, Data Warehouse, Databases, Fabric platform, Fabric Public APIs, Lakehouse, Microsoft Fabric, Monthly Update, OneLake, Real-Time Intelligence, Roadmap

### Available Power BI Categories
Admin, AI, Analysis Services, Announcements, API, Archive, Copilot, Customer Stories, Data loss prevention, DAX, Developers, Direct Lake, Features, Information Protection, Metrics, Paginated Reports, Power BI, Power BI Embedded, Power BI Mobile, Report Server, Semantic model, Support, Template apps, Web Modeling

### Tag Guidance
- Use existing tags whenever possible
- Choose tags that accurately represent the content
- Avoid repeating the title in tags
- Use 3–5 meaningful tags (not too broad or too specific)
- Avoid internal codenames or team-specific jargon
- Create a new tag only if needed for multiple future posts
