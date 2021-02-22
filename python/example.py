#!/usr/bin/env python
import sys,os
import numpy as np
import pylab as py
from corelib import JAMLIB
from scipy.integrate import quad

###################################
# select distribution
###################################
jamlib=JAMLIB('JAM17/PPDF')
#jamlib=JAMLIB('JAM17/FFpion')
#jamlib=JAMLIB('JAM17/FFkaon')

###################################
# Quick test
###################################
x=0.05
Q2=2.5
flav='up'
print 'alphaS     = ',jamlib.get_alphaS(Q2)
print 'num pos    = ',jamlib.npos
print 'xF(ipos=0) = ',jamlib.get_XF(0,flav,x,Q2)

###################################
# Plot xF
###################################
X=np.logspace(-3,0,200)

sp=[[(jamlib.get_XF(i,'sp',x,Q2)) for x in X] for i in range(jamlib.npos)]
sp0=np.mean(sp,axis=0)
dsp0=np.std(sp,axis=0)

py.figure(figsize=(7,5))
ax=py.subplot(111)
ax.fill_between(X,sp0-dsp0,sp0+dsp0,edgecolor='r',facecolor='r',alpha=0.3)
ax.plot(X,sp0,'r-',lw=2)
ax.set_xlim(np.amin(X),np.amax(X));
ax.set_xlabel(r'$x$',size=50)
ax.set_ylabel(r'$xs^+(x)$',size=50)
ax.tick_params(axis='both', which='major', labelsize=20)
ax.set_xscale('log')
ax.set_xlim(1e-3,1)
py.tight_layout()
py.savefig('xSP.pdf')
