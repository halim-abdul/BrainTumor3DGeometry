import numpy as np
from neurogeo.metrics import dice,iou,sensitivity,specificity,hd95

def test_perfect():
    a=np.zeros((10,10,10),bool); a[2:6,2:6,2:6]=1
    assert abs(dice(a,a)-1)<1e-7
    assert abs(iou(a,a)-1)<1e-7
    assert abs(sensitivity(a,a)-1)<1e-7
    assert abs(specificity(a,a)-1)<1e-7
    assert hd95(a,a)==0
