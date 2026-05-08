# metric-report-checker

An intelligent agent/skill that reviews analytical metric reports at the moment they are requested and determines whether each key metric is trustworthy, suspicious, broken, stale, or behaving as expected.

## What It Does

- Evaluates metric health across analytical reports at request time
- Classifies each metric as: **trustworthy**, **suspicious**, **broken**, **stale**, or **expected**
- Built on GitHub Copilot agents, skills, and MCP server integrations
- Designed for PM workflows in Azure DevOps + Power BI environments

## Architecture

| Folder | Purpose |
|--------|---------|
| `brain/` | AI context, project routing rules, and project definitions |
| `.github/agents/` | Custom Copilot agents for specialized roles |
| `.github/skills/` | On-demand workflow skills with templates |
| `.github/prompts/` | Quick-task prompt templates |
| `.github/instructions/` | File-specific guidance for agents |
| `data/` | Tracked follow-ups, action items, metrics |

## Getting Started

1. Clone the repo
2. Open in VS Code with GitHub Copilot enabled
3. Configure MCP servers in `.vscode/mcp.json` for your environment
4. Use `/daily-review` or other prompt templates to trigger workflows

## Requirements

- VS Code with GitHub Copilot (agent mode)
- Azure DevOps MCP server access
- Power BI / Fabric MCP server access (optional)

## License

[MIT](LICENSE)
