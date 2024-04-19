"""Listas en python"""


"""Listas pop(): quitar un elemento de una lista en python"""

paises = ["Perú", "Francia", "Eslovenia", "Disney"]

print("Los valores iniciales en mi lista de paises son {}".format(paises))

paises.pop()

#El pop quita el ultimo valor de la lista

print("Los valores iniciales en mi lista de paises son {}".format(paises))

#Podemos usar pop selecionando un valor

paises.pop(0)

print("Los valores finales de mis lista con pop es: {}".format(paises))