import numpy as np
from matplotlib import pyplot as plt
from .case import Case
import glob

class Moser(Case):
  # spanwise direction is z
  def __init__(self, dir):
    super().__init__(dir)
    self.yf        = None
    with open(glob.glob(self.dir + "LM_Channel_????_mean_prof.dat")[0], 'r') as f:
      lines = f.readlines()
      for line in lines:
        if '%  Re_tau' in line:
          val = line.split('=')[1].strip()
          self.retau = float(val.strip())
        if '%  Kinematic Viscosity' in line:
          val = line.split('=')[1].strip()
          nu = float(val.strip())
          self.reb = 2.0 / nu # based on 2h
    self.cf = 8.0 * (self.retau / self.reb)**2

    utau = 2.0*self.retau/self.reb
    data = np.loadtxt(glob.glob(self.dir + "LM_Channel_????_mean_prof.dat")[0], skiprows=72)
    self.yf = data[:, 0]
    self.u  = data[:, 2]*utau
    data = np.loadtxt(glob.glob(self.dir + "LM_Channel_????_vel_fluc_prof.dat")[0], skiprows=75)
    self.uu = data[:, 2]*utau**2
    self.vv = data[:, 3]*utau**2
    self.ww = data[:, 4]*utau**2
    self.uv = data[:, 5]*utau**2
    self.uw = data[:, 6]*utau**2
    self.vw = data[:, 7]*utau**2