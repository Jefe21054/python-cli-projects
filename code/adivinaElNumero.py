import random

print("     B I E N V E N I D O     ")

nombre=input('Escribe tu nombre: ')
flag=0

while flag == 0:
    print(f'\nElije la dificultad\n')
    print(f'     M E N U     \n')
    print(f'1. FACIL')
    print(f'2. MEDIO')
    print(f'3. DIFICIL\n')
    choice = input('-> ')
    while choice != '3' and choice != '2' and choice != '1':
        print(f'\nElije entre los numeros que estan en el menu!')
        print(f'     M E N U     \n')
        print(f'1. FACIL')
        print(f'2. MEDIO')
        print(f'3. DIFICIL\n')
        choice = input('-> ')

    if choice=='1':
        print(f'\nHola {nombre},'+' El juego consiste en que adivines un numero entre 1 y 20 en 6 intentos')
        numero=random.randint(1,20)
        cont=0
        while cont<6:
            num=int(input('Ingresa el numero que crees que elegi: '))
            cont = cont + 1
            if num>numero:
                print(f'Estas por encima del numero!\n')
            if num<numero:
                print(f'Estas por debajo del numero!\n')
            if num==numero:
                break
        if num == numero:
            print(f'\nGANASTE!')
        if num != numero:
            print(f'\nWASTED!'+f'\nEl numero era {numero}')
    elif choice=='2':
        print(f'\nHola {nombre},'+' El juego consiste en que adivines un numero entre 1 y 50 en 6 intentos')
        numero=random.randint(1,50)
        cont=0
        while cont<6:
            num=int(input('Ingresa el numero que crees que elegi: '))
            cont = cont + 1
            if num>numero:
                print(f'Estas por encima del numero!\n')
            if num<numero:
                print(f'Estas por debajo del numero!\n')
            if num==numero:
                break
        if num == numero:
            print(f'\nGANASTE!')
        if num != numero:
            print(f'\nWASTED!'+f'\nEl numero era {numero}')
    elif choice=='3':
        print(f'\nHola {nombre},'+' El juego consiste en que adivines un numero entre 1 y 100 en 6 intentos')
        numero=random.randint(1,100)
        cont=0
        while cont<6:
            num=int(input('Ingresa el numero que crees que elegi: '))
            cont = cont + 1
            if num>numero:
                print(f'Estas por encima del numero!\n')
            if num<numero:
                print(f'Estas por debajo del numero!\n')
            if num==numero:
                break
        if num == numero:
            print(f'\nGANASTE!')
        if num != numero:
            print(f'\nWASTED!'+f'\nEl numero era {numero}')
    print('Deseas intentar nuevamente?')
    print('Digita "0" si quieres repetir')
    print('Si no, digita otro numero')
    flag=int(input('-> '))
