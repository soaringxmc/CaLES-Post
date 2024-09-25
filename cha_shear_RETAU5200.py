from cans import *
from moser import *
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')  # lines

folders = [
'CHA_RETAU5200_H0.1_SMAG_AR2_NX128_NY96_NZ64/',
'CHA_RETAU5200_H0.1_SMAG_AR2_NX256_NY192_NZ128/',
'CHA_RETAU5200_H0.1_SMAG_AR2_NX512_NY384_NZ256/',
'CHA_SMALL_RETAU5200_H0.1_SMAG_AR2_NX512_NY384_NZ512/',
]
dns = Moser('CHA_RETAU5200/')
utau = 2.0*dns.retau/dns.reb
plt.plot(dns.yf, dns.uv/utau**2, label='DNS', color='black')
for i in range(len(folders)):
  les = CaNS(folders[i])
  les.read_stats()
  plt.plot(les.zf, les.uw/utau**2, label=f'$N_z={les.nz}$')

plt.axvline(x=0.1, color='black', linestyle='--')
plt.legend()
plt.xlabel('$y/h$')
plt.ylabel('$<uv>^+$')
plt.xlim([ 0, 1])
plt.ylim([-1, 0])
# plt.show()
plt.savefig(f"cha_shear_RETAU5200_H0.1_SMAG_AR2.pdf", format='pdf', bbox_inches='tight')
plt.close()