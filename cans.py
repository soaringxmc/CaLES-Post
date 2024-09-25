import numpy as np
from matplotlib import pyplot as plt
from case import Case
from scipy.interpolate import interp1d
import glob
import re
from scipy.integrate import trapezoid

class CaNS(Case):
  def __init__(self, dir):
    super().__init__(dir)
    self.zc = None
    self.zf = None
    with open(self.dir + "input.nml", 'r') as f:
      lines = f.readlines()
      for line in lines:
        if 'ng(1:3)' in line:
          values = line.split('=')[1].strip().split(',')
          self.nx, self.ny, self.nz = [int(val.strip()) for val in values]
        elif 'l(1:3)' in line:
          values = line.split('=')[1].strip().split(',')
          self.lx, self.ly, self.lz = [float(val.strip()) for val in values]
        elif 'visci' in line:
          val = line.split('=')[1].strip()
          self.reb = 2.0 * float(val.strip())
        elif 'velf' in line:
          values = line.split('=')[1].strip().split(',')
          ubx, uby, ubz = [float(val.strip()) for val in values]
          self.ub = ubx
        elif 'sgstype' in line:
          self.sgs = line.split('=')[1].strip().strip("'")
        elif 'lwm(0:1,1:3)' in line:
          values = line.split('=')[1].strip().split(',')
          self.lwm = [float(val.strip()) for val in values]
          self.lwm = np.reshape(self.lwm, (3, 2))
        elif 'hwm' in line:
          val = line.split('=')[1].strip()
          self.hwm = float(val.strip())

    self.dx = self.lx / self.nx
    self.dy = self.ly / self.ny
    data = np.loadtxt(self.dir + "grid.out", skiprows=0)
    self.dzc = np.max(data[:, 3])
    self.dzw = np.min(data[:, 3])

  def stats_input(self):
    with open(self.dir + "input.py", 'r') as f:
      lines = f.readlines()
      for line in lines:
        if 'tbeg' in line:
          val = line.split('=')[1].strip()
          self.tbeg = float(val.strip())
        elif 'tend' in line:
          val = line.split('=')[1].strip()
          self.tend = float(val.strip())
        elif 'fldstp' in line:
          val = line.split('=')[1].strip()
          self.fldstp = int(val.strip())

  def forcing(self):
    data = np.loadtxt(self.dir + 'forcing.out', skiprows=0)
    t, ind = np.unique(data[:,0], return_index=True) # this requires the same number of tasks used for restart
    dpdx_arr = data[ind,1][np.where((t>self.tbeg) & (t<self.tend))]
    return dpdx_arr

  def stats(self):
    dpdx_arr = self.forcing()
    dpdx = -np.average(dpdx_arr)
    h = self.lz/2.0
    visc = 2.0/self.reb
    utau = np.sqrt(dpdx*h)
    retau = utau*h/visc
    dnu   = visc/utau
    cf    = utau**2/(0.5*self.ub**2)
    np.savetxt(self.dir + "results/stats_new.txt",np.c_[retau,utau,dnu])
    # print("Pressure gradient = ", dpdx)
    # print("u_tau/u_bulk = ", utau/self.ub)
    # print("dnu/h        = ", dnu/h)
    # print("Friction Reynolds number = ", retau)

  def uncertainty(self):
    dpdx_arr = self.forcing()
    def uncertainty(x, M):
      N = np.floor(len(x)/M)*M
      K = int(N/M)
      x_ave = np.zeros(K)
      mu_hat = np.mean(x)
      for k in range(K):
        x_ave[k] = np.mean(x[k*M:(k+1)*M]-mu_hat)
      s0 = sum(x_ave**2)
      s1 = sum(x_ave[0:K-1]*x_ave[1:K])
      var2 = 1/((K-1)*(K-2))*(s0+2*s1)
      return s1/s0, np.sqrt(var2)/mu_hat
    
    x = -dpdx_arr
    M = 1
    while True:
      ratio, uncertainty_val = uncertainty(x, M)
      if ratio > 0.47 and ratio < 0.53:
        break
      M = M + 1
    print(M,ratio,uncertainty_val)
    return uncertainty_val


  def read_stats(self):
    with open(self.dir + "results/stats.txt", 'r') as f:
      line   = f.readline().strip()
      values = [float(num) for num in line.split()]
      self.retau = values[0]
      self.cf = 8.0 * (self.retau / self.reb)**2

    data = np.loadtxt(glob.glob(self.dir + "results/stats-single-point-chan-?????.out")[0], skiprows=0)
    self.zc = data[:len(data)//2, 0]
    self.zf = data[:len(data)//2, 1]
    self.u  = data[:len(data)//2, 2]
    self.v  = data[:len(data)//2, 3]
    self.w  = data[:len(data)//2, 4]
    self.uu = data[:len(data)//2, 5]
    self.vv = data[:len(data)//2, 6]
    self.ww = data[:len(data)//2, 7]
    self.uw = data[:len(data)//2, 8]

  def error(self, ref):
    err = np.zeros(5)
    # velocity
    les = self.u
    func = interp1d(ref.yf, ref.u, axis=0, fill_value="extrapolate")
    dns = func(self.zc)
    index = self.zc > 0.1
    zc = self.zc[index]
    dns = dns[index]
    les = les[index]
    err[0] = np.sqrt(trapezoid((les-dns)**2,zc)) / trapezoid(dns,zc)
    # fluctuation
    for i in range(4):
      if i == 0:
        les = self.uu
        dns = ref.uu
        z = self.zc
      elif i == 1:
        les = self.vv
        dns = ref.ww
        z = self.zc
      elif i == 2:
        les = self.ww
        dns = ref.vv
        z = self.zf
      elif i == 3:
        les = self.uw*(-1) # to obtain positive errors
        dns = ref.uv*(-1)
        z = self.zf
      func = interp1d(ref.yf, dns, axis=0, fill_value="extrapolate")
      dns = func(z)
      index = (z > 0.1)
      z = z[index]
      dns = dns[index]
      les = les[index]
      err[i+1] = np.sqrt(trapezoid((les-dns)**2,z)) / trapezoid(dns,z)
    return err
  
  def elapsed_time(self):
    average_times = []
    with open(self.dir + 'output', 'r') as file:
      for line in file:
        if 'Avrg, min & max elapsed time:' in line:
          next_line = next(file)
          values = next_line.split()
          avrg_time = float(values[0])
          average_times.append(avrg_time)
    overall_average = sum(average_times[1:-1]) / (len(average_times)-2)
    return overall_average
  
  def number_processes(self):
    with open(self.dir + 'job.sh', 'r') as file:
        for line in file:
            if not line.startswith('#'):
                match = re.search(r'-n\s+(\d+)', line)
                if match:
                    return int(match.group(1))
    return None