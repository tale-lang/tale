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
        buf.write("^\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\6\7")
        buf.write(")\n\7\r\7\16\7*\3\b\6\b.\n\b\r\b\16\b/\3\t\3\t\3\n\3\n")
        buf.write("\7\n\66\n\n\f\n\16\n9\13\n\5\n;\n\n\3\n\3\n\3\13\6\13")
        buf.write("@\n\13\r\13\16\13A\3\13\3\13\3\f\5\fG\n\f\3\f\3\f\7\f")
        buf.write("K\n\f\f\f\16\fN\13\f\3\r\3\r\3\r\3\r\7\rT\n\r\f\r\16\r")
        buf.write("W\13\r\3\16\3\16\5\16[\n\16\3\16\3\16\2\2\17\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\2\33\16\3")
        buf.write("\2\7\4\2C\\c|\3\2\62;\5\2,-//\61\61\4\2\13\13\"\"\4\2")
        buf.write("\f\f\16\17\2e\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\33\3\2")
        buf.write("\2\2\3\35\3\2\2\2\5\37\3\2\2\2\7!\3\2\2\2\t#\3\2\2\2\13")
        buf.write("%\3\2\2\2\r(\3\2\2\2\17-\3\2\2\2\21\61\3\2\2\2\23\63\3")
        buf.write("\2\2\2\25?\3\2\2\2\27F\3\2\2\2\31O\3\2\2\2\33Z\3\2\2\2")
        buf.write("\35\36\7?\2\2\36\4\3\2\2\2\37 \7<\2\2 \6\3\2\2\2!\"\7")
        buf.write("*\2\2\"\b\3\2\2\2#$\7+\2\2$\n\3\2\2\2%&\7.\2\2&\f\3\2")
        buf.write("\2\2\')\t\2\2\2(\'\3\2\2\2)*\3\2\2\2*(\3\2\2\2*+\3\2\2")
        buf.write("\2+\16\3\2\2\2,.\t\3\2\2-,\3\2\2\2./\3\2\2\2/-\3\2\2\2")
        buf.write("/\60\3\2\2\2\60\20\3\2\2\2\61\62\t\4\2\2\62\22\3\2\2\2")
        buf.write("\63:\7$\2\2\64\66\13\2\2\2\65\64\3\2\2\2\669\3\2\2\2\67")
        buf.write("\65\3\2\2\2\678\3\2\2\28;\3\2\2\29\67\3\2\2\2:\67\3\2")
        buf.write("\2\2:;\3\2\2\2;<\3\2\2\2<=\7$\2\2=\24\3\2\2\2>@\t\5\2")
        buf.write("\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2AB\3\2\2\2BC\3\2\2\2C")
        buf.write("D\b\13\2\2D\26\3\2\2\2EG\7\17\2\2FE\3\2\2\2FG\3\2\2\2")
        buf.write("GH\3\2\2\2HL\7\f\2\2IK\7\"\2\2JI\3\2\2\2KN\3\2\2\2LJ\3")
        buf.write("\2\2\2LM\3\2\2\2M\30\3\2\2\2NL\3\2\2\2OP\7/\2\2PQ\7/\2")
        buf.write("\2QU\3\2\2\2RT\n\6\2\2SR\3\2\2\2TW\3\2\2\2US\3\2\2\2U")
        buf.write("V\3\2\2\2V\32\3\2\2\2WU\3\2\2\2X[\5\25\13\2Y[\5\31\r\2")
        buf.write("ZX\3\2\2\2ZY\3\2\2\2[\\\3\2\2\2\\]\b\16\2\2]\34\3\2\2")
        buf.write("\2\f\2*/\67:AFLUZ\3\b\2\2")
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
            "'='", "':'", "'('", "')'", "','" ]

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


