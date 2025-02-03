import numpy as np
from matplotlib import pyplot as plt
from cans import CaNS
from scipy.interpolate import interp1d
import glob
import re

class DIT(CaNS):
  def __init__(self, dir):
    super().__init__(dir)
    self.generator = type('Generator', (), {})()
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
        elif 'sgstype' in line:
          self.sgs = line.split('=')[1].strip().strip("'")

    self.dx = self.lx / self.nx
    self.dy = self.ly / self.ny
    data = np.loadtxt(self.dir + "grid.out", skiprows=0)
    self.dzc = np.max(data[:, 3])
    self.dzw = np.min(data[:, 3])

  def read_spec(self):
    data = np.loadtxt(self.dir + 'tkespec_0.txt', skiprows=0)
    self.kappa   = data[:, 0]
    self.energy0 = data[:, 1]
    data = np.loadtxt(self.dir + 'tkespec_1.txt', skiprows=0)
    self.energy1 = data[:, 1]
    data = np.loadtxt(self.dir + 'tkespec_2.txt', skiprows=0)
    self.energy2 = data[:, 1]
    #
    data = np.loadtxt(self.dir + 'tkespec_cbc_0.txt', skiprows=0)
    self.generator.kappa   = data[:, 0]
    self.generator.energy0 = data[:, 1]
    data = np.loadtxt(self.dir + 'tkespec_cbc_1.txt', skiprows=0)
    self.generator.energy1 = data[:, 1]
    data = np.loadtxt(self.dir + 'tkespec_cbc_2.txt', skiprows=0)
    self.generator.energy2 = data[:, 1]