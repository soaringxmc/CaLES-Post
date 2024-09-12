import numpy as np
from matplotlib import pyplot as plt
from case import Case
import glob

class Pirozzoli(Case):
  def __init__(self, dir):
    
    with open(dir + 'params.txt', 'r') as f:
      line   = f.readline().strip()
      values = [float(num) for num in line.split()]
      self.reb   = values[0]
      self.retau = values[1]
      self.cf = 8.0 * (self.retau / self.reb)**2