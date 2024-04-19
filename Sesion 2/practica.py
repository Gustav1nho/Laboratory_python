"""


crear 3 variables: nombre, edad, pais de residencia y distrito

Requisitos:
-nombre: string, edad: int , pais de residencia: string, distrito: string
-Concatenar estos datos e indicar una porcion como la siguiente

José tiene X años es del distrito de y viene de "pais de residencia"

-obtener el modulo de su edad al usarlo con el numero 5, mostrar el modulo
"""

Nombre = "Gustavo"
Edad = 20
Pais = "Perú"
Distrito = "Callao"

print("{} tiene {} años es del distrito {} y viene de: {}".format(Nombre, Edad, Pais, Distrito))

modulo = Edad % 5

print("El modulo entre la Edad y 5 es:", modulo)
