# Generated from tale/syntax/grammar/Tale.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from antlr_denter.DenterHelper import DenterHelper
from .TaleParser import TaleParser



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("\\\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\6\7")
        buf.write(")\n\7\r\7\16\7*\3\b\6\b.\n\b\r\b\16\b/\3\t\3\t\3\n\3\n")
        buf.write("\7\n\66\n\n\f\n\16\n9\13\n\3\n\3\n\3\13\6\13>\n\13\r\13")
        buf.write("\16\13?\3\13\3\13\3\f\5\fE\n\f\3\f\3\f\7\fI\n\f\f\f\16")
        buf.write("\fL\13\f\3\r\3\r\3\r\3\r\7\rR\n\r\f\r\16\rU\13\r\3\16")
        buf.write("\3\16\5\16Y\n\16\3\16\3\16\3\67\2\17\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\2\33\16\3\2\7\4\2")
        buf.write("C\\c|\3\2\62;\5\2,-//\61\61\4\2\13\13\"\"\4\2\f\f\16\17")
        buf.write("\2b\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\33\3\2\2\2\3\35\3")
        buf.write("\2\2\2\5\37\3\2\2\2\7!\3\2\2\2\t#\3\2\2\2\13%\3\2\2\2")
        buf.write("\r(\3\2\2\2\17-\3\2\2\2\21\61\3\2\2\2\23\63\3\2\2\2\25")
        buf.write("=\3\2\2\2\27D\3\2\2\2\31M\3\2\2\2\33X\3\2\2\2\35\36\7")
        buf.write("?\2\2\36\4\3\2\2\2\37 \7<\2\2 \6\3\2\2\2!\"\7.\2\2\"\b")
        buf.write("\3\2\2\2#$\7*\2\2$\n\3\2\2\2%&\7+\2\2&\f\3\2\2\2\')\t")
        buf.write("\2\2\2(\'\3\2\2\2)*\3\2\2\2*(\3\2\2\2*+\3\2\2\2+\16\3")
        buf.write("\2\2\2,.\t\3\2\2-,\3\2\2\2./\3\2\2\2/-\3\2\2\2/\60\3\2")
        buf.write("\2\2\60\20\3\2\2\2\61\62\t\4\2\2\62\22\3\2\2\2\63\67\7")
        buf.write("$\2\2\64\66\13\2\2\2\65\64\3\2\2\2\669\3\2\2\2\678\3\2")
        buf.write("\2\2\67\65\3\2\2\28:\3\2\2\29\67\3\2\2\2:;\7$\2\2;\24")
        buf.write("\3\2\2\2<>\t\5\2\2=<\3\2\2\2>?\3\2\2\2?=\3\2\2\2?@\3\2")
        buf.write("\2\2@A\3\2\2\2AB\b\13\2\2B\26\3\2\2\2CE\7\17\2\2DC\3\2")
        buf.write("\2\2DE\3\2\2\2EF\3\2\2\2FJ\7\f\2\2GI\7\"\2\2HG\3\2\2\2")
        buf.write("IL\3\2\2\2JH\3\2\2\2JK\3\2\2\2K\30\3\2\2\2LJ\3\2\2\2M")
        buf.write("N\7/\2\2NO\7/\2\2OS\3\2\2\2PR\n\6\2\2QP\3\2\2\2RU\3\2")
        buf.write("\2\2SQ\3\2\2\2ST\3\2\2\2T\32\3\2\2\2US\3\2\2\2VY\5\25")
        buf.write("\13\2WY\5\31\r\2XV\3\2\2\2XW\3\2\2\2YZ\3\2\2\2Z[\b\16")
        buf.write("\2\2[\34\3\2\2\2\13\2*/\67?DJSX\3\b\2\2")
        return buf.getvalue()


class TaleLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    IDENTIFIER = 6
    NUMBER = 7
    OPERATOR = 8
    STRING = 9
    WS = 10
    NEWLINE = 11
    SKIP_ = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "':'", "','", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "NUMBER", "OPERATOR", "STRING", "WS", "NEWLINE", 
            "SKIP_" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "IDENTIFIER", 
                  "NUMBER", "OPERATOR", "STRING", "WS", "NEWLINE", "COMMENT", 
                  "SKIP_" ]

    grammarFileName = "Tale.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    class TaleDenter(DenterHelper):
        def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
            super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
            self.lexer: TaleLexer = lexer

        def pull_token(self):
            return super(TaleLexer, self.lexer).nextToken()

    denter = None

    def nextToken(self):
        if not self.denter:
            self.denter = self.TaleDenter(self, self.NEWLINE, TaleParser.INDENT, TaleParser.DEDENT, False)

        return self.denter.next_token()


