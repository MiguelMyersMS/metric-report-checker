---
name: docs-image
description: "Image workflow for technical documentation. Use when adding, organizing, placing, or inserting images into Microsoft Fabric documentation. Handles the full image lifecycle: suggesting where images are needed, requesting images from the user, reviewing submitted images, moving them to the correct media folder, inserting them into the document with proper syntax and alt text, and cleaning up staging files. Trigger when: user asks to add images, insert screenshots, place diagrams, organize media files, or add visuals to a document."
---

# Docs Image

Workflow for suggesting, placing, and inserting images in Microsoft Fabric technical documentation.

## Quick Reference

| Phase | Description |
|-------|-------------|
| 1 | Suggest image placement |
| 2 | Get images from user |
| 3 | Review images and update list |
| 4 | Move images to correct location |
| 5 | Insert images into document |
| 6 | Clean up staging files |

## Rules

- Only PNG format is accepted. Ignore any other format.
- All image filenames must be lowercase with words separated by hyphens (for example, `workspace-settings-panel.png`).
- Every image must be embedded with the `:::image:::` syntax — never plain markdown `![]()`.
- Every image must have alt text. See [Alt text guidelines](#alt-text-guidelines).
- The docs-writer skill is responsible for writing the alt text. This skill handles file operations only.

---

## Phase 1: Suggest image placement

- Review the provided documentation files.
- Identify sections where images would enhance understanding, such as diagrams, screenshots, or charts.
- For each section, note:
  - The type of image needed (screenshot, diagram, chart)
  - A brief description of what it should show
  - The exact location in the document where it will be placed
- Save the list as `docs-list.md` in the `.github` directory using this format:

  ```markdown
  ## Image list

  | # | File name | Type | Description | Location in document |
  |---|-----------|------|-------------|----------------------|
  | 1 | workspace-overview.png | Screenshot | Overview of the workspace settings page | After the introduction paragraph in "Configure your workspace" |
  ```

Update the task list to reflect completion of Phase 1.

---

## Phase 2: Get images from user

- Ask the user to provide images based on the suggestions from Phase 1.
- Create a staging folder named `docs-images-staging` in the root of the repository.
- Instruct the user to upload PNG images to that folder using the filenames from `docs-list.md`.

Update the task list to reflect completion of Phase 2.

---

## Phase 3: Review images and update list

Once the user has uploaded images:

- Review each image in `docs-images-staging` to understand what it shows.
- Verify each image matches its description in `docs-list.md`.
- If an image doesn't match or is missing, update `docs-list.md` and ask the user to provide a replacement.
- Note the key visual elements in each image — this information will be passed to the docs-writer skill for alt text authoring.
- Confirm with the user that all images are correct before proceeding.

Update the task list to reflect completion of Phase 3.

---

## Phase 4: Move images to correct location

For each image in `docs-images-staging`:

- Move it to `media/<document-name>/` relative to the document it belongs to.
  - Example: images for `docs/real-time-intelligence/tutorial-7-create-anomaly-detection.md` go in `docs/real-time-intelligence/media/tutorial-7-create-anomaly-detection/`
- Create the folder if it doesn't exist.
- Keep filenames lowercase with hyphens.

Update the task list to reflect completion of Phase 4.

---

## Phase 5: Insert images into document

For each image, insert it at the location specified in `docs-list.md` using this syntax:

```markdown
:::image type="content" source="./media/<document-name>/<image-name>.png" alt-text="<Alt text>.":::
```

### Alt text guidelines

Alt text is written by the calling context (docs-writer skill or user). When inserting, use the alt text provided. If none was provided:

- Start with the image type: "Screenshot of...", "Diagram showing...", "Chart illustrating..."
- Describe the key content concisely.
- End with a period.
- Do not start with "image of" or repeat the surrounding paragraph text.

Update the task list to reflect completion of Phase 5.

---

## Phase 6: Clean up

- Delete `docs-list.md` from the `.github` directory.
- Delete the `docs-images-staging` folder from the root of the repository.

Update the task list to reflect completion of Phase 6.
