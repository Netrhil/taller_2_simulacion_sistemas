# Estimar el valor de pi a travez del metodo de Gregory-Leibniz

from random import random
import numpy as np
import matplotlib.pyplot as plt

pi=[]
iteraciones = range(1, 1000)
def gregory_leibniz(n):
    s = 0
    for k in range(1, n + 1):
        s += (-1)**(k + 1) / (2 * k - 1)
    return 4 * s

# I es el numero de iteraciones en la sumatoria
for i in iteraciones:
    pi.append(gregory_leibniz(i))


#Setea los valores del label del grafico
plt.plot(iteraciones, pi, 'g')
plt.title('Estimar el valor de pi a travez de Gregory-Leibniz')
plt.xlabel('Numero de iteraciones')
plt.ylabel('valor estimado de pi')
plt.ylim(3.11,3.17)
plt.show()

plt.hist(pi, bins = np.linspace(3.12,3.16,1000), color='green')
plt.title('Estimar el valor de pi a travez de Gregory-Leibniz')
plt.xlabel('Valor estimado de Pi')
plt.ylabel('Numero de iteraciones')
plt.xlim(3.13,3.15)
plt.show()
