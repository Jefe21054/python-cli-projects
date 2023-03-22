import os

runProgram = True
todoList = []

def showMenuOptions():
    '''Funcion para mostrar opciones del menu'''
    print()
    print('Please choose one of the following options:')
    print()
    print('1. Create a task.')
    print('2. Mark a task as done.')
    print('3. Erase a task.')
    print('4. Exit.')

def showTodoList():
    '''Funcion para mostrar la lista de tareas'''
    global todoList
    print()
    print('************************************')
    for tarea in todoList:
        print(f'{todoList.index(tarea)+1}. {tarea}')
    print('************************************')
    print()

def createTodoList():
    '''Funcion para mostrar la lista de tareas'''
    os.system('clear') # WIndows => os.system('cls')
    global todoList
    print('Create new task...')
    todo = input('Please, enter your task: ')
    todoList.append(todo)
    # Mostrar la lista de tareas
    showTodoList()

def updateTodoList():
    '''Funcion para marcar una tarea como realizada'''
    global todoList
    print('Mark a task as done...')
    todoId = int(input("Enter the number of the task you've done: "))
    todoList[todoId-1] = todoList[todoId-1] + "✔️"
    showTodoList()

def deleteTodoList():
    '''Funcion para borrar una tarea'''
    global todoList
    print('Delete a task...')
    todoId = int(input("Enter the number of the task you want to delete: "))
    del todoList[todoId-1]
    showTodoList()

def main():
    global runProgram
    print('...: WELCOME TO A PYTHON TO-DO LIST :...')
    while runProgram:
        try:
            showMenuOptions() # Llamado de la funcion para mostrar menu
            option = int(input('Please, select a number from the list above:'))
            match option:
                case 1:
                    createTodoList()
                case 2:
                    updateTodoList()
                case 3:
                    deleteTodoList()
                case 4:
                    os.system('clear') # WIndows => os.system('cls')
                    runProgram = False
                    print('Goodbye, see you soon!')
                    print('...: CLOSING THE PYTHON TO-DO LIST :...\n')
                case _:
                    os.system('clear') # WIndows => os.system('cls')
                    print('Not valid choice. Please, select a valid option from 1 to 4.')
        except ValueError:
            os.system('clear') # WIndows => os.system('cls')
            print('Please, enter just numbers!')
            print()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nProgram ended by the user!')
        print('...: CLOSING THE PYTHON TO-DO LIST :...\n')
