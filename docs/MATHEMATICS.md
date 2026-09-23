# Mathematical Foundations

## Image as a function
A 3D MR image is modeled as a scalar field \(f:\Omega\subset\mathbb R^3\to\mathbb R\); multimodal MRI is a vector-valued field.

## Variational view
Segmentation balances fidelity to observed image evidence and regularity of the inferred region. Total variation encourages piecewise-regular solutions while preserving discontinuities better than quadratic smoothness.

## Surface geometry
A tumor boundary is a two-dimensional manifold embedded in \(\mathbb R^3\), approximated by a triangular mesh. Discrete differential geometry gives local normals, curvature surrogates and global shape descriptors.

## Shape descriptors
For volume \(V\) and area \(A\), sphericity is
\[
\psi=\frac{\pi^{1/3}(6V)^{2/3}}{A},
\]
with \(\psi=1\) for an ideal sphere. Principal-axis ratios quantify elongation.

## Surface distance
Given boundary point sets A and B, the symmetric Hausdorff distance uses maximum nearest-neighbor error. HD95 replaces the maximum by the 95th percentile for robustness to isolated outliers.

## Topology
Connected components and Euler characteristic measure global structure. Persistent homology can extend this analysis across threshold filtrations and detect stable connected components, loops and cavities.
