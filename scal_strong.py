from cans import *
from moser import *
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')  # lines

folders = [
'scal_strong/exp_none/CHA_RETAU550_NX1536_NY1024_NZ1024_ND001/',
'scal_strong/exp_none/CHA_RETAU550_NX1536_NY1024_NZ1024_ND002/',
'scal_strong/exp_none/CHA_RETAU550_NX1536_NY1024_NZ1024_ND004/',
'scal_strong/exp_none/CHA_RETAU550_NX1536_NY1024_NZ1024_ND008/',
'scal_strong/exp_none/CHA_RETAU550_NX1536_NY1024_NZ1024_ND016/',
'scal_strong/exp_none/CHA_RETAU550_NX1536_NY1024_NZ1024_ND032/',
'scal_strong/exp_none/CHA_RETAU550_NX1536_NY1024_NZ1024_ND064/',
'scal_strong/exp_none/CHA_RETAU550_NX1536_NY1024_NZ1024_ND128/',
'scal_strong/exp_none/CHA_RETAU550_NX1536_NY1024_NZ1024_ND256/',
]
time_elapsed = np.zeros(len(folders))
number_processes = np.zeros(len(folders))
for i in range(len(folders)):
  les = CaNS(folders[i])
  number_processes[i] = les.number_processes()
  time_elapsed[i] = les.elapsed_time()
plt.plot(number_processes, time_elapsed, marker='o', markersize=4)


folders = [
'scal_strong/exp_smag/CHA_RETAU550_NX1536_NY1024_NZ1024_ND002/',
'scal_strong/exp_smag/CHA_RETAU550_NX1536_NY1024_NZ1024_ND004/',
'scal_strong/exp_smag/CHA_RETAU550_NX1536_NY1024_NZ1024_ND008/',
'scal_strong/exp_smag/CHA_RETAU550_NX1536_NY1024_NZ1024_ND016/',
'scal_strong/exp_smag/CHA_RETAU550_NX1536_NY1024_NZ1024_ND032/',
'scal_strong/exp_smag/CHA_RETAU550_NX1536_NY1024_NZ1024_ND064/',
'scal_strong/exp_smag/CHA_RETAU550_NX1536_NY1024_NZ1024_ND128/',
'scal_strong/exp_smag/CHA_RETAU550_NX1536_NY1024_NZ1024_ND256/',
]
time_elapsed = np.zeros(len(folders))
number_processes = np.zeros(len(folders))
for i in range(len(folders)):
  les = CaNS(folders[i])
  number_processes[i] = les.number_processes()
  time_elapsed[i] = les.elapsed_time()
plt.plot(number_processes, time_elapsed, marker='s', markersize=4)


folders = [
'scal_strong/exp_dsmag/CHA_RETAU550_NX1536_NY1024_NZ1024_ND004/',
'scal_strong/exp_dsmag/CHA_RETAU550_NX1536_NY1024_NZ1024_ND008/',
'scal_strong/exp_dsmag/CHA_RETAU550_NX1536_NY1024_NZ1024_ND016/',
'scal_strong/exp_dsmag/CHA_RETAU550_NX1536_NY1024_NZ1024_ND032/',
'scal_strong/exp_dsmag/CHA_RETAU550_NX1536_NY1024_NZ1024_ND064/',
'scal_strong/exp_dsmag/CHA_RETAU550_NX1536_NY1024_NZ1024_ND128/',
'scal_strong/exp_dsmag/CHA_RETAU550_NX1536_NY1024_NZ1024_ND256/',
]
time_elapsed = np.zeros(len(folders))
number_processes = np.zeros(len(folders))
for i in range(len(folders)):
  les = CaNS(folders[i])
  number_processes[i] = les.number_processes()
  time_elapsed[i] = les.elapsed_time()
plt.plot(number_processes, time_elapsed, marker='^', markersize=4)

plt.xscale('log')
plt.xlabel('$N_{GPU}$')
plt.ylabel('Iteration wall time (s)')
plt.xlim([3, 1300])
plt.ylim([0, 3])
# plt.legend(['None', 'SM', 'DSM'])
# plt.show()
plt.savefig(f"strong_scal_exp.pdf", format='pdf', bbox_inches='tight')
plt.close()