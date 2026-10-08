
# T1 — Jogo da Velha com Inteligência Artificial

Trabalho desenvolvido para a disciplina de **Inteligência Artificial**, do curso de Sistemas de Informação da PUCRS.

## 1. Objetivo

O objetivo do trabalho é desenvolver e avaliar algoritmos de aprendizado de máquina capazes de classificar o estado de um tabuleiro de Jogo da Velha.

Os tabuleiros são classificados em quatro categorias:

- **Tem jogo:** a partida ainda não terminou.
- **X venceu:** o jogador X completou uma combinação vencedora.
- **O venceu:** o jogador O completou uma combinação vencedora.
- **Empate:** o tabuleiro está completo e não existe vencedor.

Além dos experimentos com os classificadores, o projeto possui uma interface interativa na qual o usuário joga contra um computador que realiza jogadas aleatórias.

Após cada jogada, o algoritmo selecionado analisa o tabuleiro e prevê seu estado.

## 2. Algoritmos

O trabalho contempla cinco algoritmos de classificação:

1. K-Nearest Neighbors (KNN)
2. Multilayer Perceptron (MLP)
3. Árvore de Decisão
4. Random Forest
5. Boosting

Cada algoritmo deve ser avaliado utilizando as duas abordagens de representação dos dados.

**Situação atual:** o KNN já foi implementado e integrado ao jogo. Os demais algoritmos estão em desenvolvimento pelos integrantes do grupo.

## 3. Dataset

O projeto utiliza conjuntos de dados de estados do Jogo da Velha, divididos em:

- `treino.csv`: treinamento dos modelos.
- `validacao.csv`: seleção de parâmetros e comparação de configurações.
- `teste.csv`: avaliação final dos modelos.

Os dados originais estão na pasta `dataset/`.

Foram preparadas duas abordagens para representar os tabuleiros.

### 3.1. Abordagem 1 — Representação das casas

Cada tabuleiro é representado por nove atributos, correspondentes às nove posições do jogo.

Os símbolos são convertidos em valores numéricos:

- X = 1
- O = -1
- Casa vazia = 0

Os arquivos dessa abordagem estão em `dataset/abordagem_1/`.

### 3.2. Abordagem 2 — Características derivadas

Nesta abordagem, cada tabuleiro é representado por 15 características:

- Quantidade de símbolos X.
- Quantidade de símbolos O.
- Indicadores de ocupação das nove casas.
- Quantidade de linhas com dois símbolos X.
- Quantidade de linhas com dois símbolos O.
- Quantidade de casas vazias.
- Indicador do próximo jogador.

Os arquivos estão em `dataset/abordagem_2/`.

O conjunto de treinamento passou por balanceamento das classes utilizando oversampling. Os conjuntos de validação e teste foram mantidos sem esse balanceamento.

## 4. Implementação do KNN

O KNN foi implementado em Python utilizando a biblioteca Scikit-learn.

Foram testados os valores de K:

`1, 3, 5, 7, 9, 11, 15 e 21`

Foi utilizado `StandardScaler` para padronizar os atributos antes da classificação.

A escolha da melhor configuração considerou o **F1 macro no conjunto de validação**.

### 4.1. Resultados

| Métrica | Resultado |
|---|---:|
| Melhor abordagem | Abordagem 2 |
| Melhor valor de K | 9 |
| F1 macro na validação | 0,8168 |
| Acurácia no teste | 82,80% |
| Precisão macro no teste | 0,7981 |
| Recall macro no teste | 0,8667 |
| F1 macro no teste | 0,8050 |

O modelo classificou corretamente 77 dos 93 exemplos do conjunto de teste.

### 4.2. Análise de overfitting

Para investigar possíveis sinais de overfitting, o KNN foi avaliado nos três conjuntos de dados.

| Conjunto | F1 macro |
|---|---:|
| Treinamento | 0,8957 |
| Validação | 0,8168 |
| Teste | 0,8050 |

O desempenho foi superior no treinamento, indicando uma possível tendência ao overfitting.

Entretanto, os resultados de validação e teste foram próximos, sugerindo desempenho relativamente consistente nos conjuntos não utilizados durante o treinamento.

O notebook `algoritmos/knn/knn.ipynb` apresenta os experimentos, o gráfico comparativo, a análise dos resultados e a conclusão.

## 5. Interface do jogo

A interface foi desenvolvida com:

- HTML
- CSS
- JavaScript
- Flask (Python)

O usuário controla o jogador **X**, enquanto o computador controla o jogador **O**, realizando jogadas aleatórias.

O objetivo do classificador não é escolher a melhor jogada, mas identificar o estado do tabuleiro.

### 5.1. Integração com os modelos

O Flask funciona como servidor local e permite a comunicação entre o JavaScript e os algoritmos Python.

O funcionamento ocorre da seguinte forma:

1. O usuário ou o computador realiza uma jogada.
2. O JavaScript envia o tabuleiro ao servidor Flask.
3. O servidor prepara os atributos utilizados pelo modelo.
4. O classificador realiza uma previsão.
5. O servidor devolve a classificação ao frontend.
6. A interface compara a previsão com o estado real do tabuleiro.

Atualmente, a integração está disponível para o KNN.

### 5.2. Avaliação durante as partidas

A interface apresenta:

- Estado real do tabuleiro.
- Previsão realizada pelo algoritmo.
- Quantidade de classificações corretas.
- Quantidade de classificações incorretas.
- Acurácia acumulada durante as partidas.
- Placar de vitórias e empates.

A acurácia é calculada por:

`Acurácia = Acertos / (Acertos + Erros) × 100`

A classificação é realizada após cada jogada, inclusive nas jogadas do computador.

Quando o classificador indica incorretamente que a partida terminou, o erro é contabilizado e o jogo pode continuar.

Quando existe um resultado final real, a partida é encerrada, mesmo que o classificador não reconheça corretamente esse estado.

## 6. Estrutura do projeto

```text
tic-tac-toe-game/
├── algoritmos/
│   └── knn/
│       ├── knn.py
│       ├── knn.ipynb
│       └── knn_comparacao_abordagens.png
├── dataset/
│   ├── abordagem_1/
│   ├── abordagem_2/
│   ├── treino.csv
│   ├── validacao.csv
│   └── teste.csv
├── front_end/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── relatorio/
│   └── relatorio_t1.md
├── app.py
└── .gitignore
```

## 7. Como executar o projeto

### 7.1. Requisitos

- Python 3
- Bibliotecas Flask, Pandas e Scikit-learn
- Navegador web

### 7.2. Clonar o repositório

```bash
git clone https://github.com/jesalvatori/tic-tac-toe-game.git
cd tic-tac-toe-game
```

### 7.3. Criar o ambiente virtual

No macOS ou Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 7.4. Instalar as dependências

```bash
python -m pip install flask pandas scikit-learn
```

### 7.5. Iniciar o servidor Flask

```bash
python app.py
```

O servidor será iniciado localmente.

Abra no navegador:

http://127.0.0.1:5000

### 7.6. Jogar

1. Selecione o algoritmo KNN.
2. Clique em uma casa vazia para marcar X.
3. Aguarde a jogada aleatória do computador.
4. Acompanhe as previsões e métricas da IA.
5. Clique em **Nova partida** para jogar novamente.

## 8. Etapas pendentes

- Finalizar os outros quatro algoritmos.
- Integrar os modelos restantes ao Flask.
- Comparar o desempenho dos cinco classificadores.
- Registrar os resultados dos testes interativos.
- Completar o relatório final do grupo.

## 9. Repositório

https://github.com/jesalvatori/tic-tac-toe-game
