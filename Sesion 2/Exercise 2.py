"""Listas en pyton"""

"""Requisito

-Crear dos listas vacias inicialmente
- Agregar luego datos de nombre, edad y profesion para ambos usando (Append)
- Sumar ambas listas y mostar el resultado en consola

- Mostrar de manera inversa la suma de ambas listas
- Actualizar la nueva lista eliminando las edades de ambas personas con remove




"""


var1 = []
var2 = []

var1.append("Jose")
var1.append("20")
var1.append("marketing")
var2.append("Mario")
var2.append("21")
var2.append("Economia")
print("El valor de mis listas son los siguientes: {} y {}".format(var1, var2))

suma_lista = var1 + var2

print("La suma de las listas es: {}".format(suma_lista))

suma_lista.reverse()

print("La reversa de mi nueva lista es: {}".format(suma_lista))

suma_lista.remove("20")
suma_lista.remove("21")

print("La lista actualizadaes: {}".format(suma_lista))