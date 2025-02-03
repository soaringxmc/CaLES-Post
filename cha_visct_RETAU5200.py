from cans import *
from moser import *
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')  # lines

folders = [
'CHA_RETAU5200_H0.1_SMAG_AR1_NX256_NY96_NZ64/',
'CHA_RETAU5200_H0.1_SMAG_AR1_NX512_NY192_NZ128/',
'CHA_RETAU5200_H0.1_SMAG_AR1_NX1024_NY384_NZ256/',
'CHA_SMALL_RETAU5200_H0.1_SMAG_AR1_NX1024_NY384_NZ512/',
]

dns = Moser('CHA_RETAU5200/')
visc = 2.0/dns.reb
for i in range(len(folders)):
  les = CaNS(folders[i])
  les.read_stats()
  plt.plot(les.zc, les.visct/visc, label=f'$\Delta z/h={les.dy:.3f}$')

plt.axvline(x=0.1, color='black', linestyle='--')
plt.legend()
plt.xlabel('$y/h$')
plt.ylabel(r'$\nu_t/\nu$')
plt.xlim([0, 1])
plt.ylim([0, 14])
# plt.yticks(np.arange(0, 0.81, 0.2))
# plt.show()
plt.savefig(f"cha_visct_RETAU5200_H0.1_SMAG_AR1.pdf", format='pdf', bbox_inches='tight')
plt.close()