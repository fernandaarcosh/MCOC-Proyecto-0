# -*- coding: utf-8 -*-
"""
Created on Sat Aug 03 13:39:38 2019

@author: Feña
"""

import scipy as sp
import matplotlib.pylab as plt


# Se desean mostrar los errores producidos por perdida de significancia, en una funcion aritmetica, se escogio la funcion cubica
a= [0.897*(10**-3), 1.564*(10**-4), 2.664*(10**-5), 3.196*(10**-6)]
N=len(a)

# Para poder observar la diferencia y los errores que se producen.
#Se obtiene primero el valor real, calculado a mano. (Calculadora TI con 12 flotantes)
valor_real=[7.21734*(10**-10),3.82569*(10**-12),1.89061*(10**-14),3.26453*(10**-17)]

#Luego los valores exactos calculados por la consola, que es de 64 bits
valor_exacto=[]
for i in a:
    ve=((i**3))
    valor_exacto.append(ve)

#Valores calculados para 32 bits
valores_32 = []
for i in a:
    v32=sp.float32((i**3))
    valores_32.append(v32)

#Valores calculados para 64 bits
valores_64 = []
for i in a:
    v64=sp.float64((i**3))
    valores_64.append(v64)
    
#Calculo de errores porcentuales entre el valor real y exacto, y el valor entregado por el programa tanto en 32 y 64 bits
error_32_r = []
error_64_r = []

i = 0
while i < N:
    error_32_r.append(((abs(valores_32[i] - valor_real[i]))/valor_real[i])*100)
    error_64_r.append(((abs(valores_64[i] - valor_real[i]))/valor_real[i])*100)
    i+=1

error_32_e = []
error_64_e = []

j = 0
while j < N:
    error_32_e.append(((abs(valores_32[j] - valor_exacto[j]))/valor_exacto[j])*100)
    error_64_e.append(((abs(valores_64[j] - valor_exacto[j]))/valor_exacto[j])*100)#como es de esperar este error debiese ser 0
    j+=1

print "\n"
print "Valores reales: ", valor_real, "\n"
print "Valores exactos: ", valor_exacto, "\n"
print "Valores 32 bits: \n", valores_32, "\n"
print "Valores 64 bits: \n", valores_64, "\n"
print "Errores 32 bits (real): \n",error_32_r, "\n"
print "Errores 64 bits (real): \n",error_64_r, "\n"
print "Errores 32 bits (exacto): \n",error_32_e, "\n"
print "Errores 64 bits (exacto): \n",error_64_e, "\n"

#Plot de los errores encontrados
plt.xlabel("a**3")
plt.ylabel("Error relativo")
plt.figure(1)
plt.plot(a,error_32_r, label="Error 32 bits (real)" )
plt.plot(a,error_64_r, label="Error 64 bits (real)" )

plt.plot(a,error_32_e, label="Error 32 bits (exacto)" )
plt.plot(a,error_64_e, label="Error 64 bits (exacto)" )

plt.savefig("loss-of-significance.png")

plt.show()