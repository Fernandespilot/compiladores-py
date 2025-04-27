# 📚 Compilador Simples

Este projeto é um **compilador simples**, desenvolvido como parte do curso de **Compiladores**.  
O objetivo é criar uma linguagem de programação básica que suporte:

- Declarações de variáveis
- Atribuições
- Estruturas condicionais (`if-then-else`)
- Estruturas de repetição (`while`, `for`)
- Comandos de entrada e saída (`input`, `output`)

## 🛠️ Descrição do Projeto

O compilador realiza:

- Análise léxica e sintática de um código fonte escrito na linguagem definida
- Geração da **árvore de sintaxe abstrata (AST)**
- Extração de **tokens**
- Validação das estruturas conforme a gramática

## ✨ Funcionalidades

- **Declarações de Variáveis**: Suporte a três tipos: `int`, `float`, `string`
- **Atribuições**: Atribuição de valores a variáveis
- **Condicionais**: `if...then...else`
- **Repetições**: `while` e `for`
- **Entrada e Saída**: `input()` e `output()`

## 🧰 Tecnologias Utilizadas

- [ANTLR 4](https://www.antlr.org/): Ferramenta para gerar o lexer e o parser
- **Python 3.x**: Linguagem utilizada para implementar o compilador

## 🗂️ Estrutura do Código

```plaintext
Compiladores-main/
├── CompiladorLexer.py    # Lexer (gerado pelo ANTLR)
├── CompiladorParser.py   # Parser (gerado pelo ANTLR)
├── CompiladorListener.py # Listener (opcional)
├── main.py               # Arquivo principal de execução
├── Compilador.g4         # Arquivo de gramática
└── Outros arquivos de suporte (tokens, interp, jar do ANTLR)
```

## 🚀 Como Usar

1. **Certifique-se de ter Python e Java instalados.**

2. **Instale a dependência do ANTLR para Python:**

```bash
pip install antlr4-python3-runtime
```

3. **Crie um arquivo fonte** (`fonte.txt`) com o código a ser compilado.

4. **Execute o compilador:**

```bash
python main.py fonte.txt
```

---

## 📄 Exemplo de Código de Entrada

```c
begin
    int a, b, result;
    float pi;
    string message;

    a = 10;
    b = 20;
    pi = 3.14;

    message = "Resultado da soma: ";
    output(message);

    if (a > b) then
        output("A é maior que B");
    else
        output("B é maior ou igual a A");
    endif

    result = 0;
    int count = 1;
    while (count <= 5) do
        result = result + count;
        count = count + 1;
    endwhile

    output("A soma dos primeiros 5 números é: ");
    output(result);

    output("Contando de 1 a 5:");
    for int i = 1 to 5 do
        output(i);
    endfor
end
```

---

## 🧠 Gramática da Linguagem

### Regras Principais

- Programa:
  ```antlr
  programa : BEGIN declaracoes comandos END;
  declaracoes : (declaracao)+;
  comandos : (comando)+;
  ```

- Declarações:
  ```antlr
  declaracao : (INT | FLOAT | STRING) ID (',' ID)* ';';
  ```

- Comandos:
  ```antlr
  comando : atribuicao
          | entrada
          | saida
          | condicional
          | repeticao;
  ```

- Expressões aritméticas e lógicas:
  ```antlr
  expressao_aritmetica : expressao_multiplicativa
                       | expressao_aritmetica '+' expressao_multiplicativa
                       | expressao_aritmetica '-' expressao_multiplicativa;

  expressao_logica : expressao_aritmetica operador_relacional expressao_aritmetica
                   | '(' expressao_logica ')'
                   | expressao_logica operador_logico expressao_logica;
  ```

- Estruturas de repetição:
  ```antlr
  repeticao : WHILE expressao_logica DO comandos ENDWHILE
            | FOR ID '=' expressao_aritmetica TO expressao_aritmetica DO comandos ENDFOR;
  ```

### Tokens Definidos

- Palavras reservadas:
  ```antlr
  BEGIN, END, INT, FLOAT, STRING, INPUT, OUTPUT, IF, THEN, ELSE, ENDIF,
  WHILE, DO, ENDWHILE, FOR, TO, ENDFOR, AND, OR, NOT
  ```

- Outros:
  ```antlr
  ID  : [a-zA-Z_][a-zA-Z_0-9]*;
  NUM : [0-9]+ ('.' [0-9]+)?;
  WS  : [ \t\n\r]+ -> skip;
  ```

---

# 🧑‍💻 Autor

Projeto desenvolvido por Pedro Fernandes Barbosa Costa como atividade prática da disciplina de Compiladores do curso de Engenharia da Computação no IFMT.
@eng.fernandespb instagram
Sinta-se à vontade para usar como base para seus estudos!

