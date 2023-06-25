'''
Para validar que un dato no sea del tipo `str` antes de ser casteado a
otro tipo de dato, podemos utilizar la función `isinstance()`. Esta función
nos permite comprobar si un objeto es de un determinado tipo de dato.
'''
dato = "123"
if not isinstance(dato, int):
    dato = int(dato)

'''
En este caso, si `dato` no es un entero, entonces se convierte a un entero
usando la función `int()`. Si `dato` ya es un entero, entonces no se hace nada.
'''
#VALIDAR SI UN DATO ES INT
numero = 10.3 #es un float
if not isinstance(numero, int):
    numero = int(numero)
    
print(numero)
print(type(numero))

#-----------------------------
#VALIDAR SI UN DATO ES FLOAT
numero = "10.3" #es un str
if not isinstance(numero, float):
    numero = float(numero)
    
print(numero)
print(type(numero))

#-----------------------------
#VALIDAR SI UN DATO ES STR
numero = 10.3443112 #es un float
if not isinstance(numero, str):
    numero = str(numero)
    
print(numero)
print(type(numero))
