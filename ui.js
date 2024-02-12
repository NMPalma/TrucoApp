// ui.js

// Función para actualizar la interfaz del juego con las cartas repartidas
function actualizarInterfaz(manoJugador1, manoJugador2) {
    // Obtener contenedores de cartas del NPC y el jugador
    const npcHand = document.getElementById('npc-hand');
    const playerHand = document.getElementById('player-hand');

    // Función auxiliar para crear un elemento de carta
    function crearCartaElemento(carta, jugador) {
        const cartaElemento = document.createElement('div');
        cartaElemento.classList.add('card');
        cartaElemento.dataset.palo = carta.palo;
        cartaElemento.dataset.numero = carta.numero;
        cartaElemento.dataset.jugador = jugador;
        // Crear la ruta de la imagen correspondiente a la carta
        const imagenSrc = `img/${carta.palo.toLowerCase()}-${carta.numero}.png`; // Suponiendo que las imágenes siguen la convención de nombres

        // Agregar la imagen como fondo del elemento de la carta
        cartaElemento.style.backgroundImage = `url(${imagenSrc})`;
        cartaElemento.addEventListener('click', () => {
            jugarCarta(cartaElemento);
        });

        return cartaElemento;
    }

    function jugarCarta(cartaElemento) {
        const mesaJugador = document.getElementById(cartaElemento.dataset.jugador + '-played-cards');
        const espacioMesa = mesaJugador.querySelector('.card-placeholder');

        // Mover la carta a la mesa
        espacioMesa.appendChild(cartaElemento);
    }

    // Actualizar la mano del NPC
    for (let i = 0; i < manoJugador1.length; i++) {
        const carta = manoJugador1[i];
        const cartaElemento = crearCartaElemento(carta);
        npcHand.appendChild(cartaElemento);
    }

    // Actualizar la mano del jugador
    for (let i = 0; i < manoJugador2.length; i++) {
        const carta = manoJugador2[i];
        const cartaElemento = crearCartaElemento(carta);
        playerHand.appendChild(cartaElemento);
    }
}

export { actualizarInterfaz };
