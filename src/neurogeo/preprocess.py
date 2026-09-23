import numpy as np
from skimage.registration import phase_cross_correlation
from scipy.ndimage import shift

def zscore_nonzero(volume, eps=1e-8):
    v=volume.astype(np.float32).copy(); m=v!=0
    if not np.any(m): return v
    mu,sd=v[m].mean(),v[m].std()
    v[m]=(v[m]-mu)/(sd+eps)
    return v

def robust_percentile_scale(volume, lo=1, hi=99):
    a,b=np.percentile(volume,[lo,hi]); return np.clip((volume-a)/(b-a+1e-8),0,1)

def register_translation(fixed, moving):
    s,err,_=phase_cross_correlation(fixed,moving,upsample_factor=10)
    return shift(moving,s,order=1), s, err
