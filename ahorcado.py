"""JUEGO DEL AHORCADO
"""

# palabra a adivinar
PALABRA_A_ADIVINAR = 'elefante'

# almacena numero de entradas erroneas
strikes = 0

# almacena entradas conforme se van ingresando
entradas = []

# lista que representa la palabra escondida, inicialmente es
# un _ por cada caracter en PALABRA_A_ADIVINAR
palabra_escondida = ['_' for c in PALABRA_A_ADIVINAR]

# diccionario de elementos i:c donde i es el índice de cada caracter c
# en PALABRA_A_ADIVINAR:
# {0:'e', 1:'l', 2:'e', 3:'f', 4:'a', 5:'n', 6:'t', 7:'e'}
dict_indice_letra = {i: PALABRA_A_ADIVINAR[i] for i in range(len(PALABRA_A_ADIVINAR))}



# tupla que almacena los dibujitos, los strikes serán los índices
# de esta tupla, si aumenta el strike, muestra el siguiente muñequito
dibujitos = (
    """
    _____   
    |    |
         |
         |
         |
         |
        ===
    """,

    """
    _____   
    |    |
    O    |
         |
         |
         |
        ===
    """,

    """
    _____   
    |    |
    O    |
    |    |
         |
         |
        ===
    """,

    """
    _____   
    |    |
    O    |
   /|    |
         |
         |
        ===
    """,

    """
    _____   
    |    |
    O    |
   /|\   |
         |
         |
        ===
    """,

    """
    _____   
    |    |
    O    |
   /|\   |
    |    |
         |
        ===
    """,

    """
    _____   
    |    |
    O    |
   /|\   |
    |    |
   /     |
        ===
    """,

    """
    _____   
    |    |
    X    |
   /|\   |
    |    |
   / \   |
        ===
    ESTAS MUERTO!
    """
)

# repite mientras que el número de strikes sea menor a los
# dibujitos que tengamos disponibles
while strikes < len(dibujitos):

    # imprime un salto de linea
    print()

    # pinta el muñequito y la palabra escondida
    print(dibujitos[strikes])
    print(palabra_escondida)

    # si se llegan a 7 strikes, se rompe el bucle
    if strikes == 7:
        break

    # entrada de datos
    entrada = input("Ingrese letra: ")
    
    # si entrada no está en, se aumenta el strike
    if entrada not in PALABRA_A_ADIVINAR:
        strikes += 1
    else:
        indices_a_cambiar = [i for i in dict_indice_letra.keys() if entrada == dict_indice_letra.get(i)]
        for i in indices_a_cambiar:
            palabra_escondida[i] = entrada

    # verifica si lo que se ingresó no se había ingreado previamente
    if entrada not in entradas:
        entradas.append(entrada)
    else:
        print(f'La letra {entrada} ya la habías ingresado...')
        input('\nPresiona enter para continua. . . ')

    # verificacion si eres genador
    if '_' not in palabra_escondida:
        print('GANASTE!')
        break


# fin del programa
input('\nPresiona una tecla para continuar. . . ')
