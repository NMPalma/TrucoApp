import random


class Carta:
    def __init__(self, palo, numero):
        self.palo = palo
        self.numero = numero
        self.valor = self.obtener_valor()

    def __repr__(self):
        return f'{self.numero} de {self.palo}'

    def obtener_valor(self):
        valores = {
            1: 8, 2: 9, 3: 10, 4: 1, 5: 2, 6: 3, 7: 4, 10: 5, 11: 6, 12: 7
        }
        valores_espada = {1: 14, 7: 13}
        valores_basto = {1: 13}
        valores_oro = {7: 12}
        if self.palo == 'Espada' and self.numero in valores_espada:
            return valores_espada[self.numero]
        elif self.palo == 'Basto' and self.numero in valores_basto:
            return valores_basto[self.numero]
        elif self.palo == 'Oro' and self.numero in valores_oro:
            return valores_oro[self.numero]
        return valores[self.numero]


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


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cartas = []
        self.puntos = 0
        self.cartas_jugadas = []
        self.envido_cantado = False
        self.truco_cantado = False

    def recibir_cartas(self, cartas):
        self.cartas = cartas

    def mostrar_cartas(self):
        return self.cartas

    def jugar_carta(self, indice):
        carta = self.cartas.pop(indice)
        self.cartas_jugadas.append(carta)
        return carta

    def __repr__(self):
        return self.nombre

    def cantar_envido(self):
        return "Envido"

    def cantar_truco(self):
        return "Truco"


class Truco:
    def __init__(self, nombre_jugador_usuario, num_jugadores, puntos_objetivo):
        self.mazo = Mazo()
        self.mazo.mezclar()
        self.jugadores = [Jugador(nombre_jugador_usuario)] + \
            [Jugador(f"Oponente {i+1}") for i in range(num_jugadores - 1)]
        self.turno_actual = random.choice(self.jugadores)
        self.puntos_objetivo = puntos_objetivo
        self.mesa = []
        self.ronda_actual = 1
        self.puntos_ronda = [0, 0, 0]
        self.apuesta_envido = 0
        self.apuesta_truco = 1

    def repartir_cartas(self):
        for jugador in self.jugadores:
            jugador.recibir_cartas([self.mazo.repartir_carta()
                                   for _ in range(3)])

    def mostrar_mis_cartas(self, jugador):
        return jugador.mostrar_cartas()

    def alternar_turno(self):
        indice_actual = self.jugadores.index(self.turno_actual)
        self.turno_actual = self.jugadores[(
            indice_actual + 1) % len(self.jugadores)]

    def opciones_turno(self, jugador):
        if jugador == self.turno_actual:
            opciones = ["Jugar carta"]
            if not jugador.envido_cantado:
                opciones.append("Cantar Envido")
            if not jugador.truco_cantado:
                opciones.append("Cantar Truco")
            opciones.append("Pasar")
            return opciones
        else:
            return []

    def mostrar_mesa(self):
        print("Mesa:")
        for jugada in self.mesa:
            print(f"{jugada[0].nombre}: {jugada[1]}")
        print("")

    def comparar_cartas(self, carta1, carta2):
        if carta1.valor > carta2.valor:
            return 1
        elif carta1.valor < carta2.valor:
            return -1
        else:
            return 0

    def determinar_ganador_ronda(self):
        jugadas = [jugada[1] for jugada in self.mesa]
        if len(jugadas) == 2:
            resultado = self.comparar_cartas(jugadas[0], jugadas[1])
            if resultado == 1:
                self.puntos_ronda[self.ronda_actual - 1] = 1
            elif resultado == -1:
                self.puntos_ronda[self.ronda_actual - 1] = -1
            else:
                self.puntos_ronda[self.ronda_actual - 1] = 0
            self.mesa = []

    def jugar(self):
        self.repartir_cartas()
        print(f"Turno inicial: {self.turno_actual}")
        print(f"Mis cartas: {self.mostrar_mis_cartas(self.jugadores[0])}")
        # No mostramos las cartas del oponente para mantenerlas ocultas

        while max(self.puntos_ronda) < 2 and min(self.puntos_ronda) > -2:
            print(f"Ronda {self.ronda_actual}")
            for _ in range(len(self.jugadores)):
                print(f"Turno de: {self.turno_actual}")
                if self.turno_actual == self.jugadores[0]:
                    opciones = self.opciones_turno(self.turno_actual)
                    print(f"Opciones disponibles: {opciones}")
                    eleccion = input("Elija una opción: ").strip().lower()
                    carta_jugada = None
                    if eleccion == "jugar carta":
                        carta_jugada = self.turno_actual.jugar_carta(
                            0)  # Ejemplo de jugar la primera carta
                    elif eleccion == "cantar envido":
                        print("Has cantado Envido")
                        self.turno_actual.envido_cantado = True
                    elif eleccion == "cantar truco":
                        print("Has cantado Truco")
                        self.turno_actual.truco_cantado = True
                    elif eleccion == "pasar":
                        print("Has pasado")
                        continue
                else:
                    # Inteligencia artificial para seleccionar una carta
                    carta_jugada = self.jugar_carta_oponente(self.turno_actual)
                if carta_jugada:
                    self.mesa.append((self.turno_actual, carta_jugada))
                    self.mostrar_mesa()
                self.alternar_turno()
            self.determinar_ganador_ronda()
            self.ronda_actual += 1
        ganador = "Usuario" if self.puntos_ronda.count(
            1) > self.puntos_ronda.count(-1) else "Oponente"
        print(f"El ganador de la ronda es: {ganador}")

    def jugar_carta_oponente(self, oponente):
        # Selecciona la mejor carta disponible (lógica simple)
        mejor_carta = max(oponente.cartas, key=lambda carta: carta.valor)
        oponente.cartas.remove(mejor_carta)
        return mejor_carta


# Ejemplo de uso
nombre_jugador_usuario = input("Ingrese su nombre: ")
num_jugadores = int(
    input("Ingrese el número total de jugadores (incluyéndote a ti): "))
while True:
    puntos_objetivo = int(
        input("Ingrese los puntos a los que será la partida (15 o 30): "))
    if puntos_objetivo in [15, 30]:
        break
    else:
        print("Puntos no válidos. Por favor, ingrese 15 o 30.")

juego = Truco(nombre_jugador_usuario, num_jugadores, puntos_objetivo)
juego.jugar()
