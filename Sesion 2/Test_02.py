"""Conversion de datos"""

"""De string: str a entero int(Entero)"""

var_1 = "hello world"
var_2 = 2024
var_3 = " Gustavo "

#imprimir las cadenas pero tienen que ir concatenadas diciendo al final "hello world 2024 'nombre'"


suma_1 = (var_1 +" "+ str(var_2) +" "+ var_3)

print(var_1 + str(var_2) + var_3)

print("{}".format(suma_1))

print("{} {} {}".format(var_1,var_2,var_3))
