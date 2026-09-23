import torch
import torch.nn.functional as F

def soft_dice_loss(logits,target,eps=1e-6):
    p=torch.sigmoid(logits); t=target.float(); dims=tuple(range(2,p.ndim)); inter=(p*t).sum(dims); den=p.sum(dims)+t.sum(dims); return 1-((2*inter+eps)/(den+eps)).mean()

def bce_dice_loss(logits,target,alpha=0.5):
    return alpha*F.binary_cross_entropy_with_logits(logits,target.float())+(1-alpha)*soft_dice_loss(logits,target)

def total_variation_3d(prob):
    dz=(prob[:,:,1:]-prob[:,:,:-1]).abs().mean(); dy=(prob[:,:,:,1:]-prob[:,:,:,:-1]).abs().mean(); dx=(prob[:,:,:,:,1:]-prob[:,:,:,:,:-1]).abs().mean(); return dx+dy+dz
