from .metrics import metric_bundle
from .geometry import shape_features
from .topology import topology_features
from .location import normalized_position, volume_fraction

def analyze_case(pred,true,brain,spacing=(1,1,1)):
    return {"metrics":metric_bundle(pred,true,spacing),"shape":shape_features(pred,spacing),"topology":topology_features(pred),"position":normalized_position(pred,brain),"tumor_brain_fraction":volume_fraction(pred,brain)}
