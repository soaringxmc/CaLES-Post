from cans import *
from moser import *
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')  # lines

folders = [
'CHA_RETAU5200_H0.1_SMAG_AR1_NX256_NY96_NZ64/',
'CHA_RETAU5200_H0.1_DSMAG_AR1_NX256_NY96_NZ64/',
]

dns = Moser('CHA_RETAU5200/')
visc = 2.0/dns.reb
x = np.linspace(0, 1, 100)
y = 1 - x
plt.plot(x, y, 'k')
for i in range(len(folders)):
  les = CaNS(folders[i])
  les.read_stats()
  utau = 2.0*les.retau/les.reb
  stress = -les.uw - les.uwm - les.uwv
  color = f'C{i}'
  # plt.plot(les.zf, stress/utau**2, color=color, linestyle='-')
  # plt.plot(les.zf, -les.uw /utau**2, color=color, linestyle='--', label='_nolegend_')
  # plt.plot(les.zf, -les.uwm/utau**2, color=color, linestyle='-.', label='_nolegend_')
  # plt.plot(les.zf, -les.uwv/utau**2, color=color, linestyle=':', label='_nolegend_')

  zf0 = np.insert(les.zf, 0, 0)
  stress0 = np.insert(stress, 0, utau**2)
  uw0 = np.insert(les.uw, 0, 0)
  uwm0 = np.insert(les.uwm, 0, 0)
  uwv0 = np.insert(les.uwv, 0, -utau**2)
  plt.plot(zf0, stress0/utau**2, color=color, linestyle='-')
  plt.plot(zf0, (-uw0-uwm0)/utau**2, color=color, linestyle='--', label='_nolegend_')
  plt.plot(zf0, -uw0 /utau**2, color=color, linestyle='-.', label='_nolegend_')
  plt.plot(zf0, -uwm0/utau**2, color=color, linestyle=':', label='_nolegend_')
  plt.plot(zf0, -uwv0/utau**2, color=color, linestyle='-', label='_nolegend_')


plt.axvline(x=0.1, color='black', linestyle='--')
plt.legend(['$1-y/h$', 'SM', 'DSM'])
plt.xlabel('$y/h$')
plt.ylabel(r'$\tau_{xy}^*$')
plt.xlim([0, 1])
plt.ylim([0, 1])
# plt.show()
plt.savefig(f"cha_balance_RETAU5200_H0.1_AR1.pdf", format='pdf', bbox_inches='tight')
plt.close()