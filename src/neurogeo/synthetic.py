import numpy as np
from scipy.ndimage import gaussian_filter

def make_brain_tumor_phantom(shape=(96,96,96), seed=7):
    """Create a deterministic 3D ellipsoidal brain with irregular tumor and 4 MRI-like modalities."""
    rng=np.random.default_rng(seed)
    z,y,x=np.indices(shape)
    c=np.array(shape)/2
    brain=((x-c[2])/(0.40*shape[2]))**2+((y-c[1])/(0.45*shape[1]))**2+((z-c[0])/(0.42*shape[0]))**2 <= 1
    tc=np.array([0.61*shape[0],0.44*shape[1],0.57*shape[2]])
    r=((x-tc[2])/(0.11*shape[2]))**2+((y-tc[1])/(0.13*shape[1]))**2+((z-tc[0])/(0.10*shape[0]))**2
    perturb=0.12*np.sin(x/4)*np.sin(y/5)*np.sin(z/6)
    tumor=(r+perturb <= 1) & brain
    edema=((x-tc[2])/(0.16*shape[2]))**2+((y-tc[1])/(0.19*shape[1]))**2+((z-tc[0])/(0.15*shape[0]))**2 <= 1
    edema=edema & brain
    base=gaussian_filter(brain.astype(float), 1.2)
    noise=lambda s: rng.normal(0,s,shape)
    t1=0.55*base + 0.20*tumor + noise(0.035)
    t1ce=0.50*base + 0.55*tumor + noise(0.035)
    t2=0.50*base + 0.35*edema + 0.20*tumor + noise(0.04)
    flair=0.45*base + 0.55*edema + 0.15*tumor + noise(0.04)
    imgs=np.stack([t1,t1ce,t2,flair]).astype(np.float32)
    return imgs, brain.astype(np.uint8), tumor.astype(np.uint8), edema.astype(np.uint8)
