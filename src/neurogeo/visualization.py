from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from .geometry import mask_to_mesh

def save_orthogonal(volume,mask,out):
    Path(out).parent.mkdir(parents=True,exist_ok=True); z,y,x=np.array(volume.shape)//2
    fig,axs=plt.subplots(1,3,figsize=(12,4));
    for ax,img,m,title in [(axs[0],volume[z],mask[z],'axial'),(axs[1],volume[:,y,:],mask[:,y,:],'coronal'),(axs[2],volume[:,:,x],mask[:,:,x],'sagittal')]:
        ax.imshow(img,cmap='gray'); ax.contour(m,levels=[.5],linewidths=1); ax.set_title(title); ax.axis('off')
    fig.tight_layout(); fig.savefig(out,dpi=160); plt.close(fig)

def save_mesh(mask,out,spacing=(1,1,1),elev=20,azim=35):
    v,f,_=mask_to_mesh(mask,spacing); fig=plt.figure(figsize=(6,6)); ax=fig.add_subplot(111,projection='3d'); poly=Poly3DCollection(v[f],alpha=.65); ax.add_collection3d(poly); ax.auto_scale_xyz(v[:,0],v[:,1],v[:,2]); ax.view_init(elev,azim); ax.set_title('Tumor surface reconstruction'); fig.tight_layout(); fig.savefig(out,dpi=160); plt.close(fig)
