import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from numpy import sqrt
import scipy.constants as const
from scipy.optimize import curve_fit                        # Funktionsfit:     popt, pcov = curve_fit(func, xdata, ydata) 
from uncertainties import ufloat                            # Fehler:           fehlerwert =  ulfaot(x, err)
from uncertainties import unumpy as unp 
from uncertainties.unumpy import uarray                     # Array von Fehler: fehlerarray =  uarray(array, errarray)
from uncertainties.unumpy import (nominal_values as noms,   # Wert:             noms(fehlerwert) = x
                                  std_devs as stds)  
from uncertainties.umath import cos

a1=80.06
a2=70.53
a3=54.74

v0=2*10**6
c1=2700

a=(80.06,70.53,54.74)
#a=np.deg2ra(a)
a80= unp.uarray([90.0,144.0,197.0,349.0,472],[0,0,0,0,0])
a70= unp.uarray([100,189,296,447,641],[0,0,0,0,0])
a54= unp.uarray([144,200,447,748,1007],[0,0,0,0,0])
#secondW= unp.uarray

def v(a,dv,v,c):
    return (c*dv)/(2*v*cos(a*np.pi/180))
    

print('80.06:', v(a[0],a80,v0,1800))
print('70.53:', v(a[1],a70,v0,1800))
print('54.74:', v(a[2],a54,v0,1800))