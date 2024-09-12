import numpy as np
from matplotlib import pyplot as plt
from case import Case
import glob

class Moser(Case):
  def __init__(self, dir):
    
    with open(glob.glob(dir + "LM_Channel_????_mean_prof.dat")[0], 'r') as f:
      lines = f.readlines()
      for line in lines:
        if '%  Re_tau' in line:
          val = line.split('=')[1].strip()
          self.retau = float(val.strip())
        if '%  Kinematic Viscosity' in line:
          val = line.split('=')[1].strip()
          nu = float(val.strip())
          self.reb = 2.0 / nu
    self.cf = 8.0 * (self.retau / self.reb)**2

    data = np.loadtxt(glob.glob(dir + "LM_Channel_????_mean_prof.dat")[0], skiprows=72)
    self.yf = data[:, 0]
    self.u  = data[:, 2]
    data = np.loadtxt(glob.glob(dir + "LM_Channel_????_vel_fluc_prof.dat")[0], skiprows=75)
    self.uu = data[:, 2]
    self.vv = data[:, 3]
    self.ww = data[:, 4]
    self.uv = data[:, 5]
    self.uw = data[:, 6]
    self.vw = data[:, 7]