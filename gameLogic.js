// gameLogic.js
class Carta {
    constructor(palo, numero) {
        this.palo = palo; // Palo de la carta (espadas, bastos, etc.)
        this.numero = numero; // Valor de la carta (1 al 12 para el truco)
    }
}

class Mazo {
    constructor() {
        this.cartas = []; // Array para almacenar las cartas del mazo
        this.crearMazo(); // Método para crear el mazo al instanciar un objeto Mazo
    }

    // Método para crear el mazo
    crearMazo() {
        const palos = ['Espada', 'Basto', 'Oro', 'Copa']; // Palos disponibles
        const numeros = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]; // Valores de las cartas

        for (let palo of palos) {
            for (let numero of numeros) {
                this.cartas.push(new Carta(palo, numero)); // Crear una carta para cada combinación de palo y valor
            }
        }
    }

    // Método para barajar el mazo
    mezclar() {
        for (let i = this.cartas.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [this.cartas[i], this.cartas[j]] = [this.cartas[j], this.cartas[i]]; // Intercambiar cartas aleatoriamente
        }
    }

    // Método para repartir una carta del mazo
    repartirCarta() {
        if (this.cartas.length === 0) {
            throw new Error('¡El mazo está vacío!');
        }
        return this.cartas.pop(); // Sacar la última carta del array y devolverla
    }
}

// Exportar la clase Mazo
export { Carta, Mazo };
