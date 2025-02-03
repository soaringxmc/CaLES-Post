import numpy as np
from matplotlib import pyplot as plt
from case import Case
from scipy.interpolate import interp1d
import glob
import re

class CBC(Case):
  def __init__(self, dir):
    super().__init__(dir)
    self.generator = type('Generator', (), {})()
    #
    data = np.loadtxt(self.dir + 'cbc_spectrum_0.txt', skiprows=0)
    self.kappa   = data[:, 0]*100
    self.energy0 = data[:, 1]*1.0e-06
    data = np.loadtxt(self.dir + 'cbc_spectrum_1.txt', skiprows=0)
    self.energy1 = data[:, 1]*1.0e-06
    data = np.loadtxt(self.dir + 'cbc_spectrum_2.txt', skiprows=0)
    self.energy2 = data[:, 1]*1.0e-06
    #
    data = np.loadtxt(self.dir + 'tkespec_cbc_dns_0.txt', skiprows=0)
    self.generator.kappa   = data[:, 0]
    self.generator.energy0 = data[:, 1]
    data = np.loadtxt(self.dir + 'tkespec_cbc_dns_1.txt', skiprows=0)
    self.generator.energy1 = data[:, 1]
    data = np.loadtxt(self.dir + 'tkespec_cbc_dns_2.txt', skiprows=0)
    self.generator.energy2 = data[:, 1]