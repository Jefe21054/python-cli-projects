import math

print("     B I E N V E N I D O     ")

r=float(input("Digita el radio del circulo: "))
dec=float(input("Cifras decimales en el resultado: "))
f=10**(dec)

area=(math.pi)*(r**2)
a=round(area*f)/f

perimetro=(2*math.pi)*r
p=round(perimetro*f)/f

print(f"\nEl area del circulo de radio {r}",f" es: {a}",
      f"\nY su perimetro es: {p}")

'''
Para elegir el numero de decimales
tambien se puede asi:
print(f'El area de la circunferencia es: {a:.Df}')
siendo D la cantidad de decimales del flotante,
al ser float hasta 16 decimales como max.
'''
