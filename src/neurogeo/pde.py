import numpy as np
from skimage.restoration import denoise_tv_chambolle

def perona_malik_3d(u, n_iter=10, dt=0.08, kappa=0.15):
    """Explicit 3D anisotropic diffusion. Small dt is required for stability."""
    u=np.asarray(u,dtype=np.float32).copy()
    for _ in range(n_iter):
        grads=[]
        for ax in range(3):
            g=np.roll(u,-1,axis=ax)-u
            c=1.0/(1.0+(g/kappa)**2)
            grads.append(c*g - np.roll(c*g,1,axis=ax))
        u += dt*sum(grads)
    return u

def rof_tv_3d(u, weight=0.08):
    return denoise_tv_chambolle(u, weight=weight, channel_axis=None)
