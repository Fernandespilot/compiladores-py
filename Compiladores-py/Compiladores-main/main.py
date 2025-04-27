import sys
from antlr4 import FileStream, CommonTokenStream # type: ignore
from Compilador.Compilador.CompiladorLexer import CompiladorLexer
from Compilador.Compilador.CompiladorParser import CompiladorParser

def main():
    # Verifica se o arquivo de entrada foi passado como argumento
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        print("Erro: Nenhum arquivo de entrada fornecido.")
        return

    # Lê o conteúdo do arquivo de entrada
    try:
        input_stream = FileStream(input_file, encoding='utf-8')
    except IOError:
        print(f"Erro ao abrir o arquivo {input_file}")
        return

    # Cria o lexer para o arquivo de entrada
    lexer = CompiladorLexer(input_stream)

    # Tokeniza a entrada
    token_stream = CommonTokenStream(lexer)

    # Preenche os tokens
    token_stream.fill()

    # Imprime os tokens
    print("Tokens extraídos:")
    for token in token_stream.tokens:
        if token.type in lexer.symbolicNames:
            token_nome = lexer.symbolicNames[token.type]
            print(f"Token: {token_nome:<15} Texto: {token.text}")
        else:
            print(f"Token conhecido: {token.type} Texto: {token.text}")

    # Cria o parser a partir do stream de tokens
    parser = CompiladorParser(token_stream)

    # Faz o parsing começando pela regra 'programa'
    tree = parser.programa()

    # Exibe a árvore de parsing (opcional)
    print("\nÁrvore de parsing:")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()
