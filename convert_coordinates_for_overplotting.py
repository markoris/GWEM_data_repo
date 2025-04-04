import numpy as np
import argparse
from RIFT import lalsimutils

def Lt_from_R(R):
	return 800*np.power((R/13.4), 6)

def chi_effective(s1z, s2z, q):
	return (s1z + q*s2z)/(1+q)

parser = argparse.ArgumentParser()
parser.add_argument('posteriorfile', help='path to posterior file')
args = parser.parse_args()

data = np.genfromtxt(args.posteriorfile, names=True)

z = 0.0098

mc = data['mc']*(1+z)
delta = data['delta_mc']

eta = 1/4*(1-delta**2)

m1, m2 = lalsimutils.m1m2(mc, eta) 
R14 = data['R14']
s1z = data['a1z']
s2z = data['a2z']
Lambda_tilde = Lt_from_R(R14)

np.savetxt('converted_posteriors.dat', np.c_[m1, m2, s1z, s2z, Lambda_tilde], header='m1 m2 a1z a2z LambdaTilde')
