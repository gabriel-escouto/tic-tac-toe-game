
from pathlib import Path
import pandas as pd

# Abordagem 1
# Representação numérica das nove casas do tabuleiro

PASTA_32 = Path(__file__).resolve().parent
DATASET_32 = PASTA_32.parent

COLUNAS_32 = [
    "tl", "tm", "tr",
    "ml", "mm", "mr",
    "bl", "bm", "br"
]

CODIFICACAO_32 = {
    "x": 1,
    "o": -1,
    "b": 0
}

SEMENTE_32 = 42


def preparar_abordagem_1_32(dados):
    """Converte as nove posições em valores numéricos."""

    resultado = dados.copy()

    for coluna in COLUNAS_32:
        resultado[coluna] = resultado[coluna].map(CODIFICACAO_32)

    if resultado[COLUNAS_32].isna().any().any():
        raise ValueError("Há valores inválidos no tabuleiro.")

    return resultado


def balancear_treino_32(dados):
    """Equilibra as classes somente no conjunto de treino."""

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

        # Leitura do dataset original
        entrada = DATASET_32 / f"{nome}.csv"
        dados = pd.read_csv(entrada)

        # Balanceamento apenas do treino
        if nome == "treino":
            dados = balancear_treino_32(dados)

        # Aplicação da Abordagem 1
        dados_a1 = preparar_abordagem_1_32(dados)

        # Exportação
        saida = PASTA_32 / f"{nome}.csv"
        dados_a1.to_csv(saida, index=False)

        print(f"\n{nome.upper()}")
        print(f"Registros: {len(dados_a1)}")
        print(dados_a1["classe"].value_counts())

    print("\nAbordagem 1 concluída!")


if __name__ == "__main__":
    executar_32()
