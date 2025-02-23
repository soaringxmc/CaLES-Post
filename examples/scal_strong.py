from cales_post import CaNS
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')  # lines

folders = [
'scal_strong/exp_none/CHA_RETAU550_ND001/',
'scal_strong/exp_none/CHA_RETAU550_ND002/',
'scal_strong/exp_none/CHA_RETAU550_ND004/',
'scal_strong/exp_none/CHA_RETAU550_ND008/',
'scal_strong/exp_none/CHA_RETAU550_ND016/',
'scal_strong/exp_none/CHA_RETAU550_ND032/',
'scal_strong/exp_none/CHA_RETAU550_ND064/',
'scal_strong/exp_none/CHA_RETAU550_ND128/',
'scal_strong/exp_none/CHA_RETAU550_ND256/',
]
time_elapsed = np.zeros(len(folders))
number_processes = np.zeros(len(folders))
for i in range(len(folders)):
  les = CaNS(folders[i])
  number_processes[i] = les.number_processes()
  time_elapsed[i] = les.elapsed_time()
x = np.linspace(1, max(number_processes/4), 100)
y = x/2
plt.plot(x, y, linestyle='--', color='black')
plt.plot(number_processes[1:7]/4, time_elapsed[1]/time_elapsed[1:7], marker='o', markersize=4)


folders = [
'scal_strong/imp1d_none/CHA_RETAU550_ND001/',
'scal_strong/imp1d_none/CHA_RETAU550_ND002/',
'scal_strong/imp1d_none/CHA_RETAU550_ND004/',
'scal_strong/imp1d_none/CHA_RETAU550_ND008/',
'scal_strong/imp1d_none/CHA_RETAU550_ND016/',
'scal_strong/imp1d_none/CHA_RETAU550_ND032/',
'scal_strong/imp1d_none/CHA_RETAU550_ND064/',
'scal_strong/imp1d_none/CHA_RETAU550_ND128/',
'scal_strong/imp1d_none/CHA_RETAU550_ND256/',
]
time_elapsed = np.zeros(len(folders))
number_processes = np.zeros(len(folders))
for i in range(len(folders)):
  les = CaNS(folders[i])
  number_processes[i] = les.number_processes()
  time_elapsed[i] = les.elapsed_time()
plt.plot(number_processes[1:7]/4, time_elapsed[1]/time_elapsed[1:7], marker='s', markersize=4)

folders = [
'scal_strong/exp_smag/CHA_RETAU550_ND001/',
'scal_strong/exp_smag/CHA_RETAU550_ND002/',
'scal_strong/exp_smag/CHA_RETAU550_ND004/',
'scal_strong/exp_smag/CHA_RETAU550_ND008/',
'scal_strong/exp_smag/CHA_RETAU550_ND016/',
'scal_strong/exp_smag/CHA_RETAU550_ND032/',
'scal_strong/exp_smag/CHA_RETAU550_ND064/',
'scal_strong/exp_smag/CHA_RETAU550_ND128/',
'scal_strong/exp_smag/CHA_RETAU550_ND256/',
]
time_elapsed = np.zeros(len(folders))
number_processes = np.zeros(len(folders))
for i in range(len(folders)):
  les = CaNS(folders[i])
  number_processes[i] = les.number_processes()
  time_elapsed[i] = les.elapsed_time()
plt.plot(number_processes[1:7]/4, time_elapsed[1]/time_elapsed[1:7], marker='^', markersize=4)

folders = [
'scal_strong/imp1d_smag/CHA_RETAU550_ND001/',
'scal_strong/imp1d_smag/CHA_RETAU550_ND002/',
'scal_strong/imp1d_smag/CHA_RETAU550_ND004/',
'scal_strong/imp1d_smag/CHA_RETAU550_ND008/',
'scal_strong/imp1d_smag/CHA_RETAU550_ND016/',
'scal_strong/imp1d_smag/CHA_RETAU550_ND032/',
'scal_strong/imp1d_smag/CHA_RETAU550_ND064/',
'scal_strong/imp1d_smag/CHA_RETAU550_ND128/',
'scal_strong/imp1d_smag/CHA_RETAU550_ND256/',
]
time_elapsed = np.zeros(len(folders))
number_processes = np.zeros(len(folders))
for i in range(len(folders)):
  les = CaNS(folders[i])
  number_processes[i] = les.number_processes()
  time_elapsed[i] = les.elapsed_time()
plt.plot(number_processes[1:7]/4, time_elapsed[1]/time_elapsed[1:7], marker='d', markersize=4)

plt.xscale('log')
plt.yscale('log')
plt.xlabel('$N_{nodes}$')
plt.ylabel('$T_2/T$')
plt.xlim([1, 100])
plt.ylim([0.5, 100])
plt.legend(['Ideal', 'Explicit DNS', 'Implicit-$y$ DNS', 'Explicit WRLES', 'Implicit-$y$ WRLES'])
# plt.show()
plt.savefig(f"strong_scal_ubuntu.pdf", format='pdf', bbox_inches='tight')
plt.close()