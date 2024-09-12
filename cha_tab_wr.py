from cans import *
from moser import *
import textwrap

# table of parameters
folders = [ 'CHA_RETAU550_NOSLIP_SMAG_AR2_NX192_NY128_NZ128/',
            'CHA_RETAU550_NOSLIP_SMAG_AR2_NX288_NY192_NZ192/',
            'CHA_RETAU550_NOSLIP_SMAG_AR2_NX384_NY256_NZ256/',
            'CHA_RETAU550_NOSLIP_SMAG_AR2_NX576_NY384_NZ384/',
            'CHA_RETAU550_NOSLIP_DSMAG_AR2_NX192_NY128_NZ128/',
            'CHA_RETAU550_NOSLIP_DSMAG_AR2_NX288_NY192_NZ192/',
            'CHA_RETAU550_NOSLIP_DSMAG_AR2_NX384_NY256_NZ256/',
            'CHA_RETAU550_NOSLIP_DSMAG_AR2_NX576_NY384_NZ384/']

line = textwrap.dedent("""
              {reb_dns} & {retau_dns:<14.1f} & {cf_dns:<12.5f} & ${nx:<4} \\times {ny:<4} \\times {nz:<4}$ & {dx:>6.1f} & {dy:>6.1f} & {dzc:>6.1f} & {dzw:>6.2f} & {sgs:<6} & {retau:<9.1f} & {cf:.5f} & {err:>6.2f}\\% & {ett:.1f} \\\\
            """).strip()

with open('tab_params.txt', 'w') as f:
  for i in range(len(folders)):
    les = CaNS(folders[i])
    dns = Moser('CHA_RETAU550/')
    err = (les.cf-dns.cf)/dns.cf
    ett = (les.tend-les.tbeg)*(2.0*dns.retau/dns.reb)
    if les.sgs == 'smag':
      sgs = 'SM'
    elif les.sgs == 'dsmag':
      sgs = 'DSM'
    f.write(line.format(
      reb_dns=int(dns.reb),
      retau_dns=dns.retau,
      cf_dns=dns.cf,
      nx=les.nx,
      ny=les.ny,
      nz=les.nz,
      dx=les.dx*dns.retau,
      dy=les.dy*dns.retau,
      dzc=les.dzc*dns.retau,
      dzw=les.dzw*dns.retau,
      sgs=sgs,
      retau=les.retau,
      cf=les.cf,
      err=err * 100,
      ett=ett
    ) + '\n') 