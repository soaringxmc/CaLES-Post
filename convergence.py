from cans import *
from moser import *
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')  # lines

# table of parameters
folders = [ 'CHA_RETAU5200_H0.1_SMAG_AR1_NX128_NY48_NZ32/',
            'CHA_RETAU5200_H0.1_SMAG_AR1_NX192_NY72_NZ48/',
            'CHA_RETAU5200_H0.1_SMAG_AR1_NX256_NY96_NZ64/',
            'CHA_RETAU5200_H0.1_SMAG_AR1_NX384_NY144_NZ96/',
            'CHA_RETAU5200_H0.1_SMAG_AR1_NX512_NY192_NZ128/',
            'CHA_RETAU5200_H0.1_SMAG_AR1_NX640_NY240_NZ160/',
            'CHA_RETAU5200_H0.1_SMAG_AR1_NX768_NY288_NZ192/',
            'CHA_RETAU5200_H0.1_SMAG_AR1_NX896_NY336_NZ224/',
            'CHA_RETAU5200_H0.1_SMAG_AR1_NX1024_NY384_NZ256/',
            'CHA_RETAU5200_H0.1_SMAG_AR1_NX1536_NY576_NZ256/',
            'CHA_SMALL_RETAU5200_H0.1_SMAG_AR1_NX1024_NY384_NZ512/',
            'CHA_SMALL_RETAU5200_H0.1_SMAG_AR1_NX2048_NY768_NZ1024/',
            'CHA_SMALL_RETAU5200_H0.1_SMAG_AR1_NX3072_NY1152_NZ1536/']

dz = np.zeros(len(folders))
err = np.zeros((len(folders), 6))
for i in range(len(folders)):
  les = CaNS(folders[i])
  dns = Moser('CHA_RETAU5200/')
  dz[i] = les.dy
  err[i,0] = (les.cf-dns.cf)/dns.cf
  err[i,1:6] = les.error(dns)

plt.plot(dz, err[:,0], marker='o', markersize=4)
plt.plot(dz, err[:,1], marker='s', markersize=4)
plt.plot(dz, err[:,2], marker='^', markersize=4)
plt.plot(dz, err[:,3], marker='D', markersize=4)
plt.plot(dz, err[:,4], marker='P', markersize=4)
plt.plot(dz, err[:,5], marker='X', markersize=4)
plt.xscale('log')
# plt.show()
plt.savefig(f"fig02b.pdf", format='pdf', bbox_inches='tight')
plt.close()