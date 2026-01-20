
# BDSA Compute Blog

Welcome to the **BDSA Compute Blog** — a comprehensive resource for tracking algorithms, performance metrics, and computational benchmarks for the **BDSA** (open source image analysis platform) project.

## What is BDSA?

BDSA is an open-source image analysis platform designed for histopathology and medical image analysis. This site provides:

- 📊 **Algorithm Documentation** - Detailed descriptions of available functions and methods
- ⚡ **Performance Metrics** - Runtime benchmarks and execution time comparisons
- 🖥️ **Hardware Comparisons** - Performance across different compute environments
- 📈 **Experiment Tracking** - Reproducible results and methodology documentation

## Available Functions

BDSA provides a suite of image analysis algorithms optimized for whole-slide imaging and histopathology workflows:

### Core Algorithms

#### [Positive Pixel Count (PPC)](/docs/algorithms/positive-pixel-count)
A color-based segmentation algorithm for immunohistochemistry (IHC) analysis. Classifies pixels in HSI color space to identify and quantify staining intensity.

- **Use Cases**: IHC scoring, automated tissue analysis, biomarker quantification
- **Input**: Whole-slide images (SVS, TIFF) or image regions
- **Output**: Pixel classifications (negative, weak, plain, strong), statistical summaries, label images

*[Learn more about PPC →](/docs/algorithms/positive-pixel-count)*

### Additional Functions

*More algorithms will be documented as they are added to BDSA.*

## Performance Metrics

This site tracks performance characteristics of BDSA functions across different scenarios:

### Runtime Benchmarks

Performance metrics include:
- **Execution time** for different image sizes
- **Memory usage** during processing
- **Throughput** (images processed per hour)
- **Scalability** with parallel processing

### Typical Performance

Performance varies based on:
- Image size and resolution
- Number of parallel processes
- Hardware specifications
- Region of interest (ROI) size

*Detailed performance data is available in the [Experiments](/docs/experiments) section.*

## Hardware Comparisons

We track and compare performance across different compute environments:

### Supported Platforms

- **Local workstations** - Development and testing
- **High-performance clusters** - Large-scale batch processing
- **Cloud computing** - Scalable on-demand processing
- **GPU acceleration** - Where applicable

### Performance Factors

Key factors affecting performance:
- **CPU cores** - Parallel processing capability
- **Memory** - Large image handling
- **Storage I/O** - Image loading speed
- **Network** - For distributed processing

*Hardware-specific benchmarks and comparisons will be documented as data becomes available.*

## Site Contents

This site is organized into several sections:

### 📚 [Algorithms](/docs/algorithms)
Comprehensive documentation of BDSA algorithms, including:
- Algorithm descriptions and theory
- Parameter explanations
- Usage examples
- Implementation details

### 📊 [Experiments](/docs/experiments)
Experiment registry with:
- Automated result tracking
- Performance comparisons
- Reproducible configurations
- Statistical summaries

### 📝 [Methodology](/docs/methodology)
Documentation of:
- Datasets used in analysis
- Evaluation protocols
- Quality control procedures
- Best practices

### 🗞️ [Blog](/blog)
Regular updates including:
- Algorithm introductions and tutorials
- Performance analysis reports
- Hardware comparison studies
- Release notes and updates

## Getting Started

### For Users

1. **Explore Algorithms** - Start with the [Algorithms](/docs/algorithms) section to understand available functions
2. **Review Performance** - Check the [Experiments](/docs/experiments) section for runtime benchmarks
3. **Read the Blog** - Follow the [Blog](/blog) for updates and detailed analyses

### For Contributors

To add new experiment results:

1. Run your analysis pipeline (outputs JSON + plots)
2. Run the generator: `python scripts/generate_experiment_pages.py <results-dir>`
3. Commit and push - GitHub Actions will publish automatically

See the [README](https://github.com/gutman-lab/bdsa-compute-blog) for detailed instructions.

## Data-Driven Approach

This site follows a **data-first philosophy**:

- ✅ All results are generated from structured data (JSON)
- ✅ Full reproducibility with versioned parameters
- ✅ Automated updates via GitHub Actions
- ✅ Transparent and auditable results

Every experiment includes:
- Complete parameter configurations
- Runtime and resource usage
- Git commit hashes for reproducibility
- Raw data and visualizations

---

**BDSA Compute Blog** - Tracking algorithms, performance, and benchmarks for reproducible image analysis.
