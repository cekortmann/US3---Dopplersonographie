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
ua80= unp.uarray([90.0,144.0,197.0,349.0,472],[0,0,0,0,0])
ua70= unp.uarray([100,189,296,447,641],[0,0,0,0,0])
ua54= unp.uarray([144,200,447,748,1007],[0,0,0,0,0])
a80 = np.array([90.0,144.0,197.0,349.0,472])
a70 = np.array([100,189,296,447,641])
a54 = np.array([144,200,447,748,1007])

def v(a,dv,v,c):
    return (c*dv)/(2*v*cos(a*np.pi/180))
    

print('80.06:', v(a[0],ua80,v0,1800))
print('70.53:', v(a[1],ua70,v0,1800))
print('54.74:', v(a[2],ua54,v0,1800))

def Ausgleich(a,x,b):
    return a*x+b

params1 = curve_fit(Ausgleich,v(a[0],a80,v0,1800),2*v0*v(a[0],a80,v0,1800)/1800)
a1_fit = params1[0][0]
b1_fit = params1[0][1] 

params2 = curve_fit(Ausgleich,v(a[1],a70,v0,1800),2*v0*v(a[1],a70,v0,1800)/1800)
a2_fit = params2[0][0]
b2_fit = params2[0][1] 

params3 = curve_fit(Ausgleich,v(a[2],a54,v0,1800),2*v0*v(a[2],a54,v0,1800)/1800)
a3_fit = params3[0][0]
b3_fit = params3[0][1] 

h1=np.linspace(0,1.3,10)
h2=np.linspace(0,0.9,10)
h3=np.linspace(0,0.8,10)



plt.plot(h1,Ausgleich(a1_fit, h1, b1_fit),'orange', markersize=6 , label = 'Ausgleichsgerade', alpha=0.5)
plt.plot(v(a[0],a80,v0,1800),2*v0*v(a[0],a80,v0,1800)/1800, 'xr', markersize=6 , label = 'Messdaten', alpha=1)
plt.legend(loc="best")
plt.grid(1)
plt.xlabel(r'$v \, / \, \mathrm{m}\cdot \mathrm{s}^{-1}$')
plt.ylabel(r'$\Delta \nu \cdot (\mathrm{cos}\alpha)^{-1}\, / \, \mathrm{Hz}$')
plt.savefig('build/plot11.pdf', bbox_inches = "tight")
plt.clf() 
print('a1',a1_fit, 'b1',b1_fit)

plt.plot(h2,Ausgleich(a2_fit, h2, b2_fit),'orange', markersize=6 , label = 'Ausgleichsgerade', alpha=0.5)
plt.plot(v(a[1],a70,v0,1800),2*v0*v(a[1],a70,v0,1800)/1800, 'xr', markersize=6 , label = 'Messdaten', alpha=1)
plt.grid(1)
plt.legend(loc="best")
plt.xlabel(r'$v \, / \, \mathrm{m}\cdot \mathrm{s}^{-1}$')
plt.ylabel(r'$\Delta \nu \cdot (\mathrm{cos}\alpha)^{-1}\, / \, \mathrm{Hz}$')
plt.savefig('build/plot12.pdf', bbox_inches = "tight")
plt.clf() 
print('a2',a2_fit, 'b2',b2_fit)

plt.plot(h3,Ausgleich(a3_fit, h3, b3_fit),'orange', markersize=6 , label = 'Ausgleichsgerade', alpha=0.5)
plt.plot( v(a[2],a54,v0,1800),2*v0*v(a[2],a54,v0,1800)/1800,'xr', markersize=6 , label = 'Messdaten', alpha=1)
plt.grid(1)
plt.xlabel(r'$v \, / \, \mathrm{m}\cdot \mathrm{s}^{-1}$')
plt.ylabel(r'$\Delta \nu \cdot (\mathrm{cos}\alpha)^{-1}\, / \, \mathrm{Hz}$')
plt.legend(loc="best")     
plt.savefig('build/plot13.pdf', bbox_inches = "tight")    
plt.clf() 
print('a3',a3_fit, 'b3',b3_fit)

#Zweiter Teil
bla, Mt1, vcm1, vm1,I = np.genfromtxt('rpm3920.txt', unpack=True, skip_header=1)

plt.plot(Mt1,vm1,'xr', linewidth = 1, label = 'Messwerte', alpha=0.5)
plt.legend(loc="best")
plt.grid(1)
plt.ylabel(r'$v \, / \,\mathrm{m}\cdot \mathrm{s}^{-1}$')
plt.xlabel(r'Messtiefe $ x\, / \, \mathrm{mm}$')
plt.savefig('build/rpm39201.pdf', bbox_inches = "tight")
plt.clf() 

plt.plot(Mt1,I,'xr', linewidth = 1, label = 'Messwerte', alpha=0.5)
plt.legend(loc="best")
plt.grid(1)
plt.ylabel(r'$I \, / \,\mathrm{V}^2\mathrm{s}^{-1}$')
plt.xlabel(r'Messtiefe $ x\, / \, \mathrm{mm}$')
plt.savefig('build/rpm39202.pdf', bbox_inches = "tight")
plt.clf() 


bla2, Mt2, vcm2, vm2,I2 = np.genfromtxt('rpm6100.txt', unpack=True, skip_header=1)

plt.plot(Mt2,vm2,'xr', linewidth = 1, label = 'Messwerte', alpha=0.5)
plt.legend(loc="best")
plt.grid(1)
plt.ylabel(r'$v \, / \,\mathrm{m}\cdot \mathrm{s}^{-1}$')
plt.xlabel(r'Messtiefe $x\, / \, \mathrm{mm}$')
plt.savefig('build/rpm61001.pdf', bbox_inches = "tight")
plt.clf() 

plt.plot(Mt2,I2,'xr', linewidth = 1, label = 'Messwerte', alpha=0.5)
plt.legend(loc="best")
plt.grid(1)
plt.ylabel(r'$I \, / \,\mathrm{V}^2\mathrm{s}^{-1}$')
plt.xlabel(r'Messtiefe $x\, / \, \mathrm{mm}$')
plt.savefig('build/rpm61002.pdf', bbox_inches = "tight")
plt.clf() 
