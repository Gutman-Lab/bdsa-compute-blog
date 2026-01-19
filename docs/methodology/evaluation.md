# Evaluation Methodology

This page documents how experiments are evaluated in BDSA.

## Metrics

Document the key metrics used for evaluation:

- **AUC** - Area Under the ROC Curve
- **F1 Score** - Harmonic mean of precision and recall
- **Precision** - True positives / (True positives + False positives)
- **Recall** - True positives / (True positives + False negatives)

## Evaluation Protocol

Describe the standard evaluation procedure:

1. Data preparation and splitting
2. Model training (if applicable)
3. Inference and prediction
4. Metric calculation
5. Visualization (PR curves, ROC curves, etc.)

## Reproducibility

All experiments should include:

- Git commit hash
- Dataset version
- Model/pipeline version
- Configuration parameters
- Runtime and resource usage

---

*Update this page as evaluation protocols evolve.*
