from duct import *
from pirozzoli import *
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')  # lines

folders = [
'DUC_RETAU1000_H0.1_SMAG_NX512_NY80_NZ80/',
'DUC_RETAU1000_H0.1_SMAG_NX768_NY120_NZ120/',
'DUC_RETAU1000_H0.1_SMAG_NX1024_NY160_NZ160/',
'DUC_RETAU1000_H0.1_SMAG_NX2048_NY320_NZ320/',
]

dns = Pirozzoli('DUC_RETAU1000/')
dns.read_stats()
retau = dns.retau
utau = 2.0*dns.retau/dns.reb
plt.plot(dns.centerline.y*retau, dns.centerline.u/utau, color='black', label='DNS')
for i in range(len(folders)):
  les = Duct(folders[i])
  les.read_stats()
  retau = les.retau
  utau = 2.0*les.retau/les.reb
  plt.plot(les.centerline.z*retau, les.centerline.u/utau, label=f'$\Delta_z/h={les.dy:.3f}$')
plt.axvline(x=0.1*dns.retau, color='black', linestyle='--')
plt.xscale('log')
plt.legend()
plt.xlabel('$y^*$')
plt.ylabel('$U^*$')
plt.xlim([1, 1100])
plt.ylim([0, 25])
# plt.show()
plt.savefig(f"duc_loglaw_centerline_SMAG.pdf", format='pdf', bbox_inches='tight')
plt.close()