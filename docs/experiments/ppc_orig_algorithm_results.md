---
title: PPC Original Algorithm - Runtime Analysis
---

# PPC Original Algorithm - Runtime Analysis

## Summary

- **Date:** 2026-01-16
- **Run ID:** `20260116_215058_f63bf7`
- **Algorithm:** Positive Pixel Count (PPC) - Original Implementation
- **Run Type:** Group batch processing
- **Run Path:** `/slurmshare/dgutman/bdsa-workflows-slurm/output/runs/20260116_215058_f63bf7`
- **Batch:** `batch_001`

## Overview

This experiment analyzed the runtime performance of the Positive Pixel Count algorithm across 981 completed jobs. Only jobs with `State=COMPLETED` and `ExitCode=0:0` as reported by Slurm's `sacct` command were included in the analysis.

**Metric:** Wall clock time (seconds) as recorded by Slurm's `ElapsedRaw` field, converted to minutes.

## Runtime Statistics

### Overall Distribution

| Statistic | Value (minutes) |
|-----------|-----------------|
| **Total Jobs** | 981 |
| **Minimum** | 0.00 |
| **Mean** | 14.88 |
| **Median (p50)** | 8.80 |
| **90th Percentile (p90)** | 30.47 |
| **95th Percentile (p95)** | 48.93 |
| **99th Percentile (p99)** | 94.95 |
| **Maximum** | 156.42 |

### Runtime Distribution Visualization

```
elapsed_minutes sparkline (p0→p100): ▁▁▁▁▁▁▁▁▂▂▂▂▃█
```

### Runtime Distribution by Bin

| Time Range | Count | Distribution |
|------------|-------|--------------|
| 0-13.03m | 627 | ████████████████████████████ |
| 13.03-26.07m | 214 | ██████████ |
| 26.07-39.10m | 73 | ███ |
| 39.10-52.14m | 24 | █ |
| 52.14-65.17m | 14 | █ |
| 65.17-78.21m | 11 | |
| 78.21-91.24m | 4 | |
| 91.24-104.28m | 8 | |
| 104.28-117.31m | 3 | |
| 117.31-130.35m | 0 | |
| 130.35-143.38m | 2 | |
| 143.38-156.42m | 1 | |

## Key Findings

- **Most jobs complete quickly:** 64% of jobs (627/981) complete in under 13 minutes
- **Median runtime:** 8.80 minutes indicates typical jobs are quite fast
- **Long tail distribution:** While most jobs are fast, some take significantly longer (up to 156 minutes)
- **90% of jobs complete within:** 30.47 minutes
- **99% of jobs complete within:** 94.95 minutes

## Batch Details

- **Manifest:** `/slurmshare/dgutman/bdsa-workflows-slurm/output/runs/20260116_215058_f63bf7/batch_001/manifest.json`
- **Segmentation Array Job ID:** None
- **PPC Array Job ID:** None
- **PPC Jobs JSONL:** `/slurmshare/dgutman/bdsa-workflows-slurm/output/runs/20260116_215058_f63bf7/batch_001/ppc_jobs.jsonl`

## Notes

- Analysis includes only successfully completed jobs (`State=COMPLETED`, `ExitCode=0:0`)
- Runtime measured as wall clock time from Slurm's `ElapsedRaw` field
- Times converted from seconds to minutes for readability
