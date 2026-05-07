# My Projects

## PM Operations (this workspace)

| Project | Path | What It Is | Key Tech |
|---------|------|-----------|----------|
| My-Ops-Hub | `C:\Users\miguelmyers\My-Ops-Hub` | Personal PM command center — brain, agents, skills, prompts | Copilot agents, MCP, Skills |
| Databases Strategy Metrics | `brain/projects/databases-strategy/` | Executive scorecard for DB strategy execution (SQL, Postgres, NoSQL, Fabric) | Power BI, ADO Feature #2079452 |
| LT Reliability Metrics | `brain/projects/lt-reliability-metrics/` | Cross-product reliability dashboard for Arun's LT (DW first, then Pipeline/Spark) | Power BI, ADO Feature #2087007, IcM-767077695 |
| PLG Key Metrics Dashboard | `brain/projects/plg-key-metrics/` | Growth dashboard with key metrics across 7 PLG priority areas (Acq Channels, TTV, Pro Dev, Trials, Expansion, Ecosystem, Partners) | Power BI, ADO Feature #2069070 |

## Report Development & Design System (satellite projects)

| Project | Path | What It Is | Key Tech |
|---------|------|-----------|----------|
| Bloodwork Dashboard | `C:\Users\miguelmyers\Documents\Projects\bloodwork-dashboard-prototype` | Personal prototype — design system lab for data visualization patterns and tokens | React 18, D3, Vite, Express, Fabric SQL |
| Lyra App (v1) | `C:\Users\miguelmyers\projects\lyra-app\my-lyra-app` | Lyra private preview — React app visualizing PBI semantic model via DAX + Vega-Lite | React 19, Vite, Tailwind, @powerbi/lyra-* |
| Lyra App (v2) | `C:\Users\miguelmyers\projects\lyra-app\my-lyra-app-v2` | Fabric Apps template — next-gen reporting surface using fabric.yaml + Vega-Lite | React 19, Vite, Tailwind, @microsoft/fabric-* |
| Customer 360 (PBIP) | `C:\Users\miguelmyers\projects\Customer 360` | Power BI report in PBIP format — exploring natural-language PBIP editing | Power BI PBIP, PBI MCP |

## How They Connect

```
Bloodwork Dashboard ──tokens, components, patterns──▶ Lyra App v2
       (design system lab)                              (Fabric Apps reporting)
                                                              │
                                                    connects to team's
                                                    semantic models
                                                              │
Customer 360 (PBIP) ◀── optimize current PBI workflow ──── while Lyra matures
       (natural-lang PBI editing)

All tracked in: My-Ops-Hub (brain/, data/, ADO)
```

**Transition plan:** Build design system + Vega-Lite gallery in bloodwork/lyra now. When Lyra reaches GA (timeline TBD, Chris Hamill → Nate decision path, Arun already bought in), shift team reporting from Power BI → Fabric Apps. Meanwhile, optimize current PBI workflow via PBIP natural-language editing.

## Conventions

- **Branch naming:** `<type>/<description>` (e.g., `feature/add-revenue-measure`)
- **Commit messages:** `<type>: <description>` (e.g., `feat: add monthly revenue measure`)
- **Types:** `feat`, `fix`, `docs`, `refactor`, `chore`, `test`
