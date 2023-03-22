'''
Manejo de errores dentro del programa para que no se rompa
ni se detenga.
try => evalua una porcion de codigo
except => maneja el posible error
else => se ejecuta cuando no hay un error
finally => se ejecuta independientemente de si hay o no errores
'''

try:
    raise Exception('Error creado a posta')
except Exception:
    print('Error creado a posta')
else:
    print('No hubo error')
finally:
    print('Esto siempre se ejecuta')
