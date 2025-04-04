import numpy as np
from matplotlib import pyplot as plt

def delta(m1,m2):
  return (m1-m2)/(m1+m2)

def q_of_delta(delta):
  # delta = 1-q/(1+q), so q=(1-delta)/(1+delta)
  return (1-delta)/(1+delta)
q_of_delta(delta(1,0.3)) # sanity check

def mass1(Mc, eta):
    """Compute larger component mass from Mc, eta"""
    return 0.5*Mc*eta**(-3./5.)*(1. + np.sqrt(1 - 4.*eta))

def mass2(Mc, eta):
    """Compute smaller component mass from Mc, eta"""
    return 0.5*Mc*eta**(-3./5.)*(1. - np.sqrt(1 - 4.*eta))

def mchirp(m1, m2):
    """Compute chirp mass from component masses"""
    return (m1*m2)**(3./5.)*(m1+m2)**(-1./5.)

def symRatio(m1, m2):
    """Compute symmetric mass ratio from component masses"""
    return m1*m2/(m1+m2)/(m1+m2)

def m1m2(Mc, eta):
    """Compute component masses from Mc, eta. Returns m1 >= m2"""
    etaV = np.array(1-4*eta,dtype=float)
    if isinstance(eta, float):
        if etaV < 0:
            etaV = 0
            etaV_sqrt =0
        else:
            etaV_sqrt = np.sqrt(etaV)
    else:
        indx_ok = etaV>=0
        etaV_sqrt = np.zeros(len(etaV),dtype=float)
        etaV_sqrt[indx_ok] = np.sqrt(etaV[indx_ok])
        etaV_sqrt[np.logical_not(indx_ok)] = 0 # set negative cases to 0, so no sqrt problems
    m1 = 0.5*Mc*eta**(-3./5.)*(1. + etaV_sqrt)
    m2 = 0.5*Mc*eta**(-3./5.)*(1. - etaV_sqrt)
    return m1, m2

def mdisk_kf(delta, R1p4, f_d=1 ):
  # written for scalar values
  R = R1p4 # lazy, assume all same radius
  q = q_of_delta(delta)
  m2 = mass2(1.186, q/(1+q)**2)
  C = m2/(R1p4/1.5) # convert radius in km to Msun, via 1Msun ~ 1.5 km
  discrim = -8.1324*C+1.4820
  out = np.zeros(discrim.shape)
  out[discrim > 0] = m2[discrim>0]*np.power(discrim[discrim>0], 1.7784)
  out = f_d*np.maximum(m2*5*1e-4,out )
  return out

def mdisk_dc(delta, R1p4, f_d=1):
  
  q = q_of_delta(delta)
  m1 = mass1(1.186, q/(1+q)**2)
  m2 = mass2(1.186, q/(1+q)**2)
  
  a0=-1.725,
  da=-2.337,
  b0=-0.564,
  db=-0.437,
  c=0.958,
  d=0.057,
  beta=5.879,
  qhat=0.886,

  val  = 0.5 * np.tanh( beta* (m2/m1  - qhat))
  
  a = a0 + da * val
  b = b0 + db * val
  # Threshold mass: follow https://github.com/mcoughlin/gwemlightcurves/blob/master/gwemlightcurves/EjectaFits/CoDi2019.py, note HARDCODED vals
  mTOV_here = 2.17
  R16 = R1p4
  mth  = (2.38 - 3.606* mTOV_here/R16)*mTOV_here
  
  mtot = m1+m2
  mdisk = a*(1+b*np.tanh((c - mtot/mth)/d) )
  mdisk[mdisk<-3] = -3.0
  mdisk = 10**mdisk

  return f_d*mdisk

def md_kf(delta, R1p4, alpha_d=1 ):
  # written for scalar values
  R = R1p4 # lazy, assume all same radius
  q = q_of_delta(delta)
  m1 = mass1(1.186, q/(1+q)**2)
  m2 = mass2(1.186, q/(1+q)**2)
  C1 = m1/(R1p4/1.5) # convert radius in km to Msun, via 1Msun ~ 1.5 km
  C2 = m2/(R1p4/1.5) # convert radius in km to Msun, via 1Msun ~ 1.5 km
  out = np.zeros(m1.shape)
  out += (-9.3335/C1 + 114.17*np.power(m2/m1,1.5465)-337.56*C1)*m1
  out += (-9.3335/C2 + 114.17*np.power(m1/m2,1.5465)-337.56*C2)*m2
  return out*1e-3*alpha_d

def md_dc(delta, R1p4, alpha_d=1 ):
  # written for scalar values
  R = R1p4 # lazy, assume all same radius
  q = q_of_delta(delta)
  m1 = mass1(1.186, q/(1+q)**2)
  m2 = mass2(1.186, q/(1+q)**2)
  C1 = m1/(R1p4/1.5) # convert radius in km to Msun, via 1Msun ~ 1.5 km
  C2 = m2/(R1p4/1.5) # convert radius in km to Msun, via 1Msun ~ 1.5 km

  from CoDi2019 import calc_meje
  from CoDi2019 import calc_vej
  m_eje=np.array(calc_meje(m1, C1, m2, C2, zeta=alpha_d, split_mej = True))
  md = m_eje[1]

  return md

def vej(delta, R1p4):
    """
        https://arxiv.org/pdf/1612.03665.pdf#equation.3.5

    https://arxiv.org/pdf/1612.03665.pdf#equation.3.6

    a = −0.219479,  b= 0.444836,  c=−2.67385

   :param float m1: mass of larger ns (MSun)
   :param float c1: compactness of the larger neutron star
   :param float m2: mass of samller ns (MSun)
   :param float c2: compactness of the smaller neutron star
   :return: velocity of ejecta mass (Msun)
   :rtype: float
    """
    R =R1p4 # lazy, assume all same radius
    q = q_of_delta(delta)
    m1 = mass1(1.186, q/(1+q)**2)
    m2 = mass2(1.186, q/(1+q)**2)
    c1 = m1/(R1p4/1.5) # convert radius in km to Msun, via 1Msun ~ 1.5 km
    c2 = m2/(R1p4/1.5) # convert radius in km to Msun, via 1Msun ~ 1.5 km

    a=-0.3090
    b=0.657
    c=-1.879

    return a*(m1/m2)*(1+c*c1) + a*(m2/m1)*(1+c*c2)+b

x = np.linspace(0,0.8,20)
y = np.linspace(10,25,20)
X,Y = np.meshgrid(x,y)
Z = mdisk_dc(X,Y)
CS = plt.contour(X,Y,Z, linestyles='dashed')
ax = plt.gca()
ax.clabel(CS)

x = np.linspace(0,0.8,20)
y = np.linspace(10,25,20)
X,Y = np.meshgrid(x,y)
Z = md_dc(X,Y)
levels = np.array([1e-3,1e-2,0.1, 0.2])
CS = plt.contour(X,Y,Z, levels)
ax = plt.gca()
ax.clabel(CS)

x = np.linspace(0,0.8,20)
y = np.linspace(10,25,20)
X,Y = np.meshgrid(x,y)
Z = vej(X,Y)
levels = np.array([0.1, 0.125, 0.15, 0.175, 0.2])
CS = plt.contour(X,Y,Z, linestyles='dotted', levels=levels)
ax = plt.gca()
ax.clabel(CS)

plt.xlabel(r'$\delta$', size=16)
plt.ylabel(r'$R_{\rm{1.4}}$', size=16)

plt.savefig("fig_naive_contours.pdf")
