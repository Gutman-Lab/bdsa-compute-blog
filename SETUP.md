# Quick Setup Guide

## Initial Setup

1. **Install dependencies:**
   ```bash
   cd bdsa-compute-blog
   npm install
   ```

2. **Start development server:**
   ```bash
   npm start
   ```
   Visit `http://localhost:3000/bdsa-compute-blog/` to see your site.
   
   **Note:** The baseUrl `/bdsa-compute-blog/` is required for local development to match the GitHub Pages deployment path.

## First Steps

### 1. Add Your Logo (Optional)

Place your logo files in `static/img/`:
- `logo.svg` - Main logo (recommended)
- `favicon.ico` - Browser favicon

### 2. Customize Configuration

Edit `docusaurus.config.ts` to:
- Update site title/tagline
- Add social links
- Customize theme colors in `src/css/custom.css`

### 3. Add Your First Experiment

1. Create a directory with your experiment results:
   ```bash
   mkdir -p results/my-first-run
   ```

2. Create `results/my-first-run/metrics.json`:
   ```json
   {
     "run_id": "my-first-run",
     "date": "2026-01-19",
     "dataset": "TCGA-SKCM",
     "model": "BDSA-Pipeline-v0.3",
     "metrics": {
       "auc": 0.91,
       "f1": 0.84,
       "precision": 0.88,
       "recall": 0.81
     },
     "runtime_minutes": 42,
     "git_commit": "abc123"
   }
   ```

3. Add any plot files (PNG, SVG) to the same directory

4. Generate the experiment page:
   ```bash
   python scripts/generate_experiment_pages.py results/my-first-run/
   ```

5. View the generated page in your docs

### 4. Write Your First Blog Post

Edit or create a new file in `blog/` following the existing format.

## GitHub Pages Deployment

1. **Create the repository:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/gutman-lab/bdsa-compute-blog.git
   git push -u origin main
   ```

2. **Enable GitHub Pages:**
   - Go to repository Settings → Pages
   - Source: GitHub Actions
   - The workflow will deploy automatically on push to `main`

3. **Access your site:**
   - `https://gutman-lab.github.io/bdsa-compute-blog/`

## Next Steps

- Customize the documentation pages in `docs/`
- Add more blog posts
- Integrate with your experiment pipeline
- Customize the theme and styling

For more details, see the [README.md](README.md).
