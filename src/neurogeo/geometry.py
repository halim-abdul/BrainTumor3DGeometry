import numpy as np
from skimage.measure import marching_cubes, mesh_surface_area
from scipy.spatial import ConvexHull

def mask_to_mesh(mask, spacing=(1,1,1), level=0.5):
    verts,faces,normals,values=marching_cubes(mask.astype(float),level=level,spacing=spacing)
    return verts,faces,normals

def mesh_area(verts,faces): return float(mesh_surface_area(verts,faces))

def mask_volume(mask,spacing=(1,1,1)): return float(np.sum(mask)*np.prod(spacing))

def sphericity(volume, area, eps=1e-12): return float((np.pi**(1/3)*(6*volume)**(2/3))/(area+eps))

def principal_axes(mask, spacing=(1,1,1)):
    pts=np.argwhere(mask>0)*np.asarray(spacing)
    c=pts.mean(0); q=pts-c
    cov=np.cov(q.T); vals,vecs=np.linalg.eigh(cov); idx=np.argsort(vals)[::-1]
    vals=vals[idx]; vecs=vecs[:,idx]
    return c,vals,vecs

def shape_features(mask,spacing=(1,1,1)):
    v,f,_=mask_to_mesh(mask,spacing); vol=mask_volume(mask,spacing); area=mesh_area(v,f)
    c,eig,axes=principal_axes(mask,spacing)
    elong=float(np.sqrt(eig[0]/max(eig[-1],1e-12)))
    return {"volume_mm3":vol,"surface_area_mm2":area,"sphericity":sphericity(vol,area),"elongation":elong,"centroid_z":float(c[0]),"centroid_y":float(c[1]),"centroid_x":float(c[2])}

def vertex_graph_mean_curvature_proxy(verts,faces):
    n=len(verts); nbr=[set() for _ in range(n)]
    for tri in faces:
        a,b,c=map(int,tri); nbr[a]|={b,c}; nbr[b]|={a,c}; nbr[c]|={a,b}
    h=np.zeros(n)
    for i,ns in enumerate(nbr):
        if ns:
            lap=np.mean(verts[list(ns)],axis=0)-verts[i]
            h[i]=0.5*np.linalg.norm(lap)
    return h
