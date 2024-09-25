from cans import *
from moser import *
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')  # lines

folders = [
'CHA_RETAU5200_H0.1_DSMAG_AR2_NX128_NY96_NZ64/',
'CHA_RETAU5200_H0.1_DSMAG_AR2_NX256_NY192_NZ128/',
'CHA_RETAU5200_H0.1_DSMAG_AR2_NX512_NY384_NZ256/',
'CHA_SMALL_RETAU5200_H0.1_DSMAG_AR2_NX512_NY384_NZ512/',
]

dns = Moser('CHA_RETAU5200/')
retau = dns.retau
utau = 2.0*dns.retau/dns.reb
plt.plot(dns.yf*retau, dns.u/utau, label='DNS', color='black')
for i in range(len(folders)):
  les = CaNS(folders[i])
  les.read_stats()
  retau = les.retau
  utau = 2.0*les.retau/les.reb
  plt.plot(les.zc*retau, les.u/utau, label=f'$N_z={les.nz}$')
plt.axvline(x=0.1*dns.retau, color='black', linestyle='--')

plt.xscale('log')
plt.legend()
plt.xlabel('$y^*$')
plt.ylabel('$U^*$')
plt.xlim([10, 6000])
plt.ylim([10, 28])
plt.yticks(np.arange(10, 30, 4, dtype=int))
# plt.show()
plt.savefig(f"cha_loglaw_RETAU5200_H0.1_DSMAG_AR2.pdf", format='pdf', bbox_inches='tight')
plt.close()