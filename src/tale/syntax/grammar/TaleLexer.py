# Generated from tale/syntax/grammar/Tale.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from antlr_denter.DenterHelper import DenterHelper
from .TaleParser import TaleParser



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("Z\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\6\6%\n\6\r\6\16\6&\3")
        buf.write("\7\6\7*\n\7\r\7\16\7+\3\b\3\b\3\t\3\t\7\t\62\n\t\f\t\16")
        buf.write("\t\65\13\t\5\t\67\n\t\3\t\3\t\3\n\6\n<\n\n\r\n\16\n=\3")
        buf.write("\n\3\n\3\13\5\13C\n\13\3\13\3\13\7\13G\n\13\f\13\16\13")
        buf.write("J\13\13\3\f\3\f\3\f\3\f\7\fP\n\f\f\f\16\fS\13\f\3\r\3")
        buf.write("\r\5\rW\n\r\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\2\31\r\3\2\7\4\2C\\c|\3\2\62;\5")
        buf.write("\2,-//\61\61\4\2\13\13\"\"\4\2\f\f\16\17\2a\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5\35\3\2\2\2\7\37\3")
        buf.write("\2\2\2\t!\3\2\2\2\13$\3\2\2\2\r)\3\2\2\2\17-\3\2\2\2\21")
        buf.write("/\3\2\2\2\23;\3\2\2\2\25B\3\2\2\2\27K\3\2\2\2\31V\3\2")
        buf.write("\2\2\33\34\7?\2\2\34\4\3\2\2\2\35\36\7<\2\2\36\6\3\2\2")
        buf.write("\2\37 \7*\2\2 \b\3\2\2\2!\"\7+\2\2\"\n\3\2\2\2#%\t\2\2")
        buf.write("\2$#\3\2\2\2%&\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'\f\3\2\2")
        buf.write("\2(*\t\3\2\2)(\3\2\2\2*+\3\2\2\2+)\3\2\2\2+,\3\2\2\2,")
        buf.write("\16\3\2\2\2-.\t\4\2\2.\20\3\2\2\2/\66\7$\2\2\60\62\13")
        buf.write("\2\2\2\61\60\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2\63\64")
        buf.write("\3\2\2\2\64\67\3\2\2\2\65\63\3\2\2\2\66\63\3\2\2\2\66")
        buf.write("\67\3\2\2\2\678\3\2\2\289\7$\2\29\22\3\2\2\2:<\t\5\2\2")
        buf.write(";:\3\2\2\2<=\3\2\2\2=;\3\2\2\2=>\3\2\2\2>?\3\2\2\2?@\b")
        buf.write("\n\2\2@\24\3\2\2\2AC\7\17\2\2BA\3\2\2\2BC\3\2\2\2CD\3")
        buf.write("\2\2\2DH\7\f\2\2EG\7\"\2\2FE\3\2\2\2GJ\3\2\2\2HF\3\2\2")
        buf.write("\2HI\3\2\2\2I\26\3\2\2\2JH\3\2\2\2KL\7/\2\2LM\7/\2\2M")
        buf.write("Q\3\2\2\2NP\n\6\2\2ON\3\2\2\2PS\3\2\2\2QO\3\2\2\2QR\3")
        buf.write("\2\2\2R\30\3\2\2\2SQ\3\2\2\2TW\5\23\n\2UW\5\27\f\2VT\3")
        buf.write("\2\2\2VU\3\2\2\2WX\3\2\2\2XY\b\r\2\2Y\32\3\2\2\2\f\2&")
        buf.write("+\63\66=BHQV\3\b\2\2")
        return buf.getvalue()


class TaleLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    IDENTIFIER = 5
    NUMBER = 6
    OPERATOR = 7
    STRING = 8
    WS = 9
    NEWLINE = 10
    SKIP_ = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "':'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "NUMBER", "OPERATOR", "STRING", "WS", "NEWLINE", 
            "SKIP_" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "IDENTIFIER", "NUMBER", 
                  "OPERATOR", "STRING", "WS", "NEWLINE", "COMMENT", "SKIP_" ]

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


