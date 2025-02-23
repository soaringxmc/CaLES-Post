import numpy as np
from matplotlib import pyplot as plt
from .cans import CaNS
from scipy.interpolate import interp1d
import glob
import re

class Duct(CaNS):
  def __init__(self, dir):
    super().__init__(dir)
    self.y = None
    self.z = None
    self.centerline = type('Centerline', (), {})()
    self.diagonal = type('Diagonal', (), {})()

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

    with open(self.dir + "results/stats.txt", 'r') as f:
      line   = f.readline().strip()
      values = [float(num) for num in line.split()]
      self.retau = values[0]
      self.cf = 8.0 * (self.retau / self.reb)**2

  def read_stats(self):
    data = np.loadtxt(glob.glob(self.dir + "results/stats-single-point-duct-?????.out")[0], skiprows=1)
    ny = self.ny
    nz = self.nz
    self.y  = np.reshape(data[:, 0],(nz,ny),order='C')
    self.z  = np.reshape(data[:, 1],(nz,ny),order='C')
    self.u  = np.reshape(data[:, 2],(nz,ny),order='C')
    self.v  = np.reshape(data[:, 3],(nz,ny),order='C')
    self.w  = np.reshape(data[:, 4],(nz,ny),order='C')
    self.uu = np.reshape(data[:, 5],(nz,ny),order='C')
    self.vv = np.reshape(data[:, 6],(nz,ny),order='C')
    self.ww = np.reshape(data[:, 7],(nz,ny),order='C')
    self.uv = np.reshape(data[:, 8],(nz,ny),order='C')
    self.uw = np.reshape(data[:, 9],(nz,ny),order='C')
    self.vw = np.reshape(data[:,10],(nz,ny),order='C')
    data = np.loadtxt(glob.glob(self.dir + "results/stats-single-point-duct-centerline-?????.out")[0], skiprows=0)
    self.centerline.z  = data[:, 0]
    self.centerline.u  = data[:, 1]
    self.centerline.v  = data[:, 2]
    self.centerline.w  = data[:, 3]
    self.centerline.uu = data[:, 4]
    self.centerline.vv = data[:, 5]
    self.centerline.ww = data[:, 6]
    self.centerline.uv = data[:, 7]
    self.centerline.uw = data[:, 8]
    self.centerline.vw = data[:, 9]
    data = np.loadtxt(glob.glob(self.dir + "results/stats-single-point-duct-diagonal-?????.out")[0], skiprows=0)
    self.diagonal.z  = data[:, 0]
    self.diagonal.u  = data[:, 1]
    self.diagonal.v  = data[:, 2]
    self.diagonal.w  = data[:, 3]
    self.diagonal.uu = data[:, 4]
    self.diagonal.vv = data[:, 5]
    self.diagonal.ww = data[:, 6]
    self.diagonal.uv = data[:, 7]
    self.diagonal.uw = data[:, 8]
    self.diagonal.vw = data[:, 9]