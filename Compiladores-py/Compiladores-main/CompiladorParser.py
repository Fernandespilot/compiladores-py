# Generated from ./Compilador.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,40,193,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,1,0,1,0,1,1,
        4,1,43,8,1,11,1,12,1,44,1,2,4,2,48,8,2,11,2,12,2,49,1,3,1,3,1,3,
        1,3,5,3,56,8,3,10,3,12,3,59,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,4,
        68,8,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,
        7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,93,8,8,1,8,1,8,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,113,8,9,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,124,8,10,10,10,
        12,10,127,9,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,
        138,8,11,10,11,12,11,141,9,11,1,12,1,12,1,12,1,12,1,12,1,12,3,12,
        149,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,160,8,
        13,1,13,1,13,1,13,1,13,5,13,166,8,13,10,13,12,13,169,9,13,1,14,1,
        14,1,15,1,15,1,16,1,16,1,16,3,16,178,8,16,1,16,1,16,1,16,1,16,1,
        16,1,17,1,17,1,17,5,17,188,8,17,10,17,12,17,191,9,17,1,17,0,3,20,
        22,26,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,3,1,
        0,20,22,1,0,10,15,1,0,35,37,193,0,36,1,0,0,0,2,42,1,0,0,0,4,47,1,
        0,0,0,6,51,1,0,0,0,8,67,1,0,0,0,10,69,1,0,0,0,12,74,1,0,0,0,14,80,
        1,0,0,0,16,86,1,0,0,0,18,112,1,0,0,0,20,114,1,0,0,0,22,128,1,0,0,
        0,24,148,1,0,0,0,26,159,1,0,0,0,28,170,1,0,0,0,30,172,1,0,0,0,32,
        174,1,0,0,0,34,184,1,0,0,0,36,37,5,18,0,0,37,38,3,2,1,0,38,39,3,
        4,2,0,39,40,5,19,0,0,40,1,1,0,0,0,41,43,3,6,3,0,42,41,1,0,0,0,43,
        44,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,3,1,0,0,0,46,48,3,8,4,
        0,47,46,1,0,0,0,48,49,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,5,1,
        0,0,0,51,52,7,0,0,0,52,57,5,38,0,0,53,54,5,1,0,0,54,56,5,38,0,0,
        55,53,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,60,1,
        0,0,0,59,57,1,0,0,0,60,61,5,2,0,0,61,7,1,0,0,0,62,68,3,10,5,0,63,
        68,3,12,6,0,64,68,3,14,7,0,65,68,3,16,8,0,66,68,3,18,9,0,67,62,1,
        0,0,0,67,63,1,0,0,0,67,64,1,0,0,0,67,65,1,0,0,0,67,66,1,0,0,0,68,
        9,1,0,0,0,69,70,5,38,0,0,70,71,5,3,0,0,71,72,3,20,10,0,72,73,5,2,
        0,0,73,11,1,0,0,0,74,75,5,23,0,0,75,76,5,4,0,0,76,77,5,38,0,0,77,
        78,5,5,0,0,78,79,5,2,0,0,79,13,1,0,0,0,80,81,5,24,0,0,81,82,5,4,
        0,0,82,83,3,20,10,0,83,84,5,5,0,0,84,85,5,2,0,0,85,15,1,0,0,0,86,
        87,5,25,0,0,87,88,3,26,13,0,88,89,5,26,0,0,89,92,3,4,2,0,90,91,5,
        27,0,0,91,93,3,4,2,0,92,90,1,0,0,0,92,93,1,0,0,0,93,94,1,0,0,0,94,
        95,5,28,0,0,95,17,1,0,0,0,96,97,5,29,0,0,97,98,3,26,13,0,98,99,5,
        30,0,0,99,100,3,4,2,0,100,101,5,31,0,0,101,113,1,0,0,0,102,103,5,
        32,0,0,103,104,5,38,0,0,104,105,5,3,0,0,105,106,3,20,10,0,106,107,
        5,33,0,0,107,108,3,20,10,0,108,109,5,30,0,0,109,110,3,4,2,0,110,
        111,5,34,0,0,111,113,1,0,0,0,112,96,1,0,0,0,112,102,1,0,0,0,113,
        19,1,0,0,0,114,115,6,10,-1,0,115,116,3,22,11,0,116,125,1,0,0,0,117,
        118,10,2,0,0,118,119,5,6,0,0,119,124,3,22,11,0,120,121,10,1,0,0,
        121,122,5,7,0,0,122,124,3,22,11,0,123,117,1,0,0,0,123,120,1,0,0,
        0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,21,1,0,0,0,
        127,125,1,0,0,0,128,129,6,11,-1,0,129,130,3,24,12,0,130,139,1,0,
        0,0,131,132,10,2,0,0,132,133,5,8,0,0,133,138,3,24,12,0,134,135,10,
        1,0,0,135,136,5,9,0,0,136,138,3,24,12,0,137,131,1,0,0,0,137,134,
        1,0,0,0,138,141,1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,23,1,
        0,0,0,141,139,1,0,0,0,142,143,5,4,0,0,143,144,3,20,10,0,144,145,
        5,5,0,0,145,149,1,0,0,0,146,149,5,39,0,0,147,149,5,38,0,0,148,142,
        1,0,0,0,148,146,1,0,0,0,148,147,1,0,0,0,149,25,1,0,0,0,150,151,6,
        13,-1,0,151,152,3,20,10,0,152,153,3,28,14,0,153,154,3,20,10,0,154,
        160,1,0,0,0,155,156,5,4,0,0,156,157,3,26,13,0,157,158,5,5,0,0,158,
        160,1,0,0,0,159,150,1,0,0,0,159,155,1,0,0,0,160,167,1,0,0,0,161,
        162,10,1,0,0,162,163,3,30,15,0,163,164,3,26,13,2,164,166,1,0,0,0,
        165,161,1,0,0,0,166,169,1,0,0,0,167,165,1,0,0,0,167,168,1,0,0,0,
        168,27,1,0,0,0,169,167,1,0,0,0,170,171,7,1,0,0,171,29,1,0,0,0,172,
        173,7,2,0,0,173,31,1,0,0,0,174,175,5,38,0,0,175,177,5,4,0,0,176,
        178,3,34,17,0,177,176,1,0,0,0,177,178,1,0,0,0,178,179,1,0,0,0,179,
        180,5,5,0,0,180,181,5,16,0,0,181,182,3,4,2,0,182,183,5,17,0,0,183,
        33,1,0,0,0,184,189,5,38,0,0,185,186,5,1,0,0,186,188,5,38,0,0,187,
        185,1,0,0,0,188,191,1,0,0,0,189,187,1,0,0,0,189,190,1,0,0,0,190,
        35,1,0,0,0,191,189,1,0,0,0,15,44,49,57,67,92,112,123,125,137,139,
        148,159,167,177,189
    ]

class CompiladorParser ( Parser ):

    grammarFileName = "Compilador.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "';'", "'='", "'('", "')'", "'+'", 
                     "'-'", "'*'", "'/'", "'=='", "'!='", "'<'", "'>'", 
                     "'<='", "'>='", "'{'", "'}'", "'begin'", "'end'", "'int'", 
                     "'float'", "'string'", "'input'", "'output'", "'if'", 
                     "'then'", "'else'", "'endif'", "'while'", "'do'", "'endwhile'", 
                     "'for'", "'to'", "'endfor'", "'and'", "'or'", "'not'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "BEGIN", "END", "INT", "FLOAT", 
                      "STRING", "INPUT", "OUTPUT", "IF", "THEN", "ELSE", 
                      "ENDIF", "WHILE", "DO", "ENDWHILE", "FOR", "TO", "ENDFOR", 
                      "AND", "OR", "NOT", "ID", "NUM", "WS" ]

    RULE_programa = 0
    RULE_declaracoes = 1
    RULE_comandos = 2
    RULE_declaracao = 3
    RULE_comando = 4
    RULE_atribuicao = 5
    RULE_entrada = 6
    RULE_saida = 7
    RULE_condicional = 8
    RULE_repeticao = 9
    RULE_expressao_aritmetica = 10
    RULE_expressao_multiplicativa = 11
    RULE_expressao_unaria = 12
    RULE_expressao_logica = 13
    RULE_operador_relacional = 14
    RULE_operador_logico = 15
    RULE_func = 16
    RULE_parametros = 17

    ruleNames =  [ "programa", "declaracoes", "comandos", "declaracao", 
                   "comando", "atribuicao", "entrada", "saida", "condicional", 
                   "repeticao", "expressao_aritmetica", "expressao_multiplicativa", 
                   "expressao_unaria", "expressao_logica", "operador_relacional", 
                   "operador_logico", "func", "parametros" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    BEGIN=18
    END=19
    INT=20
    FLOAT=21
    STRING=22
    INPUT=23
    OUTPUT=24
    IF=25
    THEN=26
    ELSE=27
    ENDIF=28
    WHILE=29
    DO=30
    ENDWHILE=31
    FOR=32
    TO=33
    ENDFOR=34
    AND=35
    OR=36
    NOT=37
    ID=38
    NUM=39
    WS=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(CompiladorParser.BEGIN, 0)

        def declaracoes(self):
            return self.getTypedRuleContext(CompiladorParser.DeclaracoesContext,0)


        def comandos(self):
            return self.getTypedRuleContext(CompiladorParser.ComandosContext,0)


        def END(self):
            return self.getToken(CompiladorParser.END, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = CompiladorParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(CompiladorParser.BEGIN)
            self.state = 37
            self.declaracoes()
            self.state = 38
            self.comandos()
            self.state = 39
            self.match(CompiladorParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.DeclaracaoContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.DeclaracaoContext,i)


        def getRuleIndex(self):
            return CompiladorParser.RULE_declaracoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracoes" ):
                listener.enterDeclaracoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracoes" ):
                listener.exitDeclaracoes(self)




    def declaracoes(self):

        localctx = CompiladorParser.DeclaracoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracoes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 41
                self.declaracao()
                self.state = 44 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.ComandoContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.ComandoContext,i)


        def getRuleIndex(self):
            return CompiladorParser.RULE_comandos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandos" ):
                listener.enterComandos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandos" ):
                listener.exitComandos(self)




    def comandos(self):

        localctx = CompiladorParser.ComandosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_comandos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.comando()
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 279768465408) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CompiladorParser.ID)
            else:
                return self.getToken(CompiladorParser.ID, i)

        def INT(self):
            return self.getToken(CompiladorParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CompiladorParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(CompiladorParser.STRING, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_declaracao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao" ):
                listener.enterDeclaracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao" ):
                listener.exitDeclaracao(self)




    def declaracao(self):

        localctx = CompiladorParser.DeclaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 52
            self.match(CompiladorParser.ID)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 53
                self.match(CompiladorParser.T__0)
                self.state = 54
                self.match(CompiladorParser.ID)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
            self.match(CompiladorParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atribuicao(self):
            return self.getTypedRuleContext(CompiladorParser.AtribuicaoContext,0)


        def entrada(self):
            return self.getTypedRuleContext(CompiladorParser.EntradaContext,0)


        def saida(self):
            return self.getTypedRuleContext(CompiladorParser.SaidaContext,0)


        def condicional(self):
            return self.getTypedRuleContext(CompiladorParser.CondicionalContext,0)


        def repeticao(self):
            return self.getTypedRuleContext(CompiladorParser.RepeticaoContext,0)


        def getRuleIndex(self):
            return CompiladorParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)




    def comando(self):

        localctx = CompiladorParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_comando)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.atribuicao()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.entrada()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.saida()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.condicional()
                pass
            elif token in [29, 32]:
                self.enterOuterAlt(localctx, 5)
                self.state = 66
                self.repeticao()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CompiladorParser.ID, 0)

        def expressao_aritmetica(self):
            return self.getTypedRuleContext(CompiladorParser.Expressao_aritmeticaContext,0)


        def getRuleIndex(self):
            return CompiladorParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)




    def atribuicao(self):

        localctx = CompiladorParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(CompiladorParser.ID)
            self.state = 70
            self.match(CompiladorParser.T__2)
            self.state = 71
            self.expressao_aritmetica(0)
            self.state = 72
            self.match(CompiladorParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntradaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(CompiladorParser.INPUT, 0)

        def ID(self):
            return self.getToken(CompiladorParser.ID, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_entrada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntrada" ):
                listener.enterEntrada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntrada" ):
                listener.exitEntrada(self)




    def entrada(self):

        localctx = CompiladorParser.EntradaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_entrada)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(CompiladorParser.INPUT)
            self.state = 75
            self.match(CompiladorParser.T__3)
            self.state = 76
            self.match(CompiladorParser.ID)
            self.state = 77
            self.match(CompiladorParser.T__4)
            self.state = 78
            self.match(CompiladorParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SaidaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OUTPUT(self):
            return self.getToken(CompiladorParser.OUTPUT, 0)

        def expressao_aritmetica(self):
            return self.getTypedRuleContext(CompiladorParser.Expressao_aritmeticaContext,0)


        def getRuleIndex(self):
            return CompiladorParser.RULE_saida

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSaida" ):
                listener.enterSaida(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSaida" ):
                listener.exitSaida(self)




    def saida(self):

        localctx = CompiladorParser.SaidaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_saida)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(CompiladorParser.OUTPUT)
            self.state = 81
            self.match(CompiladorParser.T__3)
            self.state = 82
            self.expressao_aritmetica(0)
            self.state = 83
            self.match(CompiladorParser.T__4)
            self.state = 84
            self.match(CompiladorParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CompiladorParser.IF, 0)

        def expressao_logica(self):
            return self.getTypedRuleContext(CompiladorParser.Expressao_logicaContext,0)


        def THEN(self):
            return self.getToken(CompiladorParser.THEN, 0)

        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.ComandosContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.ComandosContext,i)


        def ENDIF(self):
            return self.getToken(CompiladorParser.ENDIF, 0)

        def ELSE(self):
            return self.getToken(CompiladorParser.ELSE, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)




    def condicional(self):

        localctx = CompiladorParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(CompiladorParser.IF)
            self.state = 87
            self.expressao_logica(0)
            self.state = 88
            self.match(CompiladorParser.THEN)
            self.state = 89
            self.comandos()
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 90
                self.match(CompiladorParser.ELSE)
                self.state = 91
                self.comandos()


            self.state = 94
            self.match(CompiladorParser.ENDIF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeticaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(CompiladorParser.WHILE, 0)

        def expressao_logica(self):
            return self.getTypedRuleContext(CompiladorParser.Expressao_logicaContext,0)


        def DO(self):
            return self.getToken(CompiladorParser.DO, 0)

        def comandos(self):
            return self.getTypedRuleContext(CompiladorParser.ComandosContext,0)


        def ENDWHILE(self):
            return self.getToken(CompiladorParser.ENDWHILE, 0)

        def FOR(self):
            return self.getToken(CompiladorParser.FOR, 0)

        def ID(self):
            return self.getToken(CompiladorParser.ID, 0)

        def expressao_aritmetica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.Expressao_aritmeticaContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.Expressao_aritmeticaContext,i)


        def TO(self):
            return self.getToken(CompiladorParser.TO, 0)

        def ENDFOR(self):
            return self.getToken(CompiladorParser.ENDFOR, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_repeticao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeticao" ):
                listener.enterRepeticao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeticao" ):
                listener.exitRepeticao(self)




    def repeticao(self):

        localctx = CompiladorParser.RepeticaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_repeticao)
        try:
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.match(CompiladorParser.WHILE)
                self.state = 97
                self.expressao_logica(0)
                self.state = 98
                self.match(CompiladorParser.DO)
                self.state = 99
                self.comandos()
                self.state = 100
                self.match(CompiladorParser.ENDWHILE)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.match(CompiladorParser.FOR)
                self.state = 103
                self.match(CompiladorParser.ID)
                self.state = 104
                self.match(CompiladorParser.T__2)
                self.state = 105
                self.expressao_aritmetica(0)
                self.state = 106
                self.match(CompiladorParser.TO)
                self.state = 107
                self.expressao_aritmetica(0)
                self.state = 108
                self.match(CompiladorParser.DO)
                self.state = 109
                self.comandos()
                self.state = 110
                self.match(CompiladorParser.ENDFOR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expressao_aritmeticaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao_multiplicativa(self):
            return self.getTypedRuleContext(CompiladorParser.Expressao_multiplicativaContext,0)


        def expressao_aritmetica(self):
            return self.getTypedRuleContext(CompiladorParser.Expressao_aritmeticaContext,0)


        def getRuleIndex(self):
            return CompiladorParser.RULE_expressao_aritmetica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao_aritmetica" ):
                listener.enterExpressao_aritmetica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao_aritmetica" ):
                listener.exitExpressao_aritmetica(self)



    def expressao_aritmetica(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CompiladorParser.Expressao_aritmeticaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expressao_aritmetica, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.expressao_multiplicativa(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 125
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 123
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = CompiladorParser.Expressao_aritmeticaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao_aritmetica)
                        self.state = 117
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 118
                        self.match(CompiladorParser.T__5)
                        self.state = 119
                        self.expressao_multiplicativa(0)
                        pass

                    elif la_ == 2:
                        localctx = CompiladorParser.Expressao_aritmeticaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao_aritmetica)
                        self.state = 120
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 121
                        self.match(CompiladorParser.T__6)
                        self.state = 122
                        self.expressao_multiplicativa(0)
                        pass

             
                self.state = 127
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expressao_multiplicativaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao_unaria(self):
            return self.getTypedRuleContext(CompiladorParser.Expressao_unariaContext,0)


        def expressao_multiplicativa(self):
            return self.getTypedRuleContext(CompiladorParser.Expressao_multiplicativaContext,0)


        def getRuleIndex(self):
            return CompiladorParser.RULE_expressao_multiplicativa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao_multiplicativa" ):
                listener.enterExpressao_multiplicativa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao_multiplicativa" ):
                listener.exitExpressao_multiplicativa(self)



    def expressao_multiplicativa(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CompiladorParser.Expressao_multiplicativaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expressao_multiplicativa, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.expressao_unaria()
            self._ctx.stop = self._input.LT(-1)
            self.state = 139
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 137
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = CompiladorParser.Expressao_multiplicativaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao_multiplicativa)
                        self.state = 131
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 132
                        self.match(CompiladorParser.T__7)
                        self.state = 133
                        self.expressao_unaria()
                        pass

                    elif la_ == 2:
                        localctx = CompiladorParser.Expressao_multiplicativaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao_multiplicativa)
                        self.state = 134
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 135
                        self.match(CompiladorParser.T__8)
                        self.state = 136
                        self.expressao_unaria()
                        pass

             
                self.state = 141
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expressao_unariaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao_aritmetica(self):
            return self.getTypedRuleContext(CompiladorParser.Expressao_aritmeticaContext,0)


        def NUM(self):
            return self.getToken(CompiladorParser.NUM, 0)

        def ID(self):
            return self.getToken(CompiladorParser.ID, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_expressao_unaria

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao_unaria" ):
                listener.enterExpressao_unaria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao_unaria" ):
                listener.exitExpressao_unaria(self)




    def expressao_unaria(self):

        localctx = CompiladorParser.Expressao_unariaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expressao_unaria)
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.match(CompiladorParser.T__3)
                self.state = 143
                self.expressao_aritmetica(0)
                self.state = 144
                self.match(CompiladorParser.T__4)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.match(CompiladorParser.NUM)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.match(CompiladorParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expressao_logicaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao_aritmetica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.Expressao_aritmeticaContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.Expressao_aritmeticaContext,i)


        def operador_relacional(self):
            return self.getTypedRuleContext(CompiladorParser.Operador_relacionalContext,0)


        def expressao_logica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.Expressao_logicaContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.Expressao_logicaContext,i)


        def operador_logico(self):
            return self.getTypedRuleContext(CompiladorParser.Operador_logicoContext,0)


        def getRuleIndex(self):
            return CompiladorParser.RULE_expressao_logica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao_logica" ):
                listener.enterExpressao_logica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao_logica" ):
                listener.exitExpressao_logica(self)



    def expressao_logica(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CompiladorParser.Expressao_logicaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expressao_logica, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 151
                self.expressao_aritmetica(0)
                self.state = 152
                self.operador_relacional()
                self.state = 153
                self.expressao_aritmetica(0)
                pass

            elif la_ == 2:
                self.state = 155
                self.match(CompiladorParser.T__3)
                self.state = 156
                self.expressao_logica(0)
                self.state = 157
                self.match(CompiladorParser.T__4)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 167
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CompiladorParser.Expressao_logicaContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao_logica)
                    self.state = 161
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 162
                    self.operador_logico()
                    self.state = 163
                    self.expressao_logica(2) 
                self.state = 169
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Operador_relacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CompiladorParser.RULE_operador_relacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperador_relacional" ):
                listener.enterOperador_relacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperador_relacional" ):
                listener.exitOperador_relacional(self)




    def operador_relacional(self):

        localctx = CompiladorParser.Operador_relacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_operador_relacional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 64512) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operador_logicoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(CompiladorParser.AND, 0)

        def OR(self):
            return self.getToken(CompiladorParser.OR, 0)

        def NOT(self):
            return self.getToken(CompiladorParser.NOT, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_operador_logico

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperador_logico" ):
                listener.enterOperador_logico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperador_logico" ):
                listener.exitOperador_logico(self)




    def operador_logico(self):

        localctx = CompiladorParser.Operador_logicoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_operador_logico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 240518168576) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CompiladorParser.ID, 0)

        def comandos(self):
            return self.getTypedRuleContext(CompiladorParser.ComandosContext,0)


        def parametros(self):
            return self.getTypedRuleContext(CompiladorParser.ParametrosContext,0)


        def getRuleIndex(self):
            return CompiladorParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)




    def func(self):

        localctx = CompiladorParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(CompiladorParser.ID)
            self.state = 175
            self.match(CompiladorParser.T__3)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 176
                self.parametros()


            self.state = 179
            self.match(CompiladorParser.T__4)
            self.state = 180
            self.match(CompiladorParser.T__15)
            self.state = 181
            self.comandos()
            self.state = 182
            self.match(CompiladorParser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CompiladorParser.ID)
            else:
                return self.getToken(CompiladorParser.ID, i)

        def getRuleIndex(self):
            return CompiladorParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)




    def parametros(self):

        localctx = CompiladorParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(CompiladorParser.ID)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 185
                self.match(CompiladorParser.T__0)
                self.state = 186
                self.match(CompiladorParser.ID)
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.expressao_aritmetica_sempred
        self._predicates[11] = self.expressao_multiplicativa_sempred
        self._predicates[13] = self.expressao_logica_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expressao_aritmetica_sempred(self, localctx:Expressao_aritmeticaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def expressao_multiplicativa_sempred(self, localctx:Expressao_multiplicativaContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def expressao_logica_sempred(self, localctx:Expressao_logicaContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         




