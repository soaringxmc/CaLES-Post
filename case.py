import numpy as np
from matplotlib import pyplot as plt

class Case:
  def __init__(self, dir):
    self.dir       = dir
    self.reb       = None
    self.retau     = None
    self.cf        = None
    self.ub        = None
    self.lx        = None
    self.ly        = None
    self.lz        = None
    self.nx        = None
    self.ny        = None
    self.nz        = None
    self.dx        = None
    self.dy        = None
    self.dzc       = None
    self.dzw       = None
    self.sgs       = None
    self.lwm       = None
    self.hwm       = None
    self.tbeg      = None
    self.tend      = None
    self.u         = None
    self.v         = None
    self.w         = None
    self.uu        = None
    self.vv        = None
    self.ww        = None
    self.uv        = None
    self.uw        = None
    self.vw        = None