'''
continue => permite saltar a la siguiente posicion
break => rompe (cancela) el ciclo
else => ejecuta una porcion de codigo cuando termina el ciclo
completo o se completa un ciclo
'''

frameworks = ['Flask','Django','FastApi','Pyramid']

# Continue
# for i in frameworks:
#     if i == 'Flask':
#         print('Es Flask')
#         continue
#     print(i)

# Break
# for i in frameworks:
#     if i == 'Flask':
#         print('Es Flask')
#         break
#     print(i)

# Else
# for i in frameworks:
#     if i == 'Flask':
#         print('Es Flask')
#     print(i)
# else:
#     print('El ciclo termino')

# Else
numero = 1
while numero < 10:
    if numero == 5:
        print('Es 5')
        # continue
    print(numero)
    numero += 1
# else:
#     print('El ciclo termino')