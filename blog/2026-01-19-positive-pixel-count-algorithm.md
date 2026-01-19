---
slug: positive-pixel-count-algorithm
title: Understanding the Positive Pixel Count Algorithm
authors:
  - name: David Gutman
    title: BDSA Project Maintainer
    url: https://github.com/dagutman
    image_url: https://github.com/dagutman.png
tags: [algorithms, ihc, image-analysis, segmentation]
---

The Positive Pixel Count (PPC) algorithm is one of the core image analysis methods in BDSA. In this post, we'll explore how it works, why we use HSI color space, and how to interpret its results.

## What is Positive Pixel Count?

Positive Pixel Count is a color-based segmentation algorithm designed specifically for immunohistochemistry (IHC) analysis. Unlike intensity-based methods, PPC analyzes pixels in the **HSI (Hue, Saturation, Intensity) color space** to identify and classify stained tissue.

The algorithm is particularly useful for DAB (3,3'-Diaminobenzidine) stained images, where brown coloration indicates positive staining. By working in HSI space, we can separate color information (hue) from brightness (intensity), making the detection more robust to variations in lighting and image acquisition.

## How It Works: The Classification Process

PPC classifies each pixel into one of four categories based on its HSI properties:

1. **Negative**: Pixels that don't meet positivity criteria
2. **Weak**: Positive pixels with lower intensity
3. **Plain**: Positive pixels with moderate intensity  
4. **Strong**: Positive pixels with high intensity

### The Core Logic

The algorithm evaluates each pixel using a series of thresholds:

```python
# Key parameters (defaults tuned for brown DAB staining)
hue_value = 0.05          # Center of hue range
hue_width = 0.15          # Width of acceptable hue range
saturation_minimum = 0.05 # Minimum saturation for positivity
intensity_upper_limit = 0.95    # Above this = negative
intensity_weak_threshold = 0.75  # Separates weak from plain
intensity_strong_threshold = 0.45 # Separates plain from strong
intensity_lower_limit = 0.05     # Below this = negative
```

A pixel is considered positive if:
- Its hue falls within the specified range (`hue_value ± hue_width/2`)
- Its saturation is above `saturation_minimum`
- Its intensity is between `intensity_lower_limit` and `intensity_upper_limit`

Once identified as positive, the pixel is further classified as weak, plain, or strong based on its intensity relative to the threshold values.

## Implementation: Tile-Based Processing

The BDSA implementation processes images efficiently using a tile-based approach with parallel processing:

```python
# Process images in parallel using multiprocessing
with Pool(args.nproc) as pool:
    jobs = [
        pool.apply_async(
            tile_positive_pixel_count,
            (
                args.inputImageFile,
                tile["tile_position"]["position"],
                tiparams,
                ppc_params,
                color_map,
                useAlpha,
                region_polygons,
                args.style,
            ),
        )
        for tile in ts.tileIterator(**tiparams)
    ]
```

This approach:
- **Processes images in 4096×4096 pixel tiles** for memory efficiency
- **Uses multiprocessing** (default: 20 parallel processes) for speed
- **Supports region of interest (ROI) analysis** via annotations
- **Handles large whole-slide images** without loading everything into memory

## Color Mapping

The algorithm produces a color-coded label image where each pixel class is visualized:

```python
# Define color map for visualization
color_map = np.empty((4, 4), dtype=np.uint8)
color_map[ppc.Labels.NEGATIVE] = 255, 255, 255, 255  # White
color_map[ppc.Labels.WEAK] = 60, 78, 194, 255      # Blue
color_map[ppc.Labels.PLAIN] = 221, 220, 220, 255   # Light gray
color_map[ppc.Labels.STRONG] = 180, 4, 38, 255      # Red
```

This visualization helps users understand the spatial distribution of staining intensity across the tissue.

## Visualizing PPC Results

The PPC algorithm produces color-coded output images that clearly show the classification of each pixel. The visualization uses the following color scheme:

- **White** = Negative pixels
- **Blue** = Weak positive pixels  
- **Light gray** = Plain positive pixels
- **Red** = Strong positive pixels

<!-- 
Example images will be added here once available:
- Original IHC image with PPC classification overlay
- Region-specific analysis examples
- Detailed classification maps
-->

## Results and Statistics

After processing, the algorithm combines results from all tiles and calculates statistics:

```python
# Combine the results and calculate statistics
stats = ppc._totals_to_stats(ppc._combine(results))
```

The output includes:
- **Pixel counts** for each category
- **Percentages** of positive vs. negative pixels
- **Ratios** of strong/weak/plain positive pixels
- **Total pixel counts** for the analyzed region

These statistics are saved in an annotation file along with all parameters used, ensuring full reproducibility.

## Why HSI Color Space?

Working in HSI (rather than RGB) provides several advantages:

1. **Color separation**: Hue represents the "color" independent of brightness
2. **Intensity control**: Intensity can be analyzed separately from color
3. **Robustness**: Less sensitive to lighting variations and image acquisition differences
4. **Interpretability**: Parameters map more directly to visual perception

For IHC analysis, this means we can reliably detect brown DAB staining even when images have varying brightness or were acquired on different scanners.

## Practical Usage

The algorithm can be run via the BDSA CLI:

```bash
PositivePixelCount \
  --inputImageFile image.svs \
  --region "-1,-1,-1,-1" \
  --outputAnnotationFile results.anot \
  --outputLabelImage labels.tiff \
  --nproc 20
```

It also supports:
- **ROI analysis** via annotation documents
- **Group filtering** to analyze specific annotation groups
- **Multi-frame images** with frame selection
- **Style options** for multi-channel image compositing

## Applications

PPC is widely used for:
- **Automated IHC scoring** in research and clinical workflows
- **Quality control** of staining procedures
- **Quantitative analysis** of biomarker expression
- **Reproducible quantification** for publication and validation

## Future Directions

We're continuously improving the algorithm, including:
- Better parameter tuning for different stain types
- Integration with machine learning for adaptive thresholding
- Support for multi-stain analysis
- Real-time processing capabilities

For more technical details, see the [algorithm documentation](/docs/algorithms/positive-pixel-count).
