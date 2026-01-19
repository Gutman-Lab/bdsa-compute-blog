#!/usr/bin/env python3
"""
Generate experiment pages from JSON results.

This script:
1. Reads experiment JSON files (from a source directory or stdin)
2. Copies artifacts to static/artifacts/<run_id>/
3. Generates MDX pages in docs/experiments/YYYY/
4. Updates the experiments index page with a leaderboard table
"""

import json
import os
import shutil
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

# Paths relative to repo root
REPO_ROOT = Path(__file__).parent.parent
ARTIFACTS_DIR = REPO_ROOT / "static" / "artifacts"
EXPERIMENTS_DIR = REPO_ROOT / "docs" / "experiments"
INDEX_FILE = EXPERIMENTS_DIR / "_index.mdx"


def load_experiment_json(json_path: Path) -> Dict:
    """Load and validate experiment JSON."""
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    # Validate required fields
    required = ['run_id', 'date', 'dataset', 'model', 'metrics']
    missing = [field for field in required if field not in data]
    if missing:
        raise ValueError(f"Missing required fields: {missing}")
    
    return data


def copy_artifacts(source_dir: Path, run_id: str) -> List[str]:
    """
    Copy artifacts from source directory to static/artifacts/<run_id>/.
    Returns list of copied file names.
    """
    target_dir = ARTIFACTS_DIR / run_id
    target_dir.mkdir(parents=True, exist_ok=True)
    
    copied_files = []
    
    # Copy JSON file
    json_file = source_dir / "metrics.json"
    if json_file.exists():
        shutil.copy2(json_file, target_dir / "metrics.json")
        copied_files.append("metrics.json")
    
    # Copy plot files (png, svg, jpg)
    for ext in ['*.png', '*.svg', '*.jpg', '*.jpeg']:
        for plot_file in source_dir.glob(ext):
            shutil.copy2(plot_file, target_dir / plot_file.name)
            copied_files.append(plot_file.name)
    
    return copied_files


def generate_experiment_page(experiment: Dict, artifacts: List[str]) -> str:
    """Generate MDX content for an experiment page."""
    run_id = experiment['run_id']
    date = experiment['date']
    dataset = experiment['dataset']
    model = experiment['model']
    metrics = experiment.get('metrics', {})
    git_commit = experiment.get('git_commit', 'N/A')
    runtime = experiment.get('runtime_minutes')
    config = experiment.get('config', {})
    
    # Find plot files
    plot_files = [f for f in artifacts if f.endswith(('.png', '.svg', '.jpg', '.jpeg'))]
    
    # Build metrics table
    metrics_rows = []
    for key, value in metrics.items():
        if isinstance(value, float):
            value = f"{value:.4f}"
        metrics_rows.append(f"| {key.upper()} | {value} |")
    
    metrics_table = "\n".join(metrics_rows) if metrics_rows else "| *No metrics available* | |"
    
    # Build plots section
    plots_section = ""
    if plot_files:
        plots_section = "\n## Plots\n\n"
        for plot_file in plot_files:
            plot_name = plot_file.replace('_', ' ').replace('.png', '').replace('.svg', '').title()
            plots_section += f"![{plot_name}](/artifacts/{run_id}/{plot_file})\n\n"
    
    # Build config section
    config_section = ""
    if config:
        config_section = f"\n## Configuration\n\n```json\n{json.dumps(config, indent=2)}\n```\n\n"
    
    # Build runtime info
    runtime_section = ""
    if runtime is not None:
        runtime_section = f"- **Runtime:** {runtime} minutes\n"
    
    content = f"""---
title: Run {run_id}
---

# Experiment Run: {run_id}

## Summary

- **Date:** {date}
- **Dataset:** {dataset}
- **Model:** {model}
- **Git commit:** `{git_commit}`
{runtime_section}
## Key Metrics

| Metric | Value |
|--------|-------|
{metrics_table}

{plots_section}## Artifacts

- [metrics.json](/artifacts/{run_id}/metrics.json)
"""
    
    if config_section:
        content += config_section
    
    return content


def update_index_page(experiments: List[Dict]) -> str:
    """Generate the experiments index page with leaderboard table."""
    # Sort by date (newest first)
    sorted_exps = sorted(experiments, key=lambda x: x['date'], reverse=True)
    
    # Build table rows
    table_rows = []
    for exp in sorted_exps:
        metrics = exp.get('metrics', {})
        auc = metrics.get('auc', 'N/A')
        f1 = metrics.get('f1', 'N/A')
        
        # Format metrics
        if isinstance(auc, float):
            auc = f"{auc:.4f}"
        if isinstance(f1, float):
            f1 = f"{f1:.4f}"
        
        year = exp['date'][:4]
        run_id = exp['run_id']
        link = f"/docs/experiments/{year}/{exp['date']}_{run_id}"
        
        table_rows.append(
            f"| {exp['date']} | [{run_id}]({link}) | {exp['dataset']} | "
            f"{exp['model']} | {auc} | {f1} | ✅ |"
        )
    
    if not table_rows:
        table_rows = ["| *No experiments yet* | | | | | | |"]
    
    content = f"""---
title: Experiment Registry
---

# Experiment Registry

This page provides an overview of all experiment runs. Individual experiment pages are auto-generated from JSON results.

## Leaderboard

| Date | Run ID | Dataset | Model | AUC | F1 | Status |
|------|--------|---------|-------|-----|-----|--------|
{chr(10).join(table_rows)}

---

*This table is auto-generated by `scripts/generate_experiment_pages.py`.*

## Adding Experiments

To add a new experiment:

1. Ensure your experiment outputs a JSON file with the required schema (see README)
2. Place artifacts (JSON + plots) in the appropriate location
3. Run the generator script: `python scripts/generate_experiment_pages.py <source_dir>`
4. Commit and push

The generator will:
- Copy artifacts to `static/artifacts/<run_id>/`
- Generate an MDX page in `docs/experiments/YYYY/`
- Update this leaderboard table
"""
    
    return content


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: generate_experiment_pages.py <source_dir> [<source_dir> ...]")
        print("\n  source_dir: Directory containing metrics.json and plot files")
        print("\nExample:")
        print("  python scripts/generate_experiment_pages.py results/run-abc123 results/run-def456")
        sys.exit(1)
    
    source_dirs = [Path(d) for d in sys.argv[1:]]
    
    # Ensure directories exist
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    EXPERIMENTS_DIR.mkdir(parents=True, exist_ok=True)
    
    experiments = []
    
    # Process each source directory
    for source_dir in source_dirs:
        if not source_dir.exists():
            print(f"Warning: {source_dir} does not exist, skipping", file=sys.stderr)
            continue
        
        json_file = source_dir / "metrics.json"
        if not json_file.exists():
            print(f"Warning: {json_file} not found, skipping {source_dir}", file=sys.stderr)
            continue
        
        try:
            # Load experiment data
            experiment = load_experiment_json(json_file)
            run_id = experiment['run_id']
            
            # Copy artifacts
            artifacts = copy_artifacts(source_dir, run_id)
            print(f"Copied {len(artifacts)} artifacts for run {run_id}")
            
            # Generate experiment page
            page_content = generate_experiment_page(experiment, artifacts)
            
            # Determine year directory
            year = experiment['date'][:4]
            year_dir = EXPERIMENTS_DIR / year
            year_dir.mkdir(parents=True, exist_ok=True)
            
            # Write page
            page_file = year_dir / f"{experiment['date']}_{run_id}.mdx"
            with open(page_file, 'w') as f:
                f.write(page_content)
            print(f"Generated page: {page_file}")
            
            experiments.append(experiment)
            
        except Exception as e:
            print(f"Error processing {source_dir}: {e}", file=sys.stderr)
            continue
    
    # Update index page
    if experiments:
        index_content = update_index_page(experiments)
        with open(INDEX_FILE, 'w') as f:
            f.write(index_content)
        print(f"Updated index page: {INDEX_FILE}")
    
    print(f"\nProcessed {len(experiments)} experiment(s)")


if __name__ == "__main__":
    main()
