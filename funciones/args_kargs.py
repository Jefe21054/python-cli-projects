# ARGS
# def func(*args):
#     for i in args:
#         print(i)

# func('EDteam','Hola Mundo',1,2,3,4,5,6,8,9,7,11)

# KARGS
# days = {
#     'dia1': 'Lunes',
#     'dia2': 'Martes'
# }

dias = dict(day1='Miercoles',day2='Jueves')

# def func2(**kargs):
#     print(kargs)

# func2(**days)
# func2(**dias)

def func3(*args, **kwargs):
    print(args)
    print(kwargs)

func3(1,2,3,4,5,6,7, **dias)

