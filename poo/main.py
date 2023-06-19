# Ejemplo de Clase
class Usuario():
    # Datos (atributos)
    # Constructor
    def __init__(self, nombre, apellido, correo, clave, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.clave = clave
        self.telefono = telefono
    
    # Funcionalidad (metodos)
    def encriptarClave(self):
        return 'encriptando...'
    
    def verificarClave(self):
        return 'desencriptando...'

print('Usuario #1')
usuario1 = Usuario(
    nombre='Ivan', 
    apellido='Iglesias', 
    correo='ivan@ed.team', 
    clave='prueba', 
    telefono='3490374'
    )
print(usuario1.nombre + ' ' + usuario1.apellido)

print('Usuario #2')
usuario2 = Usuario(
    nombre='John', 
    apellido='Doe', 
    correo='john.doe@ed.team', 
    clave='test', 
    telefono='1234567'
    )
print(usuario2.nombre + ' ' + usuario2.apellido)