# Metric Report Review

## Executive summary

The report appears partially reliable. Several metrics loaded successfully, but multiple values require review before they should be used for decision-making.

The most important issues are:

- Weekly Active Users dropped sharply, but the drop appears related to incomplete data coverage.
- Total Accounts decreased even though it is marked as a cumulative metric.
- Monthly Revenue appears incomplete because only 64% of expected data is present.
- NPS Score appears stale because the latest data timestamp is one week old.
- Signup Conversion Rate dropped sharply, but recent backend migration context may explain the change.

## Overall status

Critical

## Key findings

| Metric | Current value | Baseline / expected range | Status | Severity | Confidence | Finding |
|---|---:|---:|---|---|---:|---|
| Weekly Active Users | 84,200 | ~124,500 trailing 7-day median | Critical | High | 92% | Sharp drop with incomplete data coverage. |
| Signup Conversion Rate | 2.1% | ~4.6% trailing 7-day median | Expected anomaly | Medium | 74% | Large decrease may be explained by recent backend migration. |
| Total Accounts | 981,200 | Previous value: 982,100 | Critical | High | 95% | Cumulative metric decreased unexpectedly. |
| Support Tickets | 318 | ~305 trailing 7-day median | Healthy | Low | 88% | Value appears within normal variation. |
| Monthly Revenue | 548,000 | ~805,000 trailing 7-day median | Critical | High | 94% | Revenue total is likely incomplete due to missing date buckets. |
| NPS Score | 41 | ~41 trailing 7-day median | Warning | Medium | 86% | Value appears stale because data has not refreshed this week. |

## Detailed findings

### Weekly Active Users

**Status:** Critical  
**Severity:** High  
**Confidence:** 92%

**Current value:** 84,200  
**Baseline or expected range:** ~124,500 trailing 7-day median  
**Percent change:** -32.4% versus trailing 7-day median  
**Robust z-score, if available:** Not available from sample data  
**Data freshness:** Expected May 8, latest data May 7  
**Data completeness:** 72%

**What was detected:**  
Weekly Active Users dropped sharply compared with the recent historical baseline.

**Evidence:**  
Current value is 84,200 compared with a trailing 7-day median of 124,500. Data completeness is only 72%, and notes indicate missing data for May 6 and May 7.

**Likely cause:**  
Incomplete data retrieval or missing date buckets, rather than a confirmed business decline.

**Context considered:**  
Sample notes mention missing data for May 6 and May 7.

**Recommended action:**  
Check ingestion or dashboard query coverage before treating this as a true user activity decline.

**Should alert someone?** Yes

### Signup Conversion Rate

**Status:** Expected anomaly  
**Severity:** Medium  
**Confidence:** 74%

**Current value:** 2.1%  
**Baseline or expected range:** ~4.6% trailing 7-day median  
**Percent change:** -54.3% versus trailing 7-day median  
**Robust z-score, if available:** Not available from sample data  
**Data freshness:** Fresh  
**Data completeness:** 100%

**What was detected:**  
Signup Conversion Rate dropped sharply compared with recent historical values.

**Evidence:**  
Current value is 2.1% compared with a trailing 7-day median of 4.6%.

**Likely cause:**  
Recent signup backend migration may explain the drop.

**Context considered:**  
Sample notes mention a signup backend migration started May 7.

**Recommended action:**  
Confirm whether the backend migration changed tracking, denominator logic, or conversion event definitions.

**Should alert someone?** No, unless the change was not expected.

### Total Accounts

**Status:** Critical  
**Severity:** High  
**Confidence:** 95%

**Current value:** 981,200  
**Baseline or expected range:** Previous value: 982,100  
**Percent change:** -0.09% versus previous value  
**Robust z-score, if available:** Not available from sample data  
**Data freshness:** Fresh  
**Data completeness:** 100%

**What was detected:**  
Total Accounts is marked as cumulative, but the value decreased.

**Evidence:**  
Previous value was 982,100. Current value is 981,200. A cumulative metric should generally not decrease unless it has a known reset, deletion logic, backfill correction, or definition change.

**Likely cause:**  
Possible data correction, deletion logic, source mismatch, tracking change, or query issue.

**Context considered:**  
No explanatory context was provided in the sample data.

**Recommended action:**  
Confirm whether account deletions, deduplication, backfill correction, or a metric definition change occurred.

**Should alert someone?** Yes

### Support Tickets

**Status:** Healthy  
**Severity:** Low  
**Confidence:** 88%

**Current value:** 318  
**Baseline or expected range:** ~305 trailing 7-day median  
**Percent change:** +4.3% versus trailing 7-day median  
**Robust z-score, if available:** Not available from sample data  
**Data freshness:** Fresh  
**Data completeness:** 100%

**What was detected:**  
No major issue detected.

**Evidence:**  
Current value is close to previous and historical comparison values.

**Likely cause:**  
Normal daily variation.

**Context considered:**  
Sample notes indicate normal daily variation.

**Recommended action:**  
No action needed.

**Should alert someone?** No

### Monthly Revenue

**Status:** Critical  
**Severity:** High  
**Confidence:** 94%

**Current value:** 548,000  
**Baseline or expected range:** ~805,000 trailing 7-day median  
**Percent change:** -31.9% versus trailing 7-day median  
**Robust z-score, if available:** Not available from sample data  
**Data freshness:** Fresh  
**Data completeness:** 64%

**What was detected:**  
Monthly Revenue is substantially below the recent baseline and appears incomplete.

**Evidence:**  
Current value is 548,000 compared with a trailing 7-day median of 805,000. Data completeness is only 64%, and notes indicate missing several daily revenue buckets.

**Likely cause:**  
Missing date buckets or incomplete aggregation.

**Context considered:**  
Sample notes mention missing daily revenue buckets.

**Recommended action:**  
Validate the underlying daily revenue data before sharing the monthly revenue number.

**Should alert someone?** Yes

### NPS Score

**Status:** Warning  
**Severity:** Medium  
**Confidence:** 86%

**Current value:** 41  
**Baseline or expected range:** ~41 trailing 7-day median  
**Percent change:** 0% versus trailing 7-day median  
**Robust z-score, if available:** Not available from sample data  
**Data freshness:** Latest data May 1, expected May 8  
**Data completeness:** 100%

**What was detected:**  
The value appears stable, but the latest data timestamp suggests the metric may be stale.

**Evidence:**  
Current value has remained at 41, but the latest data timestamp is May 1 while the expected refresh timestamp is May 8.

**Likely cause:**  
The metric may not have refreshed this week.

**Context considered:**  
No additional context was provided.

**Recommended action:**  
Confirm the NPS pipeline or survey export refresh schedule.

**Should alert someone?** Yes, if this metric is expected to refresh weekly or daily.

## Unknowns and assumptions

- Robust z-score could not be calculated because the sample file only includes summary baselines, not full historical values.
- Expected ranges are inferred from trailing medians.
- The signup conversion anomaly is treated as expected only because migration context is provided.
- Cumulative metric behavior assumes Total Accounts should not decrease unless a reset, correction, deletion, or definition change occurred.

## Recommended next steps

1. Investigate incomplete data for Weekly Active Users and Monthly Revenue.
2. Confirm why Total Accounts decreased.
3. Confirm whether the signup backend migration changed metric definitions or event tracking.
4. Verify the NPS Score refresh schedule.
5. Add more historical values to support robust z-score and seasonality-aware checks.