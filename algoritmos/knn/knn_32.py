
from pathlib import Path

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

RAIZ_32 = Path(__file__).resolve().parents[2]
VALORES_K_32 = [1, 3, 5, 7, 9, 11, 15, 21]

CLASSES_32 = [
    "Tem jogo",
    "X venceu",
    "O venceu",
    "Empate"
]


def carregar_dados_32(abordagem):
    pasta = RAIZ_32 / "dataset" / abordagem

    treino = pd.read_csv(pasta / "treino.csv")
    validacao = pd.read_csv(pasta / "validacao.csv")
    teste = pd.read_csv(pasta / "teste.csv")

    return treino, validacao, teste


def separar_dados_32(dados):
    X = dados.drop(columns=["classe"])
    y = dados["classe"]
    return X, y


def criar_modelo_32(k):
    return Pipeline([
        ("normalizacao", StandardScaler()),
        ("knn", KNeighborsClassifier(n_neighbors=k))
    ])


def executar_32():
    melhor_f1_32 = -1
    melhor_k_32 = None
    melhor_abordagem_32 = None
    melhor_modelo_32 = None

    for abordagem_32 in ["abordagem_1", "abordagem_2"]:
        treino, validacao, _ = carregar_dados_32(abordagem_32)

        X_treino, y_treino = separar_dados_32(treino)
        X_validacao, y_validacao = separar_dados_32(validacao)

        print(f"\n{abordagem_32.upper()}")

        for k_32 in VALORES_K_32:
            modelo_32 = criar_modelo_32(k_32)
            modelo_32.fit(X_treino, y_treino)

            previsoes_32 = modelo_32.predict(X_validacao)

            f1_32 = f1_score(
                y_validacao,
                previsoes_32,
                average="macro",
                zero_division=0
            )

            print(f"K = {k_32} | F1 macro = {f1_32:.4f}")

            if f1_32 > melhor_f1_32:
                melhor_f1_32 = f1_32
                melhor_k_32 = k_32
                melhor_abordagem_32 = abordagem_32
                melhor_modelo_32 = modelo_32

    print("\nMELHOR CONFIGURACAO DO KNN")
    print(f"Abordagem: {melhor_abordagem_32}")
    print(f"K: {melhor_k_32}")
    print(f"F1 macro na validacao: {melhor_f1_32:.4f}")

    _, _, teste = carregar_dados_32(melhor_abordagem_32)
    X_teste, y_teste = separar_dados_32(teste)

    previsoes_teste_32 = melhor_modelo_32.predict(X_teste)

    acuracia_32 = accuracy_score(y_teste, previsoes_teste_32)
    precisao_32 = precision_score(
        y_teste, previsoes_teste_32,
        average="macro", zero_division=0
    )
    recall_32 = recall_score(
        y_teste, previsoes_teste_32,
        average="macro", zero_division=0
    )
    f1_teste_32 = f1_score(
        y_teste, previsoes_teste_32,
        average="macro", zero_division=0
    )

    print("\nRESULTADOS NO TESTE")
    print(f"Acuracia: {acuracia_32:.4f}")
    print(f"Precisao macro: {precisao_32:.4f}")
    print(f"Recall macro: {recall_32:.4f}")
    print(f"F1 macro: {f1_teste_32:.4f}")

    print("\nRELATORIO POR CLASSE")
    print(classification_report(
        y_teste,
        previsoes_teste_32,
        labels=CLASSES_32,
        zero_division=0
    ))

    print("\nMATRIZ DE CONFUSAO")
    print("Ordem das classes:", CLASSES_32)
    print(confusion_matrix(
        y_teste,
        previsoes_teste_32,
        labels=CLASSES_32
    ))


if __name__ == "__main__":
    executar_32()
