import numpy as np
from .case import Case
import glob
import re

class Pirozzoli(Case):
  # spanwise direction is z
  def __init__(self, dir):
    super().__init__(dir)
    self.z = None
    self.y = None
    self.centerline = type('Centerline', (), {})()
    self.diagonal = type('Diagonal', (), {})()

    with open(glob.glob(self.dir + "plotyz_Retau*.dat")[0], 'r') as file:
      for line in file:
        match = re.search(r'I=(\d+), J=(\d+)', line)
        if match:
          self.nz = int(match.group(1))
          self.ny = int(match.group(2))
          break
        
    with open(self.dir + 'params.txt', 'r') as f:
      line   = f.readline().strip()
      values = [float(num) for num in line.split()]
      self.reb   = values[0]
      self.retau = values[1]
      self.cf = 8.0 * (self.retau / self.reb)**2

  def read_stats(self):
      
    data = np.loadtxt(glob.glob(self.dir + "plotyz_Retau*.dat")[0], skiprows=20)
    nz = self.nz
    ny = self.ny
    utau = 2.0*self.retau/self.reb
    self.z  = np.reshape(data[:, 0],(nz,ny),order='C')
    self.y  = np.reshape(data[:, 1],(nz,ny),order='C')
    self.u  = np.reshape(data[:, 2],(nz,ny),order='C')
    self.v  = np.reshape(data[:, 4],(nz,ny),order='C')
    self.w  = np.reshape(data[:, 5],(nz,ny),order='C')
    self.uu = np.reshape(data[:, 6],(nz,ny),order='C')*utau**2
    self.vv = np.reshape(data[:, 7],(nz,ny),order='C')*utau**2
    self.ww = np.reshape(data[:, 8],(nz,ny),order='C')*utau**2
    self.uv = np.reshape(data[:, 9],(nz,ny),order='C')*utau**2
    self.uw = np.reshape(data[:,10],(nz,ny),order='C')*utau**2
    self.vw = np.reshape(data[:,11],(nz,ny),order='C')*utau**2
    data = np.loadtxt(self.dir + "stats-single-point-duct-centerline.out", skiprows=0)
    self.centerline.y  = data[:, 1]
    self.centerline.u  = data[:, 2]
    self.centerline.v  = data[:, 4]
    self.centerline.w  = data[:, 5]
    self.centerline.uu = data[:, 6]*utau**2
    self.centerline.vv = data[:, 7]*utau**2
    self.centerline.ww = data[:, 8]*utau**2
    self.centerline.uv = data[:, 9]*utau**2
    self.centerline.uw = data[:,10]*utau**2
    self.centerline.vw = data[:,11]*utau**2
    data = np.loadtxt(self.dir + "stats-single-point-duct-diagonal.out", skiprows=0)
    self.diagonal.y  = data[:, 1]
    self.diagonal.u  = data[:, 2]
    self.diagonal.v  = data[:, 4]
    self.diagonal.w  = data[:, 5]
    self.diagonal.uu = data[:, 6]*utau**2
    self.diagonal.vv = data[:, 7]*utau**2
    self.diagonal.ww = data[:, 8]*utau**2
    self.diagonal.uv = data[:, 9]*utau**2
    self.diagonal.uw = data[:,10]*utau**2
    self.diagonal.vw = data[:,11]*utau**2