from duct import *
from pirozzoli import *
import textwrap

# table of parameters
folders = [ 'DUC_RETAU1000_H0.1_SMAG_NX128_NY80_NZ80/',
            'DUC_RETAU1000_H0.1_SMAG_NX256_NY80_NZ80/',
            'DUC_RETAU1000_H0.1_SMAG_NX512_NY80_NZ80/',
            'DUC_RETAU1000_H0.1_SMAG_NX768_NY120_NZ120/',
            'DUC_RETAU1000_H0.1_SMAG_NX1024_NY160_NZ160/',
            'DUC_RETAU1000_H0.1_SMAG_NX2048_NY320_NZ320/',
            'DUC_RETAU1000_H0.1_DSMAG_NX128_NY80_NZ80/',
            'DUC_RETAU1000_H0.1_DSMAG_NX256_NY80_NZ80/',
            'DUC_RETAU1000_H0.1_DSMAG_NX512_NY80_NZ80/',
            'DUC_RETAU1000_H0.1_DSMAG_NX768_NY120_NZ120/',
            'DUC_RETAU1000_H0.1_DSMAG_NX1024_NY160_NZ160/',
            'DUC_RETAU1000_H0.1_DSMAG_NX2048_NY320_NZ320/']

line = textwrap.dedent("""
              ${nx:<4} \\times {ny:<4} \\times {nz:<4}$ & {dx:<6.3f} & {dy:<6.3f} & {dzc:<6.3f} & {ar:<2.1f} & {sgs:<6} & {retau:<9.1f} & ${cf:.5f} \pm {uncertainty:.2f}\\%$ & {err:>6.2f}\\% & {ett:.1f} \\\\
            """).strip()

with open('tab_params.txt', 'w') as f:
  for i in range(len(folders)):
    les = Duct(folders[i])
    les.read_stats()
    uncertainty = les.uncertainty()
    dns = Pirozzoli('DUC_RETAU1000/')
    dns.read_stats()
    err = (les.cf-dns.cf)/dns.cf
    ett = (les.tend-les.tbeg)*(2.0*dns.retau/dns.reb)
    if les.sgs == 'smag':
      sgs = 'SM'
    elif les.sgs == 'dsmag':
      sgs = 'DSM'
    f.write(line.format(
      nx=les.nx,
      ny=les.ny,
      nz=les.nz,
      dx=les.dx,
      dy=les.dy,
      dzc=les.dzc,
      ar=les.dx/les.dy,
      sgs=sgs,
      retau=les.retau,
      cf=les.cf,
      uncertainty=uncertainty*100,
      err=err * 100,
      ett=ett
    ) + '\n') 