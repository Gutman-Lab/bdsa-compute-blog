# Experiment JSON Format Guide

This document describes the JSON format that experiment report generating scripts should output for automatic integration into the BDSA Compute Blog.

## Required JSON Schema

Your scripts should output a JSON file named `metrics.json` with the following structure:

```json
{
  "run_id": "20260116_215058_f63bf7",
  "date": "2026-01-16",
  "dataset": "TCGA-SKCM",
  "model": "PPC-Original",
  "metrics": {
    "total_jobs": 981,
    "min_runtime_minutes": 0.00,
    "mean_runtime_minutes": 14.88,
    "median_runtime_minutes": 8.80,
    "p90_runtime_minutes": 30.47,
    "p95_runtime_minutes": 48.93,
    "p99_runtime_minutes": 94.95,
    "max_runtime_minutes": 156.42
  },
  "runtime_minutes": 14.88,
  "git_commit": "a1b2c3d",
  "config": {
    "algorithm": "PPC",
    "batch": "batch_001",
    "run_path": "/slurmshare/dgutman/bdsa-workflows-slurm/output/runs/20260116_215058_f63bf7"
  }
}
```

## Field Descriptions

### Required Fields

- **`run_id`** (string): Unique identifier for this experiment run (e.g., timestamp-based ID)
- **`date`** (string): Date in ISO format (YYYY-MM-DD)
- **`dataset`** (string): Name of the dataset used
- **`model`** (string): Algorithm/model name or version
- **`metrics`** (object): Key performance metrics (see below)

### Optional Fields

- **`runtime_minutes`** (number): Overall runtime for the experiment
- **`git_commit`** (string): Git commit hash for reproducibility
- **`config`** (object): Configuration parameters used
- **`slurm_job_id`** (string): SLURM job identifier
- **`gpu_info`** (object): GPU resource information
- **`resource_usage`** (object): CPU/memory usage statistics

## Metrics Object

The `metrics` object can contain any key-value pairs. Common examples:

- Runtime statistics: `min_runtime_minutes`, `mean_runtime_minutes`, `median_runtime_minutes`, `max_runtime_minutes`
- Percentiles: `p50_runtime_minutes`, `p90_runtime_minutes`, `p95_runtime_minutes`, `p99_runtime_minutes`
- Counts: `total_jobs`, `completed_jobs`, `failed_jobs`
- Performance metrics: `throughput`, `images_per_hour`, `pixels_processed`
- Accuracy metrics: `auc`, `f1`, `precision`, `recall`

## Example: Runtime Analysis Report

For runtime/performance analysis reports, use this structure:

```json
{
  "run_id": "20260116_215058_f63bf7",
  "date": "2026-01-16",
  "dataset": "batch_001",
  "model": "PPC-Original",
  "metrics": {
    "total_jobs": 981,
    "completed_jobs": 981,
    "failed_jobs": 0,
    "min_runtime_minutes": 0.00,
    "mean_runtime_minutes": 14.88,
    "median_runtime_minutes": 8.80,
    "p90_runtime_minutes": 30.47,
    "p95_runtime_minutes": 48.93,
    "p99_runtime_minutes": 94.95,
    "max_runtime_minutes": 156.42,
    "stddev_runtime_minutes": 18.23
  },
  "runtime_minutes": 14.88,
  "git_commit": "f63bf7",
  "config": {
    "algorithm": "PPC",
    "batch": "batch_001",
    "run_path": "/slurmshare/dgutman/bdsa-workflows-slurm/output/runs/20260116_215058_f63bf7",
    "manifest_path": "/slurmshare/dgutman/bdsa-workflows-slurm/output/runs/20260116_215058_f63bf7/batch_001/manifest.json",
    "slurm_state_filter": "COMPLETED",
    "exit_code_filter": "0:0"
  }
}
```

## Distribution Data

If you have distribution/histogram data, you can include it in the `config` object or as additional metrics:

```json
{
  "metrics": {
    "distribution_bins": [
      {"range": "0-13.03m", "count": 627},
      {"range": "13.03-26.07m", "count": 214},
      {"range": "26.07-39.10m", "count": 73}
    ]
  }
}
```

## Plot Files

Place any visualization files (PNG, SVG, JPG) in the same directory as `metrics.json`. The generator script will automatically:
- Copy them to `static/artifacts/<run_id>/`
- Include them in the generated experiment page

Common plot names:
- `runtime_distribution.png`
- `histogram.png`
- `sparkline.png`
- `performance_comparison.png`

## Usage

1. **Generate your JSON file:**
   ```bash
   your-script.py > results/run-abc123/metrics.json
   ```

2. **Add plot files (optional):**
   ```bash
   cp runtime_plot.png results/run-abc123/
   ```

3. **Run the generator:**
   ```bash
   python scripts/generate_experiment_pages.py results/run-abc123/
   ```

4. **Commit and push:**
   ```bash
   git add docs/experiments/ static/artifacts/
   git commit -m "Add experiment run abc123"
   git push
   ```

## Tips for Script Writers

1. **Use consistent date format:** Always use `YYYY-MM-DD` for dates
2. **Include git commit:** Helps with reproducibility
3. **Store paths in config:** Keep file paths in the `config` object for reference
4. **Use descriptive metric names:** Make metric keys self-explanatory
5. **Include units:** Add units to metric names (e.g., `runtime_minutes`, not just `runtime`)
6. **Round appropriately:** Use 2-4 decimal places for floats
7. **Include context:** Put algorithm version, parameters, and environment info in `config`

## Example Python Script Template

```python
import json
from datetime import datetime
import subprocess

def generate_metrics_json(run_id, dataset, model, metrics_dict, config_dict=None):
    """Generate metrics.json in the required format."""
    
    # Get git commit if available
    try:
        git_commit = subprocess.check_output(
            ['git', 'rev-parse', '--short', 'HEAD']
        ).decode().strip()
    except:
        git_commit = "unknown"
    
    metrics = {
        "run_id": run_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "dataset": dataset,
        "model": model,
        "metrics": metrics_dict,
        "git_commit": git_commit,
    }
    
    if config_dict:
        metrics["config"] = config_dict
    
    return metrics

# Example usage
metrics = generate_metrics_json(
    run_id="20260116_215058_f63bf7",
    dataset="batch_001",
    model="PPC-Original",
    metrics_dict={
        "total_jobs": 981,
        "mean_runtime_minutes": 14.88,
        "median_runtime_minutes": 8.80,
    },
    config_dict={
        "algorithm": "PPC",
        "batch": "batch_001",
    }
)

with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)
```
