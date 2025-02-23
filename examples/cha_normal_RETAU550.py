from cales_post import CaNS, Moser
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')  # lines

folders = [
'CHA_RETAU550_NOSLIP_SMAG_AR2_NX192_NY128_NZ128/',
'CHA_RETAU550_NOSLIP_SMAG_AR2_NX288_NY192_NZ192/',
'CHA_RETAU550_NOSLIP_SMAG_AR2_NX384_NY256_NZ256/',
'CHA_RETAU550_NOSLIP_SMAG_AR2_NX576_NY384_NZ384/',
]
dns = Moser('CHA_RETAU550/')
retau = dns.retau
utau = 2.0*dns.retau/dns.reb

plt.plot(dns.yf, dns.uu/utau**2, label='DNS', color='black', linestyle='-')
for i in range(len(folders)):
  les = CaNS(folders[i])
  les.read_stats()
  plt.plot(les.zc, les.uu/utau**2, label=f'$\Delta z^+={les.dy*retau:.1f}$', linestyle='-')

plt.gca().set_prop_cycle(None)
plt.plot(dns.yf, dns.vv/utau**2, color='black', linestyle='--')
for i in range(len(folders)):
  les = CaNS(folders[i])
  les.read_stats()
  plt.plot(les.zf, les.ww/utau**2, linestyle='--')

plt.gca().set_prop_cycle(None)
plt.plot(dns.yf, dns.ww/utau**2, color='black', linestyle='-.')
for i in range(len(folders)):
  les = CaNS(folders[i])
  les.read_stats()
  plt.plot(les.zc, les.vv/utau**2, linestyle='-.')

plt.legend()
plt.xlabel('$y/h$')
plt.ylabel('$<u_iu_j>^+$')
plt.xlim([0, 1])
plt.ylim([0, 10])
# plt.show()
plt.savefig(f"cha_normal_RETAU550_NOSLIP_SMAG_AR2.pdf", format='pdf', bbox_inches='tight')
plt.close()