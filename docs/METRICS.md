# Metrics

For prediction P and ground truth G:

- Dice = `2|P∩G|/(|P|+|G|)`
- IoU = `|P∩G|/|P∪G|`
- Sensitivity = `TP/(TP+FN)`
- Specificity = `TN/(TN+FP)`
- Precision = `TP/(TP+FP)`
- HD95 = 95th percentile of symmetric boundary nearest-neighbor distances
- ASSD = mean symmetric surface distance

Voxel spacing must be provided for physical-distance metrics. A value in voxels is not interchangeable with millimeters.
