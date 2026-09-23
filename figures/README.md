# Generated visualization assets

The research code generates the visualization set used by this project, including:

- `figures/pipeline/research_pipeline.png`
- `figures/mri/synthetic_multimodal_mri.png`
- `figures/curves/training_curves.png`
- `figures/curves/metric_dashboard.png`
- `figures/geometry/radial_shape_histogram.png`
- `figures/3d/tumor_surface.png`
- `figures/3d/tumor_in_brain.png`
- `figures/3d/brain_tumor_rotation.gif`

These binary demonstration assets are generated from synthetic data and are not clinical patient images. The Python visualization and synthetic-data modules in `src/neurogeo/` and `scripts/run_synthetic_demo.py` provide reproducible generation paths. Binary outputs are intentionally kept separate from clinical data and must never contain protected health information.
