from cans import *
from moser import *
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')  # lines

folders = [
'CHA_RETAU550_NOSLIP_DSMAG_AR2_NX192_NY128_NZ128/',
'CHA_RETAU550_NOSLIP_DSMAG_AR2_NX288_NY192_NZ192/',
'CHA_RETAU550_NOSLIP_DSMAG_AR2_NX384_NY256_NZ256/',
'CHA_RETAU550_NOSLIP_DSMAG_AR2_NX576_NY384_NZ384/',
]

dns = Moser('CHA_RETAU550/')
visc = 2.0/dns.reb
for i in range(len(folders)):
  les = CaNS(folders[i])
  les.read_stats()
  plt.plot(les.zc, les.visct/visc, label=f'$\Delta_z^+={les.dy*dns.retau:.1f}$')

plt.legend()
plt.xlabel('$y/h$')
plt.ylabel(r'$\nu_t/\nu$')
plt.xlim([0, 1])
plt.ylim([0, 0.8])
plt.yticks(np.arange(0, 0.81, 0.2))
# plt.show()
plt.savefig(f"cha_visct_RETAU550_NOSLIP_DSMAG_AR2.pdf", format='pdf', bbox_inches='tight')
plt.close()