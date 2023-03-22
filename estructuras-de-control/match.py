'''
Match es el Switch-Case de Python. Sirve para evaluar un dato y
con base a ello realizar una accion
'''

status = 'liquido'

match status:
    case 'solido':
        print('El estado es solido')
    case 'liquido':
        print('El estado es liquido')
    case 'gaseoso':
        print('El estado es gaseoso')
    case _:
        print('El estado no existe')