import { Carta, Mazo } from './gameLogic.js';
import { actualizarInterfaz } from './ui.js';
import { tomarDecision } from './npcLogic.js';

function repartirCartas(mazo) {
    const jugador1 = []; // Mano del primer jugador
    const jugador2 = []; // Mano del segundo jugador

    for (let i = 0; i < 3; i++) {
        jugador1.push(mazo.repartirCarta()); // Agregar carta a la mano del primer jugador
        jugador2.push(mazo.repartirCarta()); // Agregar carta a la mano del segundo jugador
    }

    return [jugador1, jugador2]; // Devolver las manos de los jugadores como un array
}

// Lógica principal del juego
const mazo = new Mazo();
mazo.mezclar(); // Barajar el mazo

const [manoJugador1, manoJugador2] = repartirCartas(mazo);

console.log('Mano del jugador 1:', manoJugador1);
console.log('Mano del jugador 2:', manoJugador2);
actualizarInterfaz(manoJugador1, manoJugador2);
tomarDecision();
