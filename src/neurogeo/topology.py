import numpy as np
from scipy.ndimage import label, binary_fill_holes
from skimage.measure import euler_number

def topology_features(mask, connectivity=3):
    m=np.asarray(mask).astype(bool)
    _,ncomp=label(m)
    e=int(euler_number(m, connectivity=connectivity))
    filled=binary_fill_holes(m)
    cavities=int(np.logical_and(filled,~m).sum()>0)
    return {"connected_components":int(ncomp),"euler_characteristic":e,"has_enclosed_cavity":cavities}
