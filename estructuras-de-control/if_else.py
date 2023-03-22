# condicion = (if) True => ejecuta codigo
# condicion = (else) False => ejecuta otra porcion de codigo

edad_persona = int(input('Por favor, ingresa tu edad: '))
EDAD_BASE = 18

if edad_persona > EDAD_BASE:
    print('Eres mayor de edad y mayor a 18 anios')
elif edad_persona == 18:
    print('Tienes 18 anios')
else:
    print('Eres menor de edad')