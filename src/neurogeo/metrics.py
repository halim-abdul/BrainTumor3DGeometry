import numpy as np
from scipy.ndimage import binary_erosion
from scipy.spatial import cKDTree

def confusion(pred, true):
    p=np.asarray(pred).astype(bool); t=np.asarray(true).astype(bool)
    tp=np.logical_and(p,t).sum(); tn=np.logical_and(~p,~t).sum(); fp=np.logical_and(p,~t).sum(); fn=np.logical_and(~p,t).sum()
    return tp,tn,fp,fn

def dice(pred,true,eps=1e-8):
    p=np.asarray(pred).astype(bool); t=np.asarray(true).astype(bool)
    return (2*np.logical_and(p,t).sum()+eps)/(p.sum()+t.sum()+eps)

def iou(pred,true,eps=1e-8):
    p=np.asarray(pred).astype(bool); t=np.asarray(true).astype(bool)
    return (np.logical_and(p,t).sum()+eps)/(np.logical_or(p,t).sum()+eps)

def sensitivity(pred,true,eps=1e-8):
    tp,_,_,fn=confusion(pred,true); return (tp+eps)/(tp+fn+eps)

def specificity(pred,true,eps=1e-8):
    _,tn,fp,_=confusion(pred,true); return (tn+eps)/(tn+fp+eps)

def precision(pred,true,eps=1e-8):
    tp,_,fp,_=confusion(pred,true); return (tp+eps)/(tp+fp+eps)

def _surface(mask):
    m=np.asarray(mask).astype(bool); return np.argwhere(m ^ binary_erosion(m))

def surface_distances(pred,true,spacing=(1,1,1)):
    a=_surface(pred)*np.asarray(spacing); b=_surface(true)*np.asarray(spacing)
    if len(a)==0 or len(b)==0: return np.array([np.inf]),np.array([np.inf])
    da=cKDTree(b).query(a,k=1)[0]; db=cKDTree(a).query(b,k=1)[0]
    return da,db

def hd95(pred,true,spacing=(1,1,1)):
    a,b=surface_distances(pred,true,spacing); return float(np.percentile(np.r_[a,b],95))

def assd(pred,true,spacing=(1,1,1)):
    a,b=surface_distances(pred,true,spacing); return float(np.mean(np.r_[a,b]))

def metric_bundle(pred,true,spacing=(1,1,1)):
    return {"dice":dice(pred,true),"iou":iou(pred,true),"sensitivity":sensitivity(pred,true),"specificity":specificity(pred,true),"precision":precision(pred,true),"hd95":hd95(pred,true,spacing),"assd":assd(pred,true,spacing)}
