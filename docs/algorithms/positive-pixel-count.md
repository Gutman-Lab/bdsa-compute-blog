# Positive Pixel Count (PPC)

The Positive Pixel Count algorithm is a color-based segmentation method designed for analyzing immunohistochemistry (IHC) stained tissue images. It classifies pixels based on their color properties in the HSI (Hue, Saturation, Intensity) color space.

## Overview

PPC identifies and categorizes "positive" pixels (typically representing stained tissue) by analyzing color characteristics rather than relying on intensity alone. This makes it particularly useful for IHC analysis where the color of the stain (e.g., brown for DAB staining) is the key indicator of positivity.

## Algorithm Classification

The algorithm classifies each pixel into one of four categories:

1. **Negative** - Pixels that do not meet the criteria for positivity
2. **Weak** - Positive pixels with lower intensity (above `intensity_weak_threshold`)
3. **Plain** - Positive pixels with moderate intensity (between `intensity_strong_threshold` and `intensity_weak_threshold`)
4. **Strong** - Positive pixels with high intensity (below `intensity_strong_threshold`)

## Key Parameters

The algorithm uses several tunable parameters in HSI color space:

- **Hue Value** (`hue_value`): Center of the hue range for positive color detection (default: 0.05, tuned for brown DAB staining)
- **Hue Width** (`hue_width`): Width of the acceptable hue range (default: 0.15)
- **Minimum Saturation** (`saturation_minimum`): Minimum saturation required for a pixel to be considered positive (default: 0.05)
- **Intensity Thresholds**:
  - `intensity_upper_limit`: Above this threshold, pixels are considered negative (default: 0.95)
  - `intensity_weak_threshold`: Separates weak from plain positive pixels (default: 0.75)
  - `intensity_strong_threshold`: Separates plain from strong positive pixels (default: 0.45)
  - `intensity_lower_limit`: Below this threshold, pixels are considered negative (default: 0.05)

## Implementation Details

The algorithm processes images in tiles for efficiency and supports parallel processing. It can work on entire images or specific regions of interest (ROIs) defined by annotations.

## Output

PPC produces:
- Pixel counts for each category (negative, weak, plain, strong)
- Statistical summaries (percentages, ratios)
- Optional label images showing the classification of each pixel
- Annotation files with results and parameters

## Use Cases

- Quantifying IHC staining intensity
- Automated scoring of tissue samples
- Quality control in histopathology workflows
- Research applications requiring reproducible staining quantification

## References

This implementation is adapted from [HistomicsTK](https://github.com/DigitalSlideArchive/HistomicsTK), originally developed for the Digital Slide Archive project.
