import numpy as np
from matplotlib import pyplot as plt
from case import Case
from scipy.interpolate import interp1d
import glob

class CaNS(Case):
  def __init__(self, dir):

    with open(dir + "input.nml", 'r') as f:
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
        elif 'sgstype' in line:
          self.sgs = line.split('=')[1].strip().strip("'")
        elif 'lwm(0:1,1:3)' in line:
          values = line.split('=')[1].strip().split(',')
          self.lwm = [float(val.strip()) for val in values]
          self.lwm = np.reshape(self.lwm, (3, 2))
        elif 'hwm' in line:
          val = line.split('=')[1].strip()
          self.hwm = float(val.strip())

    with open(dir + "input.py", 'r') as f:
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

    with open(dir + "results/stats.txt", 'r') as f:
      line   = f.readline().strip()
      values = [float(num) for num in line.split()]
      self.retau = values[0]
      self.cf = 8.0 * (self.retau / self.reb)**2

    self.dx = self.lx / self.nx
    self.dy = self.ly / self.ny
    data = np.loadtxt(dir + "grid.out", skiprows=0)
    self.dzc = np.max(data[:, 3])
    self.dzw = np.min(data[:, 3])

    data = np.loadtxt(glob.glob(dir + "results/stats-single-point-chan-?????.out")[0], skiprows=0)
    self.yc = data[:, 0]
    self.yf = data[:, 1]
    self.u  = data[:, 2]
    self.v  = data[:, 3]
    self.w  = data[:, 4]
    self.uu = data[:, 5]
    self.vv = data[:, 6]
    self.ww = data[:, 7]
    self.uw = data[:, 8]

  def error(self, ref):
    err = np.zeros(5)
    utau = 2.0*ref.retau/ref.reb
    # velocity
    les = self.u
    func = interp1d(ref.yf, ref.u*utau, axis=0, fill_value="extrapolate")
    dns = func(self.yc)
    index = (self.yc > 0.1) & (self.yc < 1.0)
    err[0] = np.sqrt(np.sum((les[index]-dns[index])**2)/np.sum((dns[index])**2))
    # fluctuation
    for i in range(4):
      if i == 0:
        les = self.uu
        dns = ref.uu*utau**2
        y = self.yc
      elif i == 1:
        les = self.vv
        dns = ref.ww*utau**2
        y = self.yc
      elif i == 2:
        les = self.ww
        dns = ref.vv*utau**2
        y = self.yf
      elif i == 3:
        les = self.uw
        dns = ref.uv*utau**2
        y = self.yf
      func = interp1d(ref.yf, dns, axis=0, fill_value="extrapolate")
      dns = func(y)
      index = (y > 0.1) & (y < 1.0)
      err[i+1] = np.sqrt(np.sum((les[index]-dns[index])**2)/np.sum((dns[index])**2))

    return err