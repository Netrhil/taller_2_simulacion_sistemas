# Estimar el valor de pi a travez del metodo de montecarlo

from random import random
import numpy as np
import matplotlib.pyplot as plt

#Genera una lista con diferentes numero de intentos
intentos = list(np.linspace(10,1000000, 1000))
pi = []

def montecarlo(intentos, aciertos = 0):
    for i in range(int(intentos)):
        # Por defecto Random() genera numeros aleatorios entre 0 y 1
        x, y = random() , random()

        # Define si el punto quedo dentro del circulo
        if x**2 + y**2 < 1 :
            aciertos = aciertos + 1
    return float(aciertos)

# I es el numero de intentos totales dentro de la lista intentos
for i in intentos:
    pi.append(4*(montecarlo(i)/i))


#Setea los valores del label del grafico
plt.plot(intentos, pi, 'g')
plt.title('Estimar el valor de pi a travez de Monte Carlos')
plt.xlabel('numero de ensayos')
plt.ylabel('valor estimado de pi')
plt.ylim(3.11,3.17)
plt.show()

plt.hist(pi, bins = np.linspace(3.12,3.16,50), color='green')
plt.title('Estimar el valor de pi a travez de Monte Carlos')
plt.xlabel('Valor estimado de Pi')
plt.ylabel('Ensayos')
plt.xlim(3.13,3.15)
plt.show()
