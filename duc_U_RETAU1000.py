from duct import *
from pirozzoli import *
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')  # lines

folders = [
'DUC_RETAU1000_H0.1_DSMAG_NX512_NY80_NZ80/',
'DUC_RETAU1000_H0.1_DSMAG_NX768_NY120_NZ120/',
'DUC_RETAU1000_H0.1_DSMAG_NX1024_NY160_NZ160/',
'DUC_RETAU1000_H0.1_DSMAG_NX2048_NY320_NZ320/',
]

dns = Pirozzoli('DUC_RETAU1000/')
dns.read_stats()
utau = 2.0*dns.retau/dns.reb
plt.plot(dns.centerline.y, dns.centerline.u/utau, color='black', label='DNS')
for i in range(len(folders)):
  les = Duct(folders[i])
  les.read_stats()
  plt.plot(les.centerline.z, les.centerline.u/utau, label=f'$N_x={les.nx}$')
plt.axvline(x=0.1, color='black', linestyle='--')
plt.legend()
plt.xlabel('$y/h$')
plt.ylabel('$U^+$')
plt.xlim([0, 1])
plt.ylim([0, 25])
# plt.show()
# plt.savefig(f"duc_U_centerline_DSMAG.pdf", format='pdf', bbox_inches='tight')
# plt.close()