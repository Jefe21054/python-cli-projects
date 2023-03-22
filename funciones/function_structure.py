'''
Las funciones nos permiten ejecutar varias veces una porcion de
codigo
parametros => cuando se crea la funcion
argumentos => cuando se invoca la funcion
'''

def fibonacci(n):
    '''Esta es una funcion que devuelve la serie de Fibonacci'''
    a,b = 0,1
    while a<n:
        print(a, end=' ')
        a,b = b,a+b
    print()

# Invocamos a la funcion
fibonacci(2000)
fibonacci(1000)
fibonacci(5000)
