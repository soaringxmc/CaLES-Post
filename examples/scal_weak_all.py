from cales_post import CaNS
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')  # lines

folders = [
'scal_weak/imp3d_none/CHA_RETAU550_ND001/',
'scal_weak/imp3d_none/CHA_RETAU550_ND002/',
'scal_weak/imp3d_none/CHA_RETAU550_ND004/',
'scal_weak/imp3d_none/CHA_RETAU550_ND008/',
'scal_weak/imp3d_none/CHA_RETAU550_ND016/',
'scal_weak/imp3d_none/CHA_RETAU550_ND032/',
'scal_weak/imp3d_none/CHA_RETAU550_ND064/',
'scal_weak/imp3d_none/CHA_RETAU550_ND128/',
'scal_weak/imp3d_none/CHA_RETAU550_ND256/',
]
time_elapsed = np.zeros(len(folders))
number_processes = np.zeros(len(folders))
for i in range(len(folders)):
  les = CaNS(folders[i])
  number_processes[i] = les.number_processes()
  time_elapsed[i] = les.elapsed_time()
x = np.linspace(1, max(number_processes/4), 100)
y = x/x
plt.plot(x, y, linestyle='--', color='black')
plt.plot(number_processes[1:7]/4, time_elapsed[1:7]/time_elapsed[1], marker='o', markersize=4)


folders = [
'scal_weak/imp3d_smag/CHA_RETAU550_ND001/',
'scal_weak/imp3d_smag/CHA_RETAU550_ND002/',
'scal_weak/imp3d_smag/CHA_RETAU550_ND004/',
'scal_weak/imp3d_smag/CHA_RETAU550_ND008/',
'scal_weak/imp3d_smag/CHA_RETAU550_ND016/',
'scal_weak/imp3d_smag/CHA_RETAU550_ND032/',
'scal_weak/imp3d_smag/CHA_RETAU550_ND064/',
'scal_weak/imp3d_smag/CHA_RETAU550_ND128/',
]
time_elapsed = np.zeros(len(folders))
number_processes = np.zeros(len(folders))
for i in range(len(folders)):
  les = CaNS(folders[i])
  number_processes[i] = les.number_processes()
  time_elapsed[i] = les.elapsed_time()
plt.plot(number_processes[1:7]/4, time_elapsed[1:7]/time_elapsed[1], marker='s', markersize=4)


folders = [
'scal_weak/imp3d_dsmag/CHA_RETAU550_ND001/',
'scal_weak/imp3d_dsmag/CHA_RETAU550_ND002/',
'scal_weak/imp3d_dsmag/CHA_RETAU550_ND004/',
'scal_weak/imp3d_dsmag/CHA_RETAU550_ND008/',
'scal_weak/imp3d_dsmag/CHA_RETAU550_ND016/',
'scal_weak/imp3d_dsmag/CHA_RETAU550_ND032/',
'scal_weak/imp3d_dsmag/CHA_RETAU550_ND064/',
'scal_weak/imp3d_dsmag/CHA_RETAU550_ND128/',
]
time_elapsed = np.zeros(len(folders))
number_processes = np.zeros(len(folders))
for i in range(len(folders)):
  les = CaNS(folders[i])
  number_processes[i] = les.number_processes()
  time_elapsed[i] = les.elapsed_time()
plt.plot(number_processes[1:7]/4, time_elapsed[1:7]/time_elapsed[1], marker='^', markersize=4)

plt.xscale('log')
plt.xlabel('$N_{node}$')
plt.ylabel('$T/T_2$')
plt.xlim([1, 100])
plt.ylim([0, 5])
plt.yticks(np.arange(0, 6, 1))
plt.legend(['Ideal','None', 'SM', 'DSM'])
plt.show()
# plt.savefig(f"weak_scal_imp3d.pdf", format='pdf', bbox_inches='tight')
plt.close()