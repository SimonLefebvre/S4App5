import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

sym.init_printing()

K = sym.Symbol('K')

G_fc = np.sqrt(2)/2
G_0 = 1
pie = np.pi/2000
a = np.sin(pie)

print('G_fc')
print(G_fc)
print('pie')
print(pie)
print('a')
print(a)


N = np.arange(2, 1024)
Eq2 = np.sin(N*pie)/(N*a)
plt.stem(N, Eq2)
plt.show()

K = 885



#Eq1 = sym.Eq((sym.sin(K*pie)/(K*a)), G_fc)
#sol = sym.solve(Eq1)
#print('solution')
#print(sol)


