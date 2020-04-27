%pylab inline
import matlotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import random
from time import time

from insertionSort import insertionSort_time
from quickSort import quickSort_time

datos = [ii*100 for ii in range(0,21)]

tiempo_is = [] 
tiempo_qs = [] 

for ii in datos:
    lista_is = random.sample(range(0,10000000),ii)
    lista_qs = lista_is.copy()

    t0 = time() 
    insertionSort_time(lista_is)
    tiempo_is.append(round(time()-t0,6))

    t0 = time ()
    quickSort_time(lista_qs)
    tiempo_qs.append(round(time()-t0,6))

print("Tiempos parciales de ejcución en INSERT SORT {} [s]\n".format(tiempo_is))
print("Tiempos parciales de ejcución en QUICK SORT {} [s]".format(tiempo_qs))

print("Tiempo total de ejcución en INSERT SORT {} [s]\n".format(sum(tiempo_is)))
print("Tiempo total de ejcución en QUICK SORT {} [s]\n".format(sum(tiempo_qs)))

fig, ax = subplots()
ax.plot(datos, tiempo_is, label ="insert sort", marker="*", color="r")
ax.plot(datos, tiempo_qs, label ="quick sort", marker="o", color="b")
ax.set_xlabel('Datos')
ax.set_ylabel('Tiempo')
ax.grid(True)
ax.legend(loc=2);

plt.tittle('Tiempo de ejcución [s] (insert vs. quick)')
plt.show()
