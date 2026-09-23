import torch
import torch.nn as nn

class GraphConv(nn.Module):
    def __init__(self,fin,fout): super().__init__(); self.lin=nn.Linear(fin,fout)
    def forward(self,x,adj):
        deg=adj.sum(-1,keepdim=True).clamp_min(1); return self.lin(adj@x/deg)

class MeshBoundaryRefiner(nn.Module):
    """Small educational GNN operating on mesh vertex features and dense adjacency."""
    def __init__(self,fin=6,hidden=32):
        super().__init__(); self.g1=GraphConv(fin,hidden); self.g2=GraphConv(hidden,hidden); self.out=GraphConv(hidden,3); self.act=nn.ReLU()
    def forward(self,x,adj): return self.out(self.act(self.g2(self.act(self.g1(x,adj)),adj)),adj)
