from cales_post import CaNS, Moser
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')  # lines



folders = [
'CHA_RETAU5200_H0.1_SMAG_AR1_NX128_NY48_NZ32/',
'CHA_RETAU5200_H0.1_SMAG_AR1_NX192_NY72_NZ48/',
'CHA_RETAU5200_H0.1_SMAG_AR1_NX256_NY96_NZ64/',
'CHA_RETAU5200_H0.1_SMAG_AR1_NX384_NY144_NZ96/',
'CHA_RETAU5200_H0.1_SMAG_AR1_NX512_NY192_NZ128/',
'CHA_RETAU5200_H0.1_SMAG_AR1_NX640_NY240_NZ160/',
'CHA_RETAU5200_H0.1_SMAG_AR1_NX768_NY288_NZ192/',
'CHA_RETAU5200_H0.1_SMAG_AR1_NX896_NY336_NZ224/',
'CHA_RETAU5200_H0.1_SMAG_AR1_NX1024_NY384_NZ256/',
'CHA_RETAU5200_H0.1_SMAG_AR1_NX1536_NY576_NZ256/',
'CHA_SMALL_RETAU5200_H0.1_SMAG_AR1_NX1024_NY384_NZ512/',
'CHA_SMALL_RETAU5200_H0.1_SMAG_AR1_NX2048_NY768_NZ1024/',
'CHA_SMALL_RETAU5200_H0.1_SMAG_AR1_NX3072_NY1152_NZ1536/',

# 'CHA_RETAU5200_H0.1_DSMAG_AR1_NX128_NY48_NZ32/',
# 'CHA_RETAU5200_H0.1_DSMAG_AR1_NX192_NY72_NZ48/',
# 'CHA_RETAU5200_H0.1_DSMAG_AR1_NX256_NY96_NZ64/',
# 'CHA_RETAU5200_H0.1_DSMAG_AR1_NX384_NY144_NZ96/',
# 'CHA_RETAU5200_H0.1_DSMAG_AR1_NX512_NY192_NZ128/',
# 'CHA_RETAU5200_H0.1_DSMAG_AR1_NX640_NY240_NZ160/',
# 'CHA_RETAU5200_H0.1_DSMAG_AR1_NX768_NY288_NZ192/',
# 'CHA_RETAU5200_H0.1_DSMAG_AR1_NX896_NY336_NZ224/',
# 'CHA_RETAU5200_H0.1_DSMAG_AR1_NX1024_NY384_NZ256/',
# 'CHA_RETAU5200_H0.1_DSMAG_AR1_NX1536_NY576_NZ256/',
# 'CHA_SMALL_RETAU5200_H0.1_DSMAG_AR1_NX1024_NY384_NZ512/',
# 'CHA_SMALL_RETAU5200_H0.1_DSMAG_AR1_NX2048_NY768_NZ1024/',
# 'CHA_SMALL_RETAU5200_H0.1_DSMAG_AR1_NX3072_NY1152_NZ1536/',

# 'CHA_RETAU5200_H0.1_SMAG_AR2_NX64_NY48_NZ32/',
# 'CHA_RETAU5200_H0.1_SMAG_AR2_NX96_NY72_NZ48/',
# 'CHA_RETAU5200_H0.1_SMAG_AR2_NX128_NY96_NZ64/',
# 'CHA_RETAU5200_H0.1_SMAG_AR2_NX192_NY144_NZ96/',
# 'CHA_RETAU5200_H0.1_SMAG_AR2_NX256_NY192_NZ128/',
# 'CHA_RETAU5200_H0.1_SMAG_AR2_NX320_NY240_NZ160/',
# 'CHA_RETAU5200_H0.1_SMAG_AR2_NX384_NY288_NZ192/',
# 'CHA_RETAU5200_H0.1_SMAG_AR2_NX448_NY336_NZ224/',
# 'CHA_RETAU5200_H0.1_SMAG_AR2_NX512_NY384_NZ256/',
# 'CHA_RETAU5200_H0.1_SMAG_AR2_NX768_NY576_NZ384/',
# 'CHA_SMALL_RETAU5200_H0.1_SMAG_AR2_NX512_NY384_NZ512/',
# 'CHA_SMALL_RETAU5200_H0.1_SMAG_AR2_NX1024_NY768_NZ1024/',
# 'CHA_SMALL_RETAU5200_H0.1_SMAG_AR2_NX1536_NY1152_NZ1536/',

# 'CHA_RETAU5200_H0.1_DSMAG_AR2_NX64_NY48_NZ32/',
# 'CHA_RETAU5200_H0.1_DSMAG_AR2_NX96_NY72_NZ48/',
# 'CHA_RETAU5200_H0.1_DSMAG_AR2_NX128_NY96_NZ64/',
# 'CHA_RETAU5200_H0.1_DSMAG_AR2_NX192_NY144_NZ96/',
# 'CHA_RETAU5200_H0.1_DSMAG_AR2_NX256_NY192_NZ128/',
# 'CHA_RETAU5200_H0.1_DSMAG_AR2_NX320_NY240_NZ160/',
# 'CHA_RETAU5200_H0.1_DSMAG_AR2_NX384_NY288_NZ192/',
# 'CHA_RETAU5200_H0.1_DSMAG_AR2_NX448_NY336_NZ224/',
# 'CHA_RETAU5200_H0.1_DSMAG_AR2_NX512_NY384_NZ256/',
# 'CHA_RETAU5200_H0.1_DSMAG_AR2_NX768_NY576_NZ384/',
# 'CHA_SMALL_RETAU5200_H0.1_DSMAG_AR2_NX512_NY384_NZ512/',
# 'CHA_SMALL_RETAU5200_H0.1_DSMAG_AR2_NX1024_NY768_NZ1024/',
# 'CHA_SMALL_RETAU5200_H0.1_DSMAG_AR2_NX1536_NY1152_NZ1536/',
]

dy = np.zeros(len(folders))
err = np.zeros((len(folders), 6))
for i in range(len(folders)):
  les = CaNS(folders[i])
  dns = Moser('CHA_RETAU5200/')
  dy[i] = les.dy
  les.read_stats()
  err[i,0] = (les.cf-dns.cf)/dns.cf
  err[i,1:6] = les.error(dns)

fig, ax1 = plt.subplots()

ax1.set_xlabel('$\Delta z/h$')
ax1.set_ylabel('Error (\%)')
ax1.set_xscale('log')
ax1.plot(dy, err[:,0]*100, marker='o', markersize=4, markerfacecolor='none', label=r'$C_f$')
ax1.plot(dy, err[:,1]*100, marker='s', markersize=4, markerfacecolor='none', label=r'$U$')
ax1.plot(dy, err[:,2]*100, marker='^', markersize=4, markerfacecolor='none', label=r'$\langle uu \rangle$')
ax1.plot(dy, err[:,4]*100, marker='P', markersize=4, markerfacecolor='none', label=r'$\langle vv \rangle$')
ax1.plot(dy, err[:,3]*100, marker='D', markersize=4, markerfacecolor='none', label=r'$\langle ww \rangle$')
ax1.plot(dy, err[:,5]*100, marker='X', markersize=4, markerfacecolor='none', label=r'$\langle uv \rangle$')
plt.legend()

ax2 = ax1.twiny()
ax2.set_xlabel('$\Delta z^+$')
ax2.set_xscale('log')
ax2.plot(dy*dns.retau, err[:,0]*100, marker='o', markersize=4, markerfacecolor='none')
ax2.plot(dy*dns.retau, err[:,1]*100, marker='s', markersize=4, markerfacecolor='none')
ax2.plot(dy*dns.retau, err[:,2]*100, marker='^', markersize=4, markerfacecolor='none')
ax2.plot(dy*dns.retau, err[:,4]*100, marker='P', markersize=4, markerfacecolor='none')
ax2.plot(dy*dns.retau, err[:,3]*100, marker='D', markersize=4, markerfacecolor='none')
ax2.plot(dy*dns.retau, err[:,5]*100, marker='X', markersize=4, markerfacecolor='none')

plt.ylim([-10, 60])
# plt.show()
plt.savefig(f"convergence_SMAG_AR1.pdf", format='pdf', bbox_inches='tight')
plt.close()