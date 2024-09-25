from cans import *
from moser import *
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')  # lines

folders = [
'scal_weak/imp3d_none/CHA_RETAU550_NX002048_NY384_NZ384_ND001/',
'scal_weak/imp3d_none/CHA_RETAU550_NX004096_NY384_NZ384_ND002/',
'scal_weak/imp3d_none/CHA_RETAU550_NX008192_NY384_NZ384_ND004/',
'scal_weak/imp3d_none/CHA_RETAU550_NX016384_NY384_NZ384_ND008/',
'scal_weak/imp3d_none/CHA_RETAU550_NX032768_NY384_NZ384_ND016/',
'scal_weak/imp3d_none/CHA_RETAU550_NX065536_NY384_NZ384_ND032/',
'scal_weak/imp3d_none/CHA_RETAU550_NX131072_NY384_NZ384_ND064/',
'scal_weak/imp3d_none/CHA_RETAU550_NX262144_NY384_NZ384_ND128/',
'scal_weak/imp3d_none/CHA_RETAU550_NX524288_NY384_NZ384_ND256/',
]
time_elapsed = np.zeros(len(folders))
number_processes = np.zeros(len(folders))
for i in range(len(folders)):
  les = CaNS(folders[i])
  number_processes[i] = les.number_processes()
  time_elapsed[i] = les.elapsed_time()
plt.plot(number_processes, time_elapsed, marker='o', markersize=4)


folders = [
'scal_weak/imp3d_smag/CHA_RETAU550_NX002048_NY384_NZ384_ND001/',
'scal_weak/imp3d_smag/CHA_RETAU550_NX004096_NY384_NZ384_ND002/',
'scal_weak/imp3d_smag/CHA_RETAU550_NX008192_NY384_NZ384_ND004/',
'scal_weak/imp3d_smag/CHA_RETAU550_NX016384_NY384_NZ384_ND008/',
'scal_weak/imp3d_smag/CHA_RETAU550_NX032768_NY384_NZ384_ND016/',
'scal_weak/imp3d_smag/CHA_RETAU550_NX065536_NY384_NZ384_ND032/',
'scal_weak/imp3d_smag/CHA_RETAU550_NX131072_NY384_NZ384_ND064/',
'scal_weak/imp3d_smag/CHA_RETAU550_NX262144_NY384_NZ384_ND128/',
]
time_elapsed = np.zeros(len(folders))
number_processes = np.zeros(len(folders))
for i in range(len(folders)):
  les = CaNS(folders[i])
  number_processes[i] = les.number_processes()
  time_elapsed[i] = les.elapsed_time()
plt.plot(number_processes, time_elapsed, marker='s', markersize=4)


folders = [
'scal_weak/imp3d_dsmag/CHA_RETAU550_NX002048_NY384_NZ384_ND001/',
'scal_weak/imp3d_dsmag/CHA_RETAU550_NX004096_NY384_NZ384_ND002/',
'scal_weak/imp3d_dsmag/CHA_RETAU550_NX008192_NY384_NZ384_ND004/',
'scal_weak/imp3d_dsmag/CHA_RETAU550_NX016384_NY384_NZ384_ND008/',
'scal_weak/imp3d_dsmag/CHA_RETAU550_NX032768_NY384_NZ384_ND016/',
'scal_weak/imp3d_dsmag/CHA_RETAU550_NX065536_NY384_NZ384_ND032/',
'scal_weak/imp3d_dsmag/CHA_RETAU550_NX131072_NY384_NZ384_ND064/',
'scal_weak/imp3d_dsmag/CHA_RETAU550_NX262144_NY384_NZ384_ND128/',
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
plt.ylim([0, 7])
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.1f}'))
plt.legend(['None', 'SM', 'DSM'])
# plt.show()
plt.savefig(f"weak_scal_imp3d.pdf", format='pdf', bbox_inches='tight')
plt.close()