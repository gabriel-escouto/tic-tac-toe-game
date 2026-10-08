
const casas = document.querySelectorAll(".casa");
const mensagem = document.getElementById("mensagem");
const estado = document.getElementById("estado");
const previsao = document.getElementById("previsao");
const botaoReiniciar = document.getElementById("reiniciar");

const seletorAlgoritmo = document.getElementById("algoritmo");
const statusModelo = document.getElementById("status-modelo");

const campoVitoriasX = document.getElementById("vitorias-x");
const campoVitoriasO = document.getElementById("vitorias-o");
const campoEmpates = document.getElementById("empates");

let tabuleiro = Array(9).fill("");
let jogoFinalizado = false;
let vezComputador = false;
let temporizadorComputador = null;

let vitoriasX = 0;
let vitoriasO = 0;
let empates = 0;

const combinacoesVitoria = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
];

function verificarEstado() {
    for (const [a, b, c] of combinacoesVitoria) {
        if (
            tabuleiro[a] !== "" &&
            tabuleiro[a] === tabuleiro[b] &&
            tabuleiro[b] === tabuleiro[c]
        ) {
            return tabuleiro[a] === "X"
                ? "X venceu"
                : "O venceu";
        }
    }

    if (tabuleiro.every(casa => casa !== "")) {
        return "Empate";
    }

    return "Tem jogo";
}

function atualizarPlacar() {
    campoVitoriasX.textContent = vitoriasX;
    campoVitoriasO.textContent = vitoriasO;
    campoEmpates.textContent = empates;
}

function atualizarSelecao() {
    const nome = seletorAlgoritmo.options[
        seletorAlgoritmo.selectedIndex
    ].text;

    statusModelo.textContent =
        `${nome} — aguardando integração com Python`;

    previsao.textContent = "Não disponível";
}

function finalizarPartida(resultado) {
    if (jogoFinalizado) return;

    jogoFinalizado = true;

    if (resultado === "X venceu") {
        vitoriasX++;
        mensagem.textContent = "Parabéns! Você venceu!";
    } else if (resultado === "O venceu") {
        vitoriasO++;
        mensagem.textContent = "O computador venceu!";
    } else {
        empates++;
        mensagem.textContent = "A partida terminou empatada!";
    }

    atualizarPlacar();
}

function atualizarInterface() {
    const resultado = verificarEstado();

    if (resultado !== "Tem jogo") {
        finalizarPartida(resultado);
    }

    casas.forEach((casa, indice) => {
        casa.textContent = tabuleiro[indice];

        casa.classList.toggle(
            "x",
            tabuleiro[indice] === "X"
        );

        casa.classList.toggle(
            "o",
            tabuleiro[indice] === "O"
        );

        casa.disabled =
            jogoFinalizado ||
            vezComputador ||
            tabuleiro[indice] !== "";
    });

    estado.textContent = resultado;

    if (!jogoFinalizado) {
        mensagem.textContent = vezComputador
            ? "O computador está jogando..."
            : "Sua vez! Escolha uma casa.";
    }
}

function jogarComputador() {
    temporizadorComputador = null;

    if (jogoFinalizado) return;

    const disponiveis = [];

    tabuleiro.forEach((valor, indice) => {
        if (valor === "") {
            disponiveis.push(indice);
        }
    });

    if (disponiveis.length === 0) return;

    const sorteio = Math.floor(
        Math.random() * disponiveis.length
    );

    const posicao = disponiveis[sorteio];

    tabuleiro[posicao] = "O";
    vezComputador = false;

    atualizarInterface();
}

function jogarHumano(posicao) {
    if (
        jogoFinalizado ||
        vezComputador ||
        tabuleiro[posicao] !== ""
    ) {
        return;
    }

    tabuleiro[posicao] = "X";
    atualizarInterface();

    if (jogoFinalizado) return;

    vezComputador = true;
    atualizarInterface();

    temporizadorComputador = setTimeout(
        jogarComputador,
        500
    );
}

function reiniciarJogo() {
    if (temporizadorComputador !== null) {
        clearTimeout(temporizadorComputador);
        temporizadorComputador = null;
    }

    tabuleiro = Array(9).fill("");
    jogoFinalizado = false;
    vezComputador = false;

    atualizarInterface();
}

casas.forEach(casa => {
    casa.addEventListener("click", () => {
        const posicao = Number(casa.dataset.posicao);
        jogarHumano(posicao);
    });
});

botaoReiniciar.addEventListener(
    "click",
    reiniciarJogo
);

seletorAlgoritmo.addEventListener(
    "change",
    atualizarSelecao
);

atualizarSelecao();
atualizarPlacar();
atualizarInterface();
