import torch
import torch.nn as nn

class Block(nn.Module):
    def __init__(self,a,b):
        super().__init__(); self.net=nn.Sequential(nn.Conv3d(a,b,3,padding=1),nn.InstanceNorm3d(b),nn.LeakyReLU(inplace=True),nn.Conv3d(b,b,3,padding=1),nn.InstanceNorm3d(b),nn.LeakyReLU(inplace=True))
    def forward(self,x): return self.net(x)

class UNet3D(nn.Module):
    def __init__(self,in_channels=4,out_channels=1,base=16):
        super().__init__(); b=base
        self.e1=Block(in_channels,b); self.e2=Block(b,2*b); self.e3=Block(2*b,4*b)
        self.pool=nn.MaxPool3d(2); self.up2=nn.ConvTranspose3d(4*b,2*b,2,2); self.d2=Block(4*b,2*b); self.up1=nn.ConvTranspose3d(2*b,b,2,2); self.d1=Block(2*b,b); self.head=nn.Conv3d(b,out_channels,1)
    def forward(self,x):
        e1=self.e1(x); e2=self.e2(self.pool(e1)); e3=self.e3(self.pool(e2)); d2=self.d2(torch.cat([self.up2(e3),e2],1)); d1=self.d1(torch.cat([self.up1(d2),e1],1)); return self.head(d1)
