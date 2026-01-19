# Welcome to BDSA Compute Blog

This site tracks experiment results, benchmarks, and updates for the **BDSA** (open source image analysis platform) project.

## What is This Site?

This is a **data-first, Markdown-based experiment tracking system** that serves as:

- 📊 **Experiment Registry** - Browse and compare experiment results
- 📝 **Lab Notebook** - Track methodology, datasets, and evaluation protocols
- 🗞️ **Blog** - Release notes, experiment highlights, and progress updates

## Core Principles

1. **Results are data** - Experiments emit JSON + plots; pages are generated programmatically
2. **Markdown-first** - Easy to diff, review, and version
3. **No servers** - Static site hosted on GitHub Pages
4. **Low maintenance** - GitHub Actions handles builds automatically

## Quick Navigation

- **[Algorithms](/docs/algorithms)** - Learn about BDSA algorithms and methods
- **[Experiments](/docs/experiments)** - Browse experiment results and leaderboard
- **[Methodology](/docs/methodology)** - Learn about datasets and evaluation protocols
- **[Blog](/blog)** - Read updates and release notes

## Getting Started

To add a new experiment:

1. Run your experiment pipeline (emits `metrics.json` + plots)
2. Run the generator script: `python scripts/generate_experiment_pages.py`
3. Commit and push - GitHub Actions will publish automatically

For more details, see the [README](https://github.com/gutman-lab/bdsa-compute-blog) in the repository.
