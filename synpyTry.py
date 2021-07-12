
import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

N = sym.Symbol('N')
fc = (np.pi/1000)/(88200*np.pi)
K = (fc*N*2)+1

tau = np.sqrt(2)/2
#Eq0 = tau * np.sin(np.pi * fc)

print(fc)
print(K)
print(tau)

print('solution:')

Eq4 = sym.Eq(K/N,1)
#Eq1 = sym.Eq(((1/N)*(sym.sin((sym.pi*fc*K)/N)/sym.sin((sym.pi*fc)/N))) , tau)
#Eq3 = sym.Eq((1/N)*sym.sin(sym.pi*fc*((fc*2*N)+1)),Eq0)

sol = sym.solve(Eq4)

print(sol)