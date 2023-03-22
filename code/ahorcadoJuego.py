import random
IMAGENES_AHORCADO = ['''
   +---+
   |   |
       |
       |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
       |
       |
       |
 =========''','''
   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''',''' 
   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''','''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''','''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''','''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']

palabras = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro ' \
           'burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra ' \
           'nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta ' \
           'perezoso serpiente araña narval cisne tigre sapo trucha pavo tortuga comadreja ' \
           'ballena lobo wombat cebra'.split()

def obtenerPalabraAlAzar(listaDePalabras):
    índiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
    return listaDePalabras[índiceDePalabras]

def mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(IMAGENES_AHORCADO[len(letrasIncorrectas)])
    print()

    print('Letras incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print(letra, end=' ')
    print()

    espaciosVacíos = '_' * len(palabraSecreta)
    for i in range(len(palabraSecreta)):
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[i] + espaciosVacíos[i + 1:]

    for letra in espaciosVacíos:
        print(letra, end=' ')
    print()

def obtenerIntento(letrasProbadas):
    while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Por favor, introduce una sola letra.')
        elif intento in letrasProbadas:
            print('Ya probaste esa letra. Elige otra.')
        elif intento not in 'abcdefghijklmnopqrstuvwxyz':
            print('Por favor ingresa una LETRA!')
        else:
            return intento

def jugarDeNuevo():
    print('¿Quieres jugar de nuevo? (sí o no)')
    return input().lower().startswith('s')

print('     A H O R C A D O     ')
letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta = obtenerPalabraAlAzar(palabras)
juegoTerminado = False

while True:
    mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)

    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)

    if intento in palabraSecreta:

        letrasCorrectas = letrasCorrectas + intento

        # Verifica si el jugador ha ganado.
        encontradoTodasLasLetras = True

        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                juegoTerminado = False
                encontradoTodasLasLetras = False
                break

        if encontradoTodasLasLetras:
            juegoTerminado = True
            print('¡Sí! ¡La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')

    else:
        letrasIncorrectas = letrasIncorrectas + intento

        # Comprobar si el jugador ha agotado sus intentos y ha perdido.
        if len(letrasIncorrectas) == (len(IMAGENES_AHORCADO) - 1):
            mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print('¡Te has quedado sin intentos!\nDespués de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' +
                  str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"')
            juegoTerminado = True

    # Preguntar al jugador si quiere volver a jugar (pero sólo si el juego ha terminado).
    if juegoTerminado:
        if jugarDeNuevo():
            letrasIncorrectas = ''
            letrasCorrectas = ''
            juegoTerminado = False
            palabraSecreta = obtenerPalabraAlAzar(palabras)
        else:
            break
