from cales_post import CaNS, Moser
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
              ${nx:<4} \\times {nz:<4} \\times {ny:<4}$ & {dx:>6.1f} & {dy:>6.1f} & {dzc:>6.1f} & {dzw:>6.2f} & {ar:<2.1f} & {sgs:<6} & {retau:<9.1f} & ${cf:.5f} \pm {uncertainty:.2f}\\%$ & {err:>6.2f}\\% & {ett:.1f} \\\\
            """).strip()

with open('tab_params.txt', 'w') as f:
  for i in range(len(folders)):
    les = CaNS(folders[i])
    les.stats_input()
    les.read_stats()
    uncertainty = les.uncertainty()
    dns = Moser('CHA_RETAU550/')
    err = (les.cf-dns.cf)/dns.cf
    ett = (les.tend-les.tbeg)*(2.0*dns.retau/dns.reb)
    if les.sgs == 'smag':
      sgs = 'SM'
    elif les.sgs == 'dsmag':
      sgs = 'DSM'
    f.write(line.format(
      nx=les.nx,
      nz=les.nz,
      ny=les.ny,
      dx=les.dx*dns.retau,
      dy=les.dy*dns.retau,
      dzc=les.dzc*dns.retau,
      dzw=les.dzw*dns.retau,
      ar=les.dx/les.dy,
      sgs=sgs,
      retau=les.retau,
      cf=les.cf,
      uncertainty=uncertainty*100,
      err=err * 100,
      ett=ett
    ) + '\n') 