# Experiment Protocol

1. Split at patient level before any patch/slice generation.
2. Fit preprocessing only on training data where relevant.
3. Record spacing, orientation and crop transforms.
4. Train a plain 3D U-Net baseline.
5. Add one component at a time: PDE preprocessing, boundary loss, topology loss, geometric refinement.
6. Evaluate whole tumor (WT), tumor core (TC), enhancing tumor (ET) separately when labels permit.
7. Report Dice and HD95 together.
8. Stress test missing modalities and intensity/noise shifts.
9. Repeat across seeds; report mean and standard deviation.
10. Save model card, configuration and software environment.
