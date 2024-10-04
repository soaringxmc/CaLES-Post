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
plt.plot(dns.yf, dns.uu/utau**2, label='DNS', color='black')
for i in range(len(folders)):
  les = CaNS(folders[i])
  les.read_stats()
  plt.plot(les.zc, les.uu/utau**2, label=f'$\Delta_z/h={les.dy:.3f}$')

plt.gca().set_prop_cycle(None)
plt.plot(dns.yf, dns.vv/utau**2, color='black')
for i in range(len(folders)):
  les = CaNS(folders[i])
  les.read_stats()
  plt.plot(les.zf, les.ww/utau**2)

plt.gca().set_prop_cycle(None)
plt.plot(dns.yf, dns.ww/utau**2, color='black')
for i in range(len(folders)):
  les = CaNS(folders[i])
  les.read_stats()
  plt.plot(les.zc, les.vv/utau**2)

plt.axvline(x=0.1, color='black', linestyle='--')
plt.legend()
plt.xlabel('$y/h$')
plt.ylabel('$<u_iu_j>^+$')
plt.xlim([0, 1])
plt.ylim([0, 14])
# plt.show()
plt.savefig(f"cha_normal_RETAU5200_H0.1_DSMAG_AR2.pdf", format='pdf', bbox_inches='tight')
plt.close()