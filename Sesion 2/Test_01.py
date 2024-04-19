"""Conversion de datos"""

"""De string a tipo de dato entero int(Entero)"""

var_1 = "8000"
var_2 = 35000
var_3 = 400.5


suma_1 = var_2 + var_3

suma_1 = var_2 + var_3
print ("El valor de suma_1 es: {}".format(suma_1))

#Esta suma no es posible por ser un valor string y otro un valor entero

#suma_2 = var_1 + var_2
#print("El valor de mi suma_3 es: {}".format(suma_2))


suma_3 = int(var_1) + var_2
print("El valor de suma_3 es: {}".format(suma_3))

suma_4 = var_2 + var_3
print("El valor de la suma_4 es: {}".format(suma_4))

var_4 = int(suma_4)
print(var_4)

var_5 = "700"
var_6 = 4000
var_7 = 40.68

"""La suma de las 3 variables como string"""

suma_5 = var_5 + str(var_6) + str(var_7)

print("El valor de la suma_5 es: {}".format(suma_5))