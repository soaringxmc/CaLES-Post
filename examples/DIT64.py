from cales_post import DIT, CBC
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')  # lines

folders = [
'DIT64_SMAG/',
'DIT64_DSMAG/',
]
labels = [
'SM',
'DSM',
]

cbc = CBC('DNS/')
plt.plot(cbc.kappa, cbc.energy0, label='CBC', color='black')
plt.plot(cbc.kappa, cbc.energy1, color='black')
plt.plot(cbc.kappa, cbc.energy2, color='black')
for i in range(len(folders)):
  les = DIT(folders[i])
  les.read_spec()
  plt.plot(les.kappa[1:], les.energy0[1:], label=labels[i], color=f'C{i}')
  plt.plot(les.kappa[1:], les.energy1[1:], color=f'C{i}')
  plt.plot(les.kappa[1:], les.energy2[1:], color=f'C{i}')
plt.axvline(x=2*np.pi/(2*les.lx/les.nx), color='black', linestyle='--')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.xlabel('$\kappa (1/m)$')
plt.ylabel('$E(\kappa) (m^3/s^2)$')
plt.xlim([10, 1000])
plt.ylim([1e-6, 1e-3])
# plt.show()
plt.savefig(f"DIT64.pdf", format='pdf', bbox_inches='tight')
plt.close()