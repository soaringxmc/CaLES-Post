from cans import *
from moser import *
import textwrap

# table of parameters
folders = [ 'CHA_RETAU5200_H0.1_SMAG_AR1_NX128_NY48_NZ32/',
            'CHA_RETAU5200_H0.1_SMAG_AR1_NX192_NY72_NZ48/',
            'CHA_RETAU5200_H0.1_SMAG_AR1_NX256_NY96_NZ64/',
            'CHA_RETAU5200_H0.1_SMAG_AR1_NX384_NY144_NZ96/',
            'CHA_RETAU5200_H0.1_SMAG_AR1_NX512_NY192_NZ128/',
            'CHA_RETAU5200_H0.1_SMAG_AR1_NX640_NY240_NZ160/',
            'CHA_RETAU5200_H0.1_SMAG_AR1_NX768_NY288_NZ192/',
            'CHA_RETAU5200_H0.1_SMAG_AR1_NX896_NY336_NZ224/',
            'CHA_RETAU5200_H0.1_SMAG_AR1_NX1024_NY384_NZ256/',
            'CHA_RETAU5200_H0.1_SMAG_AR1_NX1536_NY576_NZ256/',
            'CHA_SMALL_RETAU5200_H0.1_SMAG_AR1_NX1024_NY384_NZ512/',
            'CHA_SMALL_RETAU5200_H0.1_SMAG_AR1_NX2048_NY768_NZ1024/',
            'CHA_SMALL_RETAU5200_H0.1_SMAG_AR1_NX3072_NY1152_NZ1536/',
            'CHA_RETAU5200_H0.1_DSMAG_AR1_NX128_NY48_NZ32/',
            'CHA_RETAU5200_H0.1_DSMAG_AR1_NX192_NY72_NZ48/',
            'CHA_RETAU5200_H0.1_DSMAG_AR1_NX256_NY96_NZ64/',
            'CHA_RETAU5200_H0.1_DSMAG_AR1_NX384_NY144_NZ96/',
            'CHA_RETAU5200_H0.1_DSMAG_AR1_NX512_NY192_NZ128/',
            'CHA_RETAU5200_H0.1_DSMAG_AR1_NX640_NY240_NZ160/',
            'CHA_RETAU5200_H0.1_DSMAG_AR1_NX768_NY288_NZ192/',
            'CHA_RETAU5200_H0.1_DSMAG_AR1_NX896_NY336_NZ224/',
            'CHA_RETAU5200_H0.1_DSMAG_AR1_NX1024_NY384_NZ256/',
            'CHA_RETAU5200_H0.1_DSMAG_AR1_NX1536_NY576_NZ256/',
            'CHA_SMALL_RETAU5200_H0.1_DSMAG_AR1_NX1024_NY384_NZ512/',
            'CHA_SMALL_RETAU5200_H0.1_DSMAG_AR1_NX2048_NY768_NZ1024/',
            'CHA_SMALL_RETAU5200_H0.1_DSMAG_AR1_NX3072_NY1152_NZ1536/',
            'CHA_RETAU5200_H0.1_SMAG_AR2_NX64_NY48_NZ32/',
            'CHA_RETAU5200_H0.1_SMAG_AR2_NX96_NY72_NZ48/',
            'CHA_RETAU5200_H0.1_SMAG_AR2_NX128_NY96_NZ64/',
            'CHA_RETAU5200_H0.1_SMAG_AR2_NX192_NY144_NZ96/',
            'CHA_RETAU5200_H0.1_SMAG_AR2_NX256_NY192_NZ128/',
            'CHA_RETAU5200_H0.1_SMAG_AR2_NX320_NY240_NZ160/',
            'CHA_RETAU5200_H0.1_SMAG_AR2_NX384_NY288_NZ192/',
            'CHA_RETAU5200_H0.1_SMAG_AR2_NX448_NY336_NZ224/',
            'CHA_RETAU5200_H0.1_SMAG_AR2_NX512_NY384_NZ256/',
            'CHA_RETAU5200_H0.1_SMAG_AR2_NX768_NY576_NZ384/',
            'CHA_SMALL_RETAU5200_H0.1_SMAG_AR2_NX512_NY384_NZ512/',
            'CHA_SMALL_RETAU5200_H0.1_SMAG_AR2_NX1024_NY768_NZ1024/',
            'CHA_SMALL_RETAU5200_H0.1_SMAG_AR2_NX1536_NY1152_NZ1536/',
            'CHA_RETAU5200_H0.1_DSMAG_AR2_NX64_NY48_NZ32/',
            'CHA_RETAU5200_H0.1_DSMAG_AR2_NX96_NY72_NZ48/',
            'CHA_RETAU5200_H0.1_DSMAG_AR2_NX128_NY96_NZ64/',
            'CHA_RETAU5200_H0.1_DSMAG_AR2_NX192_NY144_NZ96/',
            'CHA_RETAU5200_H0.1_DSMAG_AR2_NX256_NY192_NZ128/',
            'CHA_RETAU5200_H0.1_DSMAG_AR2_NX320_NY240_NZ160/',
            'CHA_RETAU5200_H0.1_DSMAG_AR2_NX384_NY288_NZ192/',
            'CHA_RETAU5200_H0.1_DSMAG_AR2_NX448_NY336_NZ224/',
            'CHA_RETAU5200_H0.1_DSMAG_AR2_NX512_NY384_NZ256/',
            'CHA_RETAU5200_H0.1_DSMAG_AR2_NX768_NY576_NZ384/',
            'CHA_SMALL_RETAU5200_H0.1_DSMAG_AR2_NX512_NY384_NZ512/',
            'CHA_SMALL_RETAU5200_H0.1_DSMAG_AR2_NX1024_NY768_NZ1024/',
            'CHA_SMALL_RETAU5200_H0.1_DSMAG_AR2_NX1536_NY1152_NZ1536/']

line = textwrap.dedent("""
              ${nx:<4} \\times {nz:<4} \\times {ny:<4}$ & {dx:<6.3f} & {dy:<6.3f} & {dzc:<6.3f} & {dzw:<6.4f} & {ar:<2.1f} & {sgs:<6} & {retau:<9.1f} & ${cf:.5f} \pm {uncertainty:.2f}\\%$ & {err:>6.2f}\\% & {ett:.1f} \\\\
            """).strip()

with open('tab_params.txt', 'w') as f:
  for i in range(len(folders)):
    dns = Moser('CHA_RETAU5200/')
    les = CaNS(folders[i])
    les.stats_input()
    les.read_stats()
    uncertainty = les.uncertainty()
    err = (les.cf-dns.cf)/dns.cf
    ett = (les.tend-les.tbeg)*(2.0*dns.retau/dns.reb)
    if les.sgs == 'smag':
      sgs = 'SM'
    elif les.sgs == 'dsmag':
      sgs = 'DSM'
    f.write(line.format(
      nx=les.nx*int(12.8/les.lx),
      nz=les.nz*int(2.0/les.lz),
      ny=les.ny*int(4.8/les.ly),
      dx=les.dx,
      dy=les.dy,
      dzc=les.dzc,
      dzw=les.dzw,
      ar=les.dx/les.dy,
      sgs=sgs,
      retau=les.retau,
      cf=les.cf,
      uncertainty=uncertainty*100,
      err=err * 100,
      ett=ett
    ) + '\n') 