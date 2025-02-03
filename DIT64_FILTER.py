from cans import *
from cbc import *
from dit import *
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')  # lines

folders = [
'DIT64_SMAG_FILTER/',
'DIT64_DSMAG_FILTER/',
]
labels = [
'SM',
'DSM',
]

cbc = DIT('DIT64_SMAG_FILTER/')
cbc.read_spec()
plt.plot(cbc.generator.kappa[1:], cbc.generator.energy0[1:], label='CBC (box-filtered)', color='black')
plt.plot(cbc.generator.kappa[1:], cbc.generator.energy1[1:], color='black')
plt.plot(cbc.generator.kappa[1:], cbc.generator.energy2[1:], color='black')
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
plt.savefig(f"DIT64_FILTER.pdf", format='pdf', bbox_inches='tight')
plt.close()