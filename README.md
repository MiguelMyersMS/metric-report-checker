# Analytical Metric Report Checker

A reusable resource for reviewing analytical metric reports and identifying whether metrics are reliable, suspicious, stale, incomplete, or broken before teams make decisions based on them.

## What this resource does

The Analytical Metric Report Checker helps teams detect issues such as:

- Blank, null, or missing metric values
- Data retrieval errors
- Stale or delayed data
- Unexpected zeros
- Sudden spikes or drops
- Suspicious flatlines
- Cumulative metrics that decrease unexpectedly
- Summed metrics with missing underlying dates
- Metrics that behave differently from historical trends
- Ratios or percentages outside valid ranges
- Anomalies that may be explained by recent backend, tracking, product, or business changes

## Who this is for

This resource is useful for:

- Data analysts
- Product managers
- UI/UX designers reviewing dashboards
- Growth teams
- Engineering teams
- Leadership teams
- Anyone responsible for interpreting metrics or reporting business performance

## Project structure

```text
metric-report-checker/
  README.md
  .github/
    copilot-instructions.md
    prompts/
      metric-report-checker.prompt.md
  templates/
    metric-registry-template.yaml
    anomaly-report-template.md
  examples/
    sample-metrics.csv
    sample-output.md
  docs/
    project-brief.md
```

## How to use this resource

1. Define the metrics that matter using the metric registry template.
2. Use the metric checker prompt to review a dashboard, report, CSV, exported data, or metric summary.
3. Classify each metric as Healthy, Warning, Critical, Expected anomaly, or Needs review.
4. Document the findings using the anomaly report template.
5. Improve the rules over time based on confirmed false positives, expected changes, and team feedback.

## Status categories

| Status | Meaning |
|---|---|
| Healthy | The metric appears reliable and within expected behavior. |
| Warning | The metric is unusual but not clearly broken. |
| Critical | The metric appears broken, missing, stale, or highly suspicious. |
| Expected anomaly | The metric looks unusual but appears explainable by known context. |
| Needs review | There is not enough information to confidently classify the metric. |

## Current status

This project is in early development.

The first version includes:

- Project brief
- Metric registry template
- Anomaly report template
- GitHub Copilot instructions
- Reusable metric checker prompt
- Example input and output files

## License

MIT License
