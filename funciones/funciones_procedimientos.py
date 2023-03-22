'''
funcion => Una funcion siempre devuelve al menos, un valor
procedimiento => No devuelve un valor
scope => Es el alcance que tiene una variable dentro del codigo
'''
# variable global, esta por fuera de toda estructura de control
name = 'Ivan'

def func():
    global name
    name = name + ' Iglesias'
    print(name)

func()
