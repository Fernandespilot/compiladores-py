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
