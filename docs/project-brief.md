# Analytical Metric Report Checker — Project Brief

## Resource name

Analytical Metric Report Checker

## Purpose

This resource helps teams review analytical metric reports and detect whether the data is reliable, suspicious, stale, incomplete, or broken before people make decisions based on it.

The checker is designed to identify issues such as missing values, data retrieval errors, stale data, sudden spikes or drops, suspicious flatlines, cumulative metric problems, missing date buckets, and metric behavior that does not match historical trends.

## Intended users

This resource is intended for:

- Data analysts
- Product managers
- UI/UX designers reviewing dashboards
- Growth teams
- Engineering teams
- Leadership teams
- Anyone responsible for interpreting metrics or reporting business performance

## Main problem it solves

Teams often review dashboards and reports assuming the data is correct. However, analytical reports can show misleading information when data pipelines fail, queries return partial results, tracking changes, metric definitions shift, or report values are stale.

This checker helps reviewers identify whether a metric can be trusted before acting on it.

## What the agent should check

The agent should review each requested metric for:

- Blank, null, empty, or missing values
- Data retrieval errors
- Stale data or missed refresh windows
- Unexpected zeros
- Sudden increases or decreases
- Suspiciously flat values
- Cumulative metrics that decrease unexpectedly
- Summed metrics with missing underlying dates
- Metrics that behave differently from historical trends
- Ratios or percentages outside valid ranges
- Related metrics that no longer move together as expected
- Anomalies that may be explained by recent backend, tracking, product, or business changes

## What the agent should produce

For each reviewed metric, the agent should produce:

- Metric name
- Current value
- Previous comparison value
- Expected range or baseline
- Status
- Severity
- Confidence level
- Explanation
- Evidence
- Likely cause
- Recommended next action
- Whether someone should be alerted

## Status categories

The checker should classify each metric as one of the following:

| Status | Meaning |
|---|---|
| Healthy | The metric appears reliable and within expected behavior. |
| Warning | The metric is unusual but not clearly broken. |
| Critical | The metric appears broken, missing, stale, or highly suspicious. |
| Expected anomaly | The metric looks unusual but appears explainable by known context. |
| Needs review | The checker does not have enough information to confidently classify the metric. |

## Sharing goal

This project should become a reusable resource that others can copy, adapt, and apply to their own dashboards, reports, or metric review workflows.

The resource should be easy to understand, easy to modify, and useful even for teams that do not yet have a formal data-quality monitoring system.
