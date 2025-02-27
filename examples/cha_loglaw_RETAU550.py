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
plt.plot(dns.yf*retau, dns.u/utau, label='DNS', color='black')
for i in range(len(folders)):
  les = CaNS(folders[i])
  les.read_stats()
  retau = les.retau
  utau = 2.0*les.retau/les.reb
  plt.plot(les.zc*retau, les.u/utau, label=f'$\Delta z^+={les.dy*dns.retau:.1f}$')

plt.xscale('log')
plt.legend()
plt.xlabel('$y^*$')
plt.ylabel('$U^*$')
plt.xlim([1, 600])
plt.ylim([0, 22])
# plt.show()
plt.savefig(f"cha_loglaw_RETAU550_NOSLIP_SMAG_AR2.pdf", format='pdf', bbox_inches='tight')
plt.close()