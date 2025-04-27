# compiladores-py
Ótimo! Vou começar analisando o que você mandou (`Compiladores-py.zip`) para entender o conteúdo e depois montar um `README.md` organizado para o projeto.

Vou extrair o que tem dentro do arquivo primeiro:

O projeto `Compiladores-py` contém:

- Um repositório Git (.git/)
- Um diretório principal chamado `Compiladores-main/` com:
  - Arquivos gerados pelo ANTLR (`CompiladorLexer.py`, `CompiladorParser.py`, etc.)
  - Gramática ANTLR (`Compilador.g4`)
  - Um `main.py` (provavelmente o arquivo principal para rodar o projeto)
  - Um `font.txt`
  - Um arquivo chamado `IAestaticaFutipynb` (aparenta ser um erro de nome — depois te explico isso)
  - Um `README.md` antigo
  - Um diretório `.antlr/` com arquivos `.java` e `.interp`, `.tokens` (gerados também pelo ANTLR)

---

Agora vou te preparar um novo `README.md` mais **organizado** e **profissional** para esse projeto!  
Vou considerar que é um **projeto de compiladores usando Python + ANTLR**.

Aqui está: 

---

# 📚 Projeto de Compilador com ANTLR e Python

Este projeto é um exemplo de construção de um compilador simples utilizando **Python** e a ferramenta **ANTLR 4**.  
A linguagem fonte é definida no arquivo de gramática `Compilador.g4`, e o processamento léxico e sintático é feito a partir do ANTLR.

## 🚀 Como executar

### 1. Pré-requisitos

- Python 3.x instalado
- Java instalado (para usar o ANTLR)
- ANTLR 4.8 (presente no projeto: `antlr-4.8-complete.jar`)

### 2. Instalar ANTLR no Python

```bash
pip install antlr4-python3-runtime
```

### 3. Gerar os arquivos do parser (se necessário)

Caso você modifique o arquivo `Compilador.g4`, será necessário regenerar os arquivos Python:

```bash
# No diretório Compiladores-main
java -jar antlr-4.8-complete.jar -Dlanguage=Python3 Compilador.g4
```

Isso gera arquivos como `CompiladorLexer.py`, `CompiladorParser.py`, etc.

### 4. Executar o compilador

```bash
python main.py
```

O arquivo `main.py` realiza a análise do código de entrada usando os componentes gerados pelo ANTLR.

---

## 🗂️ Estrutura do Projeto

```plaintext
Compiladores-main/
├── .antlr/              # Arquivos auxiliares gerados pelo ANTLR
├── Compilador.g4         # Arquivo de gramática ANTLR
├── CompiladorLexer.py    # Lexer gerado
├── CompiladorParser.py   # Parser gerado
├── CompiladorListener.py # Listener base gerado
├── font.txt              # Arquivo adicional (provavelmente usado para testes)
├── IAestaticaFutipynb    # (Arquivo possivelmente corrompido ou nome errado)
├── main.py               # Código principal que usa o parser/lexer
├── README.md             # Este arquivo
└── antlr-4.8-complete.jar# Ferramenta ANTLR 4.8
```

---

## 🧠 Sobre

Este projeto foi desenvolvido para fins educacionais na disciplina de **Compiladores do curso de Engenharia da Computação**.  
O objetivo é entender a construção de linguagens formais, análise léxica, análise sintática e criação de compiladores.

---

## ⚠️ Observações

- O arquivo `IAestaticaFutipynb` parece estar com o nome errado.Deveria ser `IAestaticaFut.ipynb` (um Jupyter Notebook). Recomenda-se corrigir o nome para facilitar a leitura.
- O repositório contém arquivos `.java` dentro da pasta `.antlr`, que são gerados para a linguagem Java. Para o projeto em Python, esses arquivos não são necessários.

---

## ✍️ Autor

> Projeto desenvolvido por Pedro Fernandes Barbosa Costa.  

