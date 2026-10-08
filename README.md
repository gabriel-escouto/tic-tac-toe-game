# T1 — Jogo da Velha com Inteligência Artificial

Trabalho desenvolvido para a disciplina de **Inteligência Artificial**, do curso de Sistemas de Informação da PUCRS.

## 1. Objetivo

Desenvolver e avaliar algoritmos de aprendizado de máquina capazes de classificar o estado de um tabuleiro de Jogo da Velha em quatro categorias:

- **Tem jogo:** a partida ainda não terminou.
- **X venceu:** o jogador X completou uma combinação vencedora.
- **O venceu:** o jogador O completou uma combinação vencedora.
- **Empate:** o tabuleiro está completo e não existe vencedor.

O projeto também possui uma interface interativa na qual o usuário joga contra o computador, que realiza jogadas aleatórias. Após cada jogada, o algoritmo selecionado prevê o estado do tabuleiro.

## 2. Algoritmos

| Algoritmo | Situação |
|---|---|
| K-Nearest Neighbors (KNN) | Implementado e integrado ao jogo |
| Multilayer Perceptron (MLP) | Em desenvolvimento |
| Árvore de Decisão | Em desenvolvimento |
| Random Forest | Em desenvolvimento |
| Boosting | Em desenvolvimento |

Cada algoritmo é avaliado nas duas abordagens de representação dos dados.

## 3. Dataset

Os dados estão divididos fisicamente em três arquivos, utilizados por todos os algoritmos:

- `treino.csv`: treinamento dos modelos.
- `validacao.csv`: seleção de parâmetros e comparação de configurações.
- `teste.csv`: avaliação final dos modelos.

Os arquivos originais estão em `dataset/`. A partir deles, foram geradas duas representações dos tabuleiros.

### 3.1. Abordagem 1 — Representação das casas

Nove atributos, um para cada posição do tabuleiro, com os símbolos convertidos em valores numéricos: X = 1, O = -1 e casa vazia = 0.

- Script: `dataset/abordagem_1/preparar_a1.py`
- Arquivos gerados: `dataset/abordagem_1/`

### 3.2. Abordagem 2 — Características derivadas

Quinze características calculadas a partir do tabuleiro: quantidade de X e de O, ocupação das nove casas, linhas com dois X, linhas com dois O, quantidade de casas vazias e indicador do próximo jogador.

- Script: `dataset/abordagem_2/preparar_a2.py`
- Arquivos gerados: `dataset/abordagem_2/`

Em ambas as abordagens, o balanceamento de classes é aplicado somente ao conjunto de treinamento.

## 4. Experimentos

Cada algoritmo possui uma pasta em `algoritmos/`, com o script de treinamento e um notebook contendo os experimentos, a seleção de parâmetros e a avaliação no conjunto de teste.

A análise completa e a comparação entre os classificadores estão em `relatorio/relatorio_t1.md`.

## 5. Interface do jogo

Desenvolvida com HTML, CSS e JavaScript, com Flask (Python) como servidor local.

O usuário controla o jogador **X** e o computador controla o jogador **O**, com jogadas aleatórias. O classificador não escolhe jogadas: sua função é identificar o estado do tabuleiro.

### 5.1. Integração com os modelos

1. O usuário ou o computador realiza uma jogada.
2. O JavaScript envia o tabuleiro ao servidor Flask.
3. O servidor prepara os atributos utilizados pelo modelo.
4. O classificador realiza a previsão.
5. O servidor devolve a classificação ao frontend.
6. A interface compara a previsão com o estado real do tabuleiro.

Atualmente, a integração está disponível para o KNN.

### 5.2. Informações exibidas

- Estado real do tabuleiro, calculado pelas regras do jogo.
- Previsão do algoritmo selecionado.
- Acertos, erros e acurácia acumulada da IA, separados por algoritmo.
- Placar de vitórias e empates.

A acurácia é calculada por:

`Acurácia = Acertos / (Acertos + Erros) × 100`

A classificação é realizada após cada jogada, inclusive nas do computador. Se o classificador indicar incorretamente que a partida terminou, o erro é contabilizado e o jogo continua. Se houver um resultado final real, a partida é encerrada, mesmo que o classificador não o reconheça.

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
│   │   ├── preparar_a1.py
│   │   ├── treino.csv
│   │   ├── validacao.csv
│   │   └── teste.csv
│   ├── abordagem_2/
│   │   ├── preparar_a2.py
│   │   ├── treino.csv
│   │   ├── validacao.csv
│   │   └── teste.csv
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
├── README.md
└── .gitignore
```

## 7. Como executar o projeto

### 7.1. Requisitos

- Python 3
- Flask, Pandas e Scikit-learn
- Matplotlib e Jupyter (para os notebooks)
- Navegador web

### 7.2. Clonar o repositório

```bash
git clone https://github.com/jesalvatori/tic-tac-toe-game.git
cd tic-tac-toe-game
```

### 7.3. Criar e ativar o ambiente virtual

macOS ou Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 7.4. Instalar as dependências

```bash
python -m pip install flask pandas scikit-learn matplotlib jupyter
```

### 7.5. Gerar os dados das abordagens (opcional)

Os arquivos processados já estão no repositório. Para gerá-los novamente:

```bash
python dataset/abordagem_1/preparar_a1.py
python dataset/abordagem_2/preparar_a2.py
```

### 7.6. Iniciar o servidor Flask

Execute a partir da pasta raiz do projeto (`tic-tac-toe-game/`):

```bash
python app.py
```

Em seguida, abra no navegador: http://127.0.0.1:5000

### 7.7. Jogar

1. Selecione o algoritmo KNN.
2. Clique em uma casa vazia para marcar X.
3. Aguarde a jogada aleatória do computador.
4. Acompanhe as previsões e as métricas da IA.
5. Clique em **Nova partida** para jogar novamente.

## 8. Etapas pendentes

- Finalizar os outros quatro algoritmos.
- Integrar os modelos restantes ao Flask.
- Comparar o desempenho dos cinco classificadores.
- Registrar os resultados dos testes interativos.
- Completar o relatório final do grupo.

## 9. Repositório

https://github.com/jesalvatori/tic-tac-toe-game
