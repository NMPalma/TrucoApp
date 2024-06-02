import random


class Carta:
    def __init__(self, palo, numero):
        self.palo = palo
        self.numero = numero

    def __repr__(self):
        return f'{self.numero} de {self.palo}'


class Mazo:
    def __init__(self):
        self.cartas = []
        self.crear_mazo()

    def crear_mazo(self):
        palos = ['Espada', 'Basto', 'Oro', 'Copa']  # Palos disponibles
        numeros = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]  # Valores de las cartas

        for palo in palos:
            for numero in numeros:
                # Crear una carta para cada combinación de palo y valor
                self.cartas.append(Carta(palo, numero))

    def mezclar(self):
        random.shuffle(self.cartas)  # Mezclar las cartas aleatoriamente

    def repartir_carta(self):
        if len(self.cartas) == 0:
            # Lanzar un error si el mazo está vacío
            raise ValueError('¡El mazo está vacío!')
        return self.cartas.pop()  # Sacar la última carta de la lista y devolverla


# Ejemplo de uso
mazo = Mazo()
mazo.mezclar()

# Repartir cartas
mis_cartas = [mazo.repartir_carta() for _ in range(3)]
cartas_oponente = [mazo.repartir_carta() for _ in range(3)]

print("Mis cartas:", mis_cartas)
print("Cartas del oponente:", cartas_oponente)
