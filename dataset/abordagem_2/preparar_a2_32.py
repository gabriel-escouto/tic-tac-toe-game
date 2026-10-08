
from pathlib import Path
import pandas as pd

# Abordagem 2
# Características calculadas a partir do tabuleiro

PASTA_32 = Path(__file__).resolve().parent
DATASET_32 = PASTA_32.parent

COLUNAS_32 = [
    "tl", "tm", "tr",
    "ml", "mm", "mr",
    "bl", "bm", "br"
]

# Linhas, colunas e diagonais do jogo
COMBINACOES_32 = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]

SEMENTE_32 = 42


def extrair_caracteristicas_32(tabuleiro):

    tabuleiro = tuple(tabuleiro)

    quantidade_x = tabuleiro.count("x")
    quantidade_o = tabuleiro.count("o")

    caracteristicas = {
        "quantidade_x": quantidade_x,
        "quantidade_o": quantidade_o
    }

    # Posições ocupadas: 1 = ocupada, 0 = vazia
    for posicao, nome in enumerate(COLUNAS_32):
        caracteristicas[f"ocupada_{nome}"] = int(
            tabuleiro[posicao] != "b"
        )

    # Alinhamentos com exatamente duas marcas
    for jogador in ("x", "o"):

        caracteristicas[f"linhas_com_2_{jogador}"] = sum(
            sum(
                tabuleiro[posicao] == jogador
                for posicao in combinacao
            ) == 2
            for combinacao in COMBINACOES_32
        )

    # Quantidade de casas vazias
    caracteristicas["casas_vazias"] = tabuleiro.count("b")

    # Próximo jogador, considerando X como primeiro
    caracteristicas["jogador_da_vez"] = (
        1 if quantidade_x == quantidade_o else -1
    )

    return caracteristicas


def preparar_abordagem_2_32(dados):

    # Verificar valores das nove posições
    if not dados[COLUNAS_32].isin(["x", "o", "b"]).all().all():
        raise ValueError("Há valores inválidos no tabuleiro.")

    # Calcular características de cada tabuleiro
    registros = [
        extrair_caracteristicas_32(tabuleiro)
        for tabuleiro in dados[COLUNAS_32].itertuples(
            index=False,
            name=None
        )
    ]

    resultado = pd.DataFrame(registros)

    # Manter a classe original como saída esperada
    resultado["classe"] = dados["classe"].to_numpy()

    return resultado


def balancear_treino_32(dados):

    maior_classe = dados["classe"].value_counts().max()
    partes = []

    for classe, grupo in dados.groupby("classe"):
        partes.append(
            grupo.sample(
                n=maior_classe,
                replace=len(grupo) < maior_classe,
                random_state=SEMENTE_32
            )
        )

    return (
        pd.concat(partes)
        .sample(frac=1, random_state=SEMENTE_32)
        .reset_index(drop=True)
    )


def executar_32():

    for nome in ["treino", "validacao", "teste"]:

        # Ler os dados originais
        entrada = DATASET_32 / f"{nome}.csv"
        dados = pd.read_csv(entrada)

        # Balancear somente o treino
        if nome == "treino":
            dados = balancear_treino_32(dados)

        # Preparar a Abordagem 2
        dados_a2 = preparar_abordagem_2_32(dados)

        # Salvar CSV processado
        saida = PASTA_32 / f"{nome}.csv"
        dados_a2.to_csv(saida, index=False)

        print(f"\n{nome.upper()}")
        print(f"Registros: {len(dados_a2)}")
        print(dados_a2["classe"].value_counts())

    print("\nAbordagem 2 concluída!")


if __name__ == "__main__":
    executar_32()
