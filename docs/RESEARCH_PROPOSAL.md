# Research Proposal

## Title
**BrainTumor Geometry: Variational, Topological and Geometric Deep Learning for Multimodal MRI Tumor Reconstruction and Shape Analysis**

## Motivation
Brain-tumor segmentation is commonly reported using voxel-overlap metrics, but downstream quantitative geometry depends on accurate boundaries and stable topology. A mask can attain a high Dice score while still exhibiting clinically or geometrically important surface errors. This project therefore treats segmentation as both an image-analysis problem and a geometric inverse problem.

## Mathematical formulation
Let the multimodal MRI be
\[
F=(f_{T1},f_{T1ce},f_{T2},f_{FLAIR}):\Omega\subset\mathbb{R}^3\to\mathbb{R}^4.
\]
We seek a segmentation probability field \(u:\Omega\to[0,1]^K\). A composite objective is
\[
\mathcal L = \lambda_D\mathcal L_{Dice}+\lambda_C\mathcal L_{CE}+\lambda_B\mathcal L_{boundary}
+\lambda_T\mathcal L_{topology}+\lambda_R\mathcal R(u).
\]
The variational regularizer \(\mathcal R\) may use total variation or curvature-inspired penalties. Surface terms are evaluated on the induced boundary \(\partial\{u>\tau\}\).

## PDE preprocessing
Perona-Malik type anisotropic diffusion:
\[
\partial_t u = \nabla\cdot\left(g(|\nabla u|)\nabla u\right), \qquad
 g(s)=\frac{1}{1+(s/\kappa)^2}.
\]
ROF denoising:
\[
\hat u=\arg\min_u \frac12\|u-f\|_2^2+\lambda\,TV(u).
\]

## 3D geometry
From a binary segmentation \(S\), marching cubes extracts a triangular surface \(M=(V,E,F)\). The project computes area, enclosed volume, principal axes, sphericity, graph-Laplacian curvature proxy, connected components and Euler characteristic.

## Tumor position
Position is reported relative to the brain geometry, not as an unsupported neuroanatomical diagnosis. If \(c_T\) is the tumor centroid and \([b_{min},b_{max}]\) the brain bounding box, normalized coordinates are
\[
\xi=(c_T-b_{min})/(b_{max}-b_{min}).
\]
These values support reproducible coarse descriptors and visualization.

## Evaluation
Primary: Dice, IoU, HD95, ASSD, sensitivity and specificity. Secondary: volume error, centroid error, surface area error, topology errors and calibration.

## Validation philosophy
Patient-level splits, no slice leakage, deterministic seeds, configuration snapshots, ablation studies, missing-modality stress tests and explicit distinction between synthetic demos and real-data benchmarks.
