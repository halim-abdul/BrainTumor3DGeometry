from neurogeo.synthetic import make_brain_tumor_phantom
from neurogeo.geometry import shape_features
from neurogeo.location import normalized_position

def test_shape_and_position():
    _,brain,tumor,_=make_brain_tumor_phantom((48,48,48))
    f=shape_features(tumor); p=normalized_position(tumor,brain)
    assert f['volume_mm3']>0 and f['surface_area_mm2']>0
    assert 0<=p['right_fraction']<=1
