import argparse, numpy as np
from neurogeo.metrics import metric_bundle
p=argparse.ArgumentParser(); p.add_argument('pred'); p.add_argument('true'); p.add_argument('--spacing',nargs=3,type=float,default=(1,1,1)); a=p.parse_args()
print(metric_bundle(np.load(a.pred),np.load(a.true),tuple(a.spacing)))
