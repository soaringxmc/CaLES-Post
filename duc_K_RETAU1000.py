from duct import *
from pirozzoli import *
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')  # lines

folders = [
'DUC_RETAU1000_H0.1_SMAG_NX128_NY80_NZ80/',
'DUC_RETAU1000_H0.1_SMAG_NX256_NY80_NZ80/',
'DUC_RETAU1000_H0.1_SMAG_NX512_NY80_NZ80/',
'DUC_RETAU1000_H0.1_SMAG_NX768_NY120_NZ120/',
'DUC_RETAU1000_H0.1_SMAG_NX1024_NY160_NZ160/',
'DUC_RETAU1000_H0.1_SMAG_NX2048_NY320_NZ320/',
'DUC_RETAU1000_H0.1_DSMAG_NX128_NY80_NZ80/',
'DUC_RETAU1000_H0.1_DSMAG_NX256_NY80_NZ80/',
'DUC_RETAU1000_H0.1_DSMAG_NX512_NY80_NZ80/',
'DUC_RETAU1000_H0.1_DSMAG_NX768_NY120_NZ120/',
'DUC_RETAU1000_H0.1_DSMAG_NX1024_NY160_NZ160/',
'DUC_RETAU1000_H0.1_DSMAG_NX2048_NY320_NZ320/',
]

dns = Pirozzoli('DUC_RETAU1000/')
dns.read_stats()
ny = dns.ny
nz = dns.nz
yc = dns.y
zc = dns.z
# print(dns.y[0,:])
# print(dns.z[:,0])

# compute yf and zf
yf = np.zeros((nz  ,ny+1))
zf = np.zeros((nz+1,ny  ))
yf[:,0 ] = -1.0
yf[:,ny] =  0.0
for j in range(1,ny):
  yf[:,j] = 2.0 * yc[:,j-1] - yf[:,j-1]
zf[0 ,:] = -1.0
zf[nz,:] =  0.0
for k in range(1,nz):
  zf[k,:] = 2.0 * zc[k-1,:] - zf[k-1,:]

# compute for dy, dz and dydz
dy = np.zeros_like(yc)
dz = np.zeros_like(zc)
for j in range(0,ny):
  dy[:,j] = yf[:,j+1] - yf[:,j]
for k in range(0,nz):
  dz[k,:] = zf[k+1,:] - zf[k,:]

dydz = dy*dz

# compute k
k_dns = 0.5*(dns.v**2 + dns.w**2) * dydz
area = np.sum(dydz)
k_dns = np.sum(k_dns) / area

print(f"{k_dns:.2E}")

for i in range(len(folders)):
  les = Duct(folders[i])
  les.read_stats()
  k = np.mean(0.5*(les.v**2 + les.w**2))
  # print(f"{k:.2E}")
  print(f"{(k-k_dns)/k_dns:.2%}")