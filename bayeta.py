import random

def frotar(n_frases):
    try:
        with open('frases.txt', 'r') as file:
            frases = [line.strip() for line in file]

        if n_frases <= 0:
            return []  # Devolver una lista vacía si n_frases es menor o igual a 0
        elif n_frases >= len(frases):
            return frases[:]  # Devolver todas las frases si n_frases es mayor o igual al tamaño de la lista
        else:
            frases_aleatorias = random.sample(frases, n_frases)
            return frases_aleatorias

    except FileNotFoundError:
        print("El archivo 'frases.txt' no fue encontrado.")
        return []