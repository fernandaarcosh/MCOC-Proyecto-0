# MCOC-Proyecto-0
# Introducción
La idea del proyecto mostrado a continuación es mostrar la perdida por significancia que se encuentra en típicas operaciones aritméticas.
# Ejemplo (Redacción de idea y procedimiento)
Para esta demostración se utilizó la función cúbica sobre 4 valores, los cuales se calcularon de cuatro maneras diferentes, la primera se tomo como valor real, entregado por la calculadora TI en configuración de 12 flotantes, luego el valor exacto que es entregado por la consola la cual es de 64 bits, fianlmente se obtuvieron los valores mediante sp.float de 32 y 64 bits. 
Finalmente se calcularon los errores que se tiene con el valor real y los sp.float encontrados, y entre el valor exacto y los sp.float de 32 y 64, como es de esperarse el error entre el valor exacto y el de 64 bits será de 0.
# Resultados
Se obtiene el error porcentual/relativo de los valores de la siguiente manera:
```
(abs(valores_32[i] - valor_real[i]))/valor_real[i])*100)

(abs(valores_32[j] - valor_exacto[j]))/valor_exacto[j])*100)
```
Este se observa de manera gráfica, en el archivo adjunto.
Y con los siguientes resultados obtenidos por consola.
```
Valores reales:  [7.217340000000001e-10, 3.82569e-12, 1.89061e-14, 3.2645300000000006e-17] 

Valores exactos: [7.21734273e-10, 3.8256941440000006e-12, 1.8906130944000005e-14, 3.2645273536e-17] 

Valores 32 bits: [7.2173428e-10, 3.8256941e-12, 1.8906131e-14, 3.2645275e-17] 

Valores 64 bits: [7.2173427299999998e-10, 3.8256941440000006e-12, 1.8906130944000005e-14, 3.2645273536e-17] 

Errores 32 bits (real): 
[3.9273289433581128e-05, 0.00010721697005273478, 0.00016469051697751258, 7.6164949260484194e-05] 

Errores 64 bits (real): 
[3.7825570070502025e-05, 0.00010832032916860673, 0.00016367204238397826, 8.1065268219657365e-05] 

Errores 32 bits (exacto): 
[1.4477188154712117e-06, 1.1033579207110294e-06, 1.0184729265789042e-06, 4.9003229316330824e-06] 

Errores 64 bits (exacto): 
[0.0, 0.0, 0.0, 0.0] 
```
# Recursos
 ```
 [https://en.wikipedia.org/wiki/Loss_of_significance]
 [https://www.youtube.com/watch?v=PZRI1IfStY0&feature=youtu.be]
 [https://www.youtube.com/watch?v=f4ekifyijIg&feature=youtu.be]
 [https://www.youtube.com/watch?v=782QWNOD_Z0&feature=youtu.be]
```
