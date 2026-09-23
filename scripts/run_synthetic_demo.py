import argparse, json
from pathlib import Path
import numpy as np
from scipy.ndimage import binary_dilation
from neurogeo.synthetic import make_brain_tumor_phantom
from neurogeo.pde import perona_malik_3d
from neurogeo.report import analyze_case
from neurogeo.visualization import save_orthogonal, save_mesh

p=argparse.ArgumentParser(); p.add_argument('--out',default='outputs/demo'); args=p.parse_args(); out=Path(args.out); out.mkdir(parents=True,exist_ok=True)
imgs,brain,true,_=make_brain_tumor_phantom(); den=perona_malik_3d(imgs[3],n_iter=5)
pred=binary_dilation(true,iterations=1)
rep=analyze_case(pred,true,brain)
(out/'report.json').write_text(json.dumps(rep,indent=2))
save_orthogonal(den,pred,out/'orthogonal.png'); save_mesh(pred,out/'tumor_surface.png')
print(json.dumps(rep,indent=2))
