# BDSA Compute Blog

**Repository:** `gutman-lab/bdsa-compute-blog`  
**Purpose:**  
A lightweight, reproducible website for tracking BDSA experiment results, benchmarks, and updates using a **Markdown-first, data-driven workflow**.

This site serves as:
- 📊 **Experiment Registry** - Browse and compare experiment results
- 📝 **Lab Notebook** - Track methodology, datasets, and evaluation protocols  
- 🗞️ **Blog** - Release notes, experiment highlights, and progress updates

The site is static, version-controlled, and published automatically via GitHub Actions.

## Why This Architecture

### Design Goals
- Results are **generated programmatically** (JSON → Markdown/MDX)
- Minimal maintenance (no servers, no databases)
- GitHub-native (PRs, diffs, provenance)
- Human-readable + machine-structured
- Easy to expand later (interactive tables, plots, dashboards)

### Chosen Stack
- **Docusaurus** (Markdown + MDX + React)
- **GitHub Pages** for hosting
- **GitHub Actions** for build & deploy
- **Python** scripts to generate pages from experiment outputs

This avoids WordPress-style overhead while still supporting:
- Blog posts
- Documentation
- Structured experiment summaries

## Repository Structure

```
bdsa-compute-blog/
├── blog/                    # Human-written narrative updates
│   └── 2026-01-19-welcome.md
│
├── docs/
│   ├── index.md            # Landing page
│   ├── methodology/
│   │   ├── datasets.md
│   │   └── evaluation.md
│   └── experiments/
│       ├── _index.mdx      # Auto-generated leaderboard
│       └── 2026/           # Year-organized experiment pages
│
├── static/
│   └── artifacts/          # Experiment outputs (JSON, plots)
│       └── <run_id>/
│           ├── metrics.json
│           └── *.png
│
├── scripts/
│   └── generate_experiment_pages.py
│
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions deployment
│
├── docusaurus.config.ts
├── sidebars.ts
├── package.json
└── README.md
```

## Experiment Data Workflow

### Step 1: Experiments Emit Structured Outputs

Each experiment run should produce:
- `metrics.json` (primary results)
- Plots (`.png` / `.svg`)
- Optional metadata (`run_meta.json`)

**Required JSON Schema:**

```json
{
  "run_id": "abc123",
  "date": "2026-01-16",
  "dataset": "TCGA-SKCM",
  "model": "BDSA-Pipeline-v0.3",
  "metrics": {
    "auc": 0.91,
    "f1": 0.84,
    "precision": 0.88,
    "recall": 0.81
  },
  "runtime_minutes": 42,
  "git_commit": "a1b2c3d"
}
```

**Optional fields:**
- `config` - Configuration parameters (object)
- `slurm_job_id` - SLURM job identifier
- `gpu_info` - GPU resource information
- `resource_usage` - CPU/memory usage stats

### Step 2: Generator Script Converts Data → MDX

Run the generator script:

```bash
python scripts/generate_experiment_pages.py <source_dir1> [<source_dir2> ...]
```

The script will:
1. Copy artifacts to `static/artifacts/<run_id>/`
2. Generate MDX pages in `docs/experiments/YYYY/`
3. Update `docs/experiments/_index.mdx` (leaderboard)

**Example:**

```bash
# Process a single experiment
python scripts/generate_experiment_pages.py results/run-abc123/

# Process multiple experiments
python scripts/generate_experiment_pages.py results/run-abc123/ results/run-def456/
```

### Step 3: Commit & Push

Markdown/MDX pages are versioned, artifacts are immutable per run, and every change is auditable.

## Local Development

### Prerequisites

- Node.js 18+ and npm
- Python 3.11+

### Setup

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Start development server:**
   ```bash
   npm start
   ```
   
   This starts a local development server. Access it at:
   - `http://localhost:3000/bdsa-compute-blog/` (or the port shown in the terminal)
   
   **Note:** The `/bdsa-compute-blog/` path is required to match the GitHub Pages deployment structure.

3. **Build for production:**
   ```bash
   npm run build
   ```

## Deployment

### GitHub Pages Setup

1. **Enable GitHub Pages:**
   - Go to repository Settings → Pages
   - Source: GitHub Actions

2. **Push to main branch:**
   - The GitHub Actions workflow will automatically:
     - Install dependencies
     - Run the generator script (if experiment results exist)
     - Build the static site
     - Deploy to GitHub Pages

3. **Access your site:**
   - URL: `https://gutman-lab.github.io/bdsa-compute-blog/`

### Manual Deployment

If you prefer to deploy manually:

```bash
npm run build
npm run deploy
```

## Adding Content

### Adding an Experiment

1. **Prepare your experiment results:**
   ```bash
   mkdir -p results/my-run-abc123
   # Copy metrics.json and plots to results/my-run-abc123/
   ```

2. **Generate pages:**
   ```bash
   python scripts/generate_experiment_pages.py results/my-run-abc123/
   ```

3. **Commit and push:**
   ```bash
   git add docs/experiments/ static/artifacts/
   git commit -m "Add experiment run abc123"
   git push
   ```

### Writing a Blog Post

Create a new file in `blog/` with the format:

```
blog/YYYY-MM-DD-post-title.md
```

Example frontmatter:

```markdown
---
slug: my-post
title: My Post Title
authors:
  - name: Your Name
tags: [tag1, tag2]
---

Your blog post content here...
```

### Adding Documentation

Add Markdown files to `docs/` and update `sidebars.ts` to include them in navigation.

## Maintenance Philosophy

- ✅ No databases
- ✅ No backend services
- ✅ No manual website editing
- ✅ Everything is reproducible, scriptable, and reviewable

If this ever needs to become interactive, React components can be added without rewriting content.

## Future Extensions (Optional)

- Interactive leaderboard (MDX + React)
- Per-dataset filtering
- Linking runs to Slurm job IDs
- Auto-ingest from CI / Slurm logs
- Badges for "best-in-class" runs

## License

[Add your license here]

## Contributing

[Add contribution guidelines if applicable]

---

**Guiding Rule:** If a result cannot be regenerated from data, it does not belong in this repo.
