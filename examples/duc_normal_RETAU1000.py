from cales_post import Pirozzoli, Duct
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
utau = 2.0*dns.retau/dns.reb
plt.plot(dns.centerline.y, dns.centerline.uu/utau**2, color='black', linestyle='-', label='DNS')
for i in range(len(folders)):
  les = Duct(folders[i])
  les.read_stats()
  plt.plot(les.centerline.z, les.centerline.uu/utau**2, linestyle='-', label=f'$\Delta z/h={les.dy:.3f}$')

plt.gca().set_prop_cycle(None)
plt.plot(dns.centerline.y, dns.centerline.vv/utau**2, color='black', linestyle='--')
for i in range(len(folders)):
  les = Duct(folders[i])
  les.read_stats()
  plt.plot(les.centerline.z, les.centerline.ww/utau**2, linestyle='--')

plt.gca().set_prop_cycle(None)
plt.plot(dns.centerline.y, dns.centerline.ww/utau**2, color='black', linestyle='-.')
for i in range(len(folders)):
  les = Duct(folders[i])
  les.read_stats()
  plt.plot(les.centerline.z, les.centerline.vv/utau**2, linestyle='-.')

plt.axvline(x=0.1, color='black', linestyle='--')
plt.legend()
plt.xlabel('$y/h$')
plt.ylabel('$<u_iu_j>^+$')
plt.xlim([0, 1])
plt.ylim([0, 9])
# plt.show()
plt.savefig(f"duc_normal_centerline_SMAG.pdf", format='pdf', bbox_inches='tight')
plt.close()