import numpy as np

def centroid(mask):
    pts=np.argwhere(np.asarray(mask)>0)
    if len(pts)==0: return np.array([np.nan]*3)
    return pts.mean(0)

def normalized_position(tumor, brain):
    t=centroid(tumor); pts=np.argwhere(np.asarray(brain)>0)
    lo=pts.min(0); hi=pts.max(0); xi=(t-lo)/(hi-lo+1e-8)
    z,y,x=xi
    return {"superior_fraction":float(z),"posterior_fraction":float(y),"right_fraction":float(x),
            "left_right":"right" if x>0.5 else "left",
            "anterior_posterior":"posterior" if y>0.5 else "anterior",
            "inferior_superior":"superior" if z>0.5 else "inferior"}

def volume_fraction(tumor, brain):
    return float(np.sum(tumor)/max(np.sum(brain),1))
