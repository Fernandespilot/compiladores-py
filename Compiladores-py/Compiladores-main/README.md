### Compilador Simples 

Este projeto é um compilador simples desenvolvido como parte do curso de Compiladores. O objetivo é implementar uma linguagem de programação básica que suporte declarações de variáveis, atribuições, estruturas condicionais e de repetição.

## Descrição do Projeto

O compilador é capaz de analisar um código fonte escrito em uma linguagem específica e gerar uma árvore de sintaxe abstrata (AST) a partir do código. Ele também extrai tokens e valida as estruturas do programa conforme as regras definidas na gramática.

### Funcionalidades

- **Declarações de Variáveis**: Suporte a três tipos de variáveis: `int`, `float` e `string`.
- **Atribuições**: Permite a atribuição de valores às variáveis.
- **Estruturas Condicionais**: Implementa a estrutura `if...then...else`.
- **Estruturas de Repetição**: Suporte a loops `while` e `for`.
- **Entrada e Saída**: Comandos para entrada de dados (`input`) e saída de dados (`output`).

## Tecnologias Utilizadas

- [ANTLR](https://www.antlr.org/): Ferramenta para geração de parser e lexer.
- Python: Linguagem de programação utilizada para implementar o compilador.

## Estrutura do Código

A estrutura do código é organizada da seguinte maneira:

- `CompiladorLexer.py`: Implementação do lexer.
- `CompiladorParser.py`: Implementação do parser.
- `main.py`: Arquivo principal que contém a lógica para ler o arquivo de entrada e gerar a árvore de sintaxe.

## Instruções de Uso

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale o ANTLR e as dependências necessárias.
3. Crie um arquivo de entrada com a extensão `.txt` contendo o código a ser compilado.
4. Execute o compilador passando o arquivo como argumento:

   ```bash
   python main.py fonte.txt
begin
    int a, b, result;
    float pi;
    string message;

    // Atribuição de valores
    a = 10;
    b = 20;
    pi = 3.14;

    // Mensagem de saída
    message = "Resultado da soma: ";
    output(message);

    // Estrutura condicional
    if (a > b) then
        output("A é maior que B");
    else
        output("B é maior ou igual a A");
    endif

    // Estrutura de repetição (while)
    result = 0;
    int count = 1;
    while (count <= 5) do
        result = result + count;
        count = count + 1;
    endwhile

    // Saída do resultado
    output("A soma dos primeiros 5 números é: ");
    output(result);

    // Usando um loop for
    output("Contando de 1 a 5:");
    for int i = 1 to 5 do
        output(i);
    endfor
end



Gramatica

grammar Compilador;

// Regras do programa
programa      : BEGIN declaracoes comandos END;
declaracoes   : (declaracao)+;
comandos      : (comando)+;

// Tipos de declaração de variáveis (três tipos: int, float, string)
declaracao
  : (INT | FLOAT | STRING) ID (',' ID)* ';';

// Comandos
comando       : atribuicao 
              | entrada 
              | saida 
              | condicional 
              | repeticao;

// Atribuição
atribuicao    : ID '=' expressao_aritmetica ';';

// Comando de entrada (teclado) e saída (vídeo)
entrada       : INPUT '(' ID ')' ';';
saida         : OUTPUT '(' expressao_aritmetica ')' ';';

// Estrutura condicional (Se... Então... Senão)
condicional   : IF expressao_logica THEN comandos (ELSE comandos)? ENDIF;

// Estruturas de repetição (duas: while e for)
repeticao     : WHILE expressao_logica DO comandos ENDWHILE
              | FOR ID '=' expressao_aritmetica TO expressao_aritmetica DO comandos ENDFOR;

// Expressões aritméticas (com adição, subtração, multiplicação e divisão)
expressao_aritmetica
  : expressao_multiplicativa
  | expressao_aritmetica '+' expressao_multiplicativa
  | expressao_aritmetica '-' expressao_multiplicativa;

expressao_multiplicativa
  : expressao_unaria
  | expressao_multiplicativa '*' expressao_unaria
  | expressao_multiplicativa '/' expressao_unaria;

expressao_unaria
  : '(' expressao_aritmetica ')'
  | NUM
  | ID;

// Expressões lógicas (com seis operadores)
expressao_logica 
              : expressao_aritmetica operador_relacional expressao_aritmetica
              | '(' expressao_logica ')'
              | expressao_logica operador_logico expressao_logica;

// Operadores relacionais e lógicos
operador_relacional 
              : '==' 
              | '!=' 
              | '<' 
              | '>' 
              | '<=' 
              | '>=';

operador_logico 
              : AND 
              | OR
              | NOT;

// Funções definidas pelo usuário
func : ID '(' parametros? ')' '{' comandos '}' ;

parametros : ID (',' ID)*;

// Lista de Tokens
BEGIN         : 'begin';
END           : 'end';
INT           : 'int';
FLOAT         : 'float';
STRING        : 'string';
INPUT         : 'input';
OUTPUT        : 'output';
IF            : 'if';
THEN          : 'then';
ELSE          : 'else';
ENDIF         : 'endif';
WHILE         : 'while';
DO            : 'do';
ENDWHILE      : 'endwhile';
FOR           : 'for';
TO            : 'to';
ENDFOR        : 'endfor';
AND           : 'and';
OR            : 'or';
NOT           : 'not';

// Tokens (ID, NUM e espaços em branco)
ID            : [a-zA-Z_][a-zA-Z_0-9]*;
NUM           : [0-9]+ ('.' [0-9]+)?;
WS            : [ \t\n\r]+ -> skip;




