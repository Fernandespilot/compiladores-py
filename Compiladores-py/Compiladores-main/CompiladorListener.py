# Generated from ./Compilador.g4 by ANTLR 4.13.2
from antlr4 import * # type: ignore
if "." in __name__:
    from .CompiladorParser import CompiladorParser
else:
    from Compilador.Compilador.CompiladorParser import CompiladorParser

# This class defines a complete listener for a parse tree produced by CompiladorParser.
class CompiladorListener(ParseTreeListener):

    # Enter a parse tree produced by CompiladorParser#programa.
    def enterPrograma(self, ctx:CompiladorParser.ProgramaContext):
        pass

    # Exit a parse tree produced by CompiladorParser#programa.
    def exitPrograma(self, ctx:CompiladorParser.ProgramaContext):
        pass


    # Enter a parse tree produced by CompiladorParser#declaracoes.
    def enterDeclaracoes(self, ctx:CompiladorParser.DeclaracoesContext):
        pass

    # Exit a parse tree produced by CompiladorParser#declaracoes.
    def exitDeclaracoes(self, ctx:CompiladorParser.DeclaracoesContext):
        pass


    # Enter a parse tree produced by CompiladorParser#comandos.
    def enterComandos(self, ctx:CompiladorParser.ComandosContext):
        pass

    # Exit a parse tree produced by CompiladorParser#comandos.
    def exitComandos(self, ctx:CompiladorParser.ComandosContext):
        pass


    # Enter a parse tree produced by CompiladorParser#declaracao.
    def enterDeclaracao(self, ctx:CompiladorParser.DeclaracaoContext):
        pass

    # Exit a parse tree produced by CompiladorParser#declaracao.
    def exitDeclaracao(self, ctx:CompiladorParser.DeclaracaoContext):
        pass


    # Enter a parse tree produced by CompiladorParser#comando.
    def enterComando(self, ctx:CompiladorParser.ComandoContext):
        pass

    # Exit a parse tree produced by CompiladorParser#comando.
    def exitComando(self, ctx:CompiladorParser.ComandoContext):
        pass


    # Enter a parse tree produced by CompiladorParser#atribuicao.
    def enterAtribuicao(self, ctx:CompiladorParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by CompiladorParser#atribuicao.
    def exitAtribuicao(self, ctx:CompiladorParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by CompiladorParser#entrada.
    def enterEntrada(self, ctx:CompiladorParser.EntradaContext):
        pass

    # Exit a parse tree produced by CompiladorParser#entrada.
    def exitEntrada(self, ctx:CompiladorParser.EntradaContext):
        pass


    # Enter a parse tree produced by CompiladorParser#saida.
    def enterSaida(self, ctx:CompiladorParser.SaidaContext):
        pass

    # Exit a parse tree produced by CompiladorParser#saida.
    def exitSaida(self, ctx:CompiladorParser.SaidaContext):
        pass


    # Enter a parse tree produced by CompiladorParser#condicional.
    def enterCondicional(self, ctx:CompiladorParser.CondicionalContext):
        pass

    # Exit a parse tree produced by CompiladorParser#condicional.
    def exitCondicional(self, ctx:CompiladorParser.CondicionalContext):
        pass


    # Enter a parse tree produced by CompiladorParser#repeticao.
    def enterRepeticao(self, ctx:CompiladorParser.RepeticaoContext):
        pass

    # Exit a parse tree produced by CompiladorParser#repeticao.
    def exitRepeticao(self, ctx:CompiladorParser.RepeticaoContext):
        pass


    # Enter a parse tree produced by CompiladorParser#expressao_aritmetica.
    def enterExpressao_aritmetica(self, ctx:CompiladorParser.Expressao_aritmeticaContext):
        pass

    # Exit a parse tree produced by CompiladorParser#expressao_aritmetica.
    def exitExpressao_aritmetica(self, ctx:CompiladorParser.Expressao_aritmeticaContext):
        pass


    # Enter a parse tree produced by CompiladorParser#expressao_multiplicativa.
    def enterExpressao_multiplicativa(self, ctx:CompiladorParser.Expressao_multiplicativaContext):
        pass

    # Exit a parse tree produced by CompiladorParser#expressao_multiplicativa.
    def exitExpressao_multiplicativa(self, ctx:CompiladorParser.Expressao_multiplicativaContext):
        pass


    # Enter a parse tree produced by CompiladorParser#expressao_unaria.
    def enterExpressao_unaria(self, ctx:CompiladorParser.Expressao_unariaContext):
        pass

    # Exit a parse tree produced by CompiladorParser#expressao_unaria.
    def exitExpressao_unaria(self, ctx:CompiladorParser.Expressao_unariaContext):
        pass


    # Enter a parse tree produced by CompiladorParser#expressao_logica.
    def enterExpressao_logica(self, ctx:CompiladorParser.Expressao_logicaContext):
        pass

    # Exit a parse tree produced by CompiladorParser#expressao_logica.
    def exitExpressao_logica(self, ctx:CompiladorParser.Expressao_logicaContext):
        pass


    # Enter a parse tree produced by CompiladorParser#operador_relacional.
    def enterOperador_relacional(self, ctx:CompiladorParser.Operador_relacionalContext):
        pass

    # Exit a parse tree produced by CompiladorParser#operador_relacional.
    def exitOperador_relacional(self, ctx:CompiladorParser.Operador_relacionalContext):
        pass


    # Enter a parse tree produced by CompiladorParser#operador_logico.
    def enterOperador_logico(self, ctx:CompiladorParser.Operador_logicoContext):
        pass

    # Exit a parse tree produced by CompiladorParser#operador_logico.
    def exitOperador_logico(self, ctx:CompiladorParser.Operador_logicoContext):
        pass


    # Enter a parse tree produced by CompiladorParser#func.
    def enterFunc(self, ctx:CompiladorParser.FuncContext):
        pass

    # Exit a parse tree produced by CompiladorParser#func.
    def exitFunc(self, ctx:CompiladorParser.FuncContext):
        pass


    # Enter a parse tree produced by CompiladorParser#parametros.
    def enterParametros(self, ctx:CompiladorParser.ParametrosContext):
        pass

    # Exit a parse tree produced by CompiladorParser#parametros.
    def exitParametros(self, ctx:CompiladorParser.ParametrosContext):
        pass



del CompiladorParser