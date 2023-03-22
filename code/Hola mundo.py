# Python permite el tipado dinamico
'''
Esto es un comentario multilinea
El tipado dinamico es cuando una misma
variable puede contener diferentes
tipos de datos a lo largo del programa.
'''
valor = 10
print("\n")
print(valor)
valor='Ivan'
print("\n")
print(valor)

#Operadores Aritmeticos
#siguen el orden de operaciones normal

num1=10
num2=5

resultado=num1/num2
a=10/3
print("\n")
print(resultado)
print("\n")
print(a)
# // es para division 'entera' o redondeada a la baja
# % es el modulo (residuo de la division)
# a**b es para potencia, a elevado b

a=10//3
print("\n")
print(a)

num1=3
num2=2

resultado=num1**num2
print("\n")
print(resultado)

#Operadores relacionales

relacional = 10 >= 20

print("\n")
print(relacional)

a=10
b=20
c=30

# los operadores aritmeticos tienen prioridad ante los relacionales

operacion = a+b!=c
print("\n")
print(operacion)

# Operadores de asignacion
# Sirven para acortar el codigo. Previamente debemos declarar un valor inicial de
# la variable igual a 0.

a=0

a+=5 # += es suma en asignacion
a-=2 # -= es resta en asignacion
a*=3 # *= es multiplicacion en asignacion
a/=3 # /= es division en asignacion
a**=2 # **= es potencia en asignacion
a%=2 # %= es modulo en asignacion

print("\n")
print(a)

# Salida de datos

# Format

nombre='Ivan'
edad=20

print("\n")
print("Hola {}, tienes {} anios".format(nombre,edad))

# Nueva forma (se usa esta en el curso)

print("\n")
print(f"Hola {nombre}, tienes {edad} anios de edad.")

# Ingreso de datos

# Datos de tipo cadena
nombre = input("Digite su nombre: ")
print(f"Hola {nombre}")

# El input guarda datos de tipo cadena.

# Datos de tipo numerico entero (int)

numero=int(input("Digite un numero: "))
print(f"El numero es: {numero}")

# Datos de tipo numerico decimal (float)

decimal=float(input("Digite un decimal: "))
print(f"El numero es: {decimal}")

# Funciones integradas
# Sirven para transformar tipos de datos, como para
# el ingreso de datos numericos, que pasa de cadena
# a entero o flotante.

# Transformacion de datos numericos a cadena (str)

n=str(12.34)
print(f"\n {n}")

# Transformacion de entero a binario (bin)

n=bin(10)
print(f"\n {n}")

# Transformacion de cualquier valor a entero (int)

n=int("0b1010",2) # Se pone 0b para indicar que es binario y el binario en si
                  # Se utiliza coma y luego la base en la que esta el numero.
print(f"\n {n}")

# Funciones integradas iguales a octave abs(), round(), len(). fix() no existe

n=len("diwqKDNOwqndqwo")
print(f"\n {n}")

# round() redondea al entero mas cercano que se pueda

n=round(5.6)
a=round(5.4)
print(f"\n Redondeo de 5.6: {n}", f"\n Redondeo de 5.4: {a}")




