from cans import *
from moser import *
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')  # lines

folders = [
'CHA_RETAU550_NOSLIP_SMAG_AR2_NX192_NY128_NZ128/',
'CHA_RETAU550_NOSLIP_DSMAG_AR2_NX192_NY128_NZ128/',
]

dns = Moser('CHA_RETAU550/')
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
  plt.plot(les.zf, stress/utau**2, color=color)
  plt.plot(les.zf, -les.uw /utau**2, color=color, label='_nolegend_')
  plt.plot(les.zf, -les.uwm/utau**2, color=color, label='_nolegend_')
  plt.plot(les.zf, -les.uwv/utau**2, color=color, label='_nolegend_')

plt.legend(['$1-y/h$', 'SM', 'DSM'])
plt.xlabel('$y/h$')
plt.ylabel(r'$\tau_{xy}^*$')
plt.xlim([0, 1])
plt.ylim([0, 1])
# plt.show()
plt.savefig(f"cha_balance_RETAU550_NOSLIP_AR2.pdf", format='pdf', bbox_inches='tight')
plt.close()