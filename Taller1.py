#Primer punto
l_paises1 = ['Colombia','Mexico','Turquía','Polonia','serbia','dinamarca','holanda','Alemania']
l_paises = []
arch=open('Ejercicio1.txt','w')
espacios=(', ')
for i in l_paises1:
    i=i.capitalize()
    l_paises.append(i)
for j in l_paises:
    ju=j+espacios
    arch.write(ju)
arch.close()

a=open('Ejercicio1.txt','w')
for k in l_paises:
    print(k)



#TERCER PUNTO CALCULADORA DE BINARIOS
s_num = int(input('Ingrese el numero a convertir en binario...'))
div = 1
s_bin = 0
list = []
while not (div == 0):
  div = s_num //2
  s_bin = s_num%2
  s_num = div
  list.append(s_bin)
print(list)


# CUARTO PUNTO PROMEDIO.... MEDIANA.... DESVIACION ESTANDAR

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

l_valores = [24, 19, 25, 21, 26, 30, 45, 48, 16]
s_mean = np.mean(l_valores)
s_median = np.median(l_valores)
s_STD = np.std(l_valores)

print('El promedio es: ', s_mean)
print('La mediana es: ', s_median)
print('La desviacion estandar es: ', s_STD)



