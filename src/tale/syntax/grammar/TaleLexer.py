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
        buf.write("Q\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\6\7\'\n\7\r\7")
        buf.write("\16\7(\3\b\6\b,\n\b\r\b\16\b-\3\t\3\t\3\n\6\n\63\n\n\r")
        buf.write("\n\16\n\64\3\n\3\n\3\13\5\13:\n\13\3\13\3\13\7\13>\n\13")
        buf.write("\f\13\16\13A\13\13\3\f\3\f\3\f\3\f\7\fG\n\f\f\f\16\fJ")
        buf.write("\13\f\3\r\3\r\5\rN\n\r\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\2\31\r\3\2\7\4\2C\\")
        buf.write("c|\3\2\62;\5\2,-//\61\61\4\2\13\13\"\"\4\2\f\f\16\17\2")
        buf.write("V\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5\35\3\2")
        buf.write("\2\2\7\37\3\2\2\2\t!\3\2\2\2\13#\3\2\2\2\r&\3\2\2\2\17")
        buf.write("+\3\2\2\2\21/\3\2\2\2\23\62\3\2\2\2\259\3\2\2\2\27B\3")
        buf.write("\2\2\2\31M\3\2\2\2\33\34\7?\2\2\34\4\3\2\2\2\35\36\7<")
        buf.write("\2\2\36\6\3\2\2\2\37 \7*\2\2 \b\3\2\2\2!\"\7+\2\2\"\n")
        buf.write("\3\2\2\2#$\7$\2\2$\f\3\2\2\2%\'\t\2\2\2&%\3\2\2\2\'(\3")
        buf.write("\2\2\2(&\3\2\2\2()\3\2\2\2)\16\3\2\2\2*,\t\3\2\2+*\3\2")
        buf.write("\2\2,-\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\20\3\2\2\2/\60\t\4")
        buf.write("\2\2\60\22\3\2\2\2\61\63\t\5\2\2\62\61\3\2\2\2\63\64\3")
        buf.write("\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65\66\3\2\2\2\66\67")
        buf.write("\b\n\2\2\67\24\3\2\2\28:\7\17\2\298\3\2\2\29:\3\2\2\2")
        buf.write(":;\3\2\2\2;?\7\f\2\2<>\7\"\2\2=<\3\2\2\2>A\3\2\2\2?=\3")
        buf.write("\2\2\2?@\3\2\2\2@\26\3\2\2\2A?\3\2\2\2BC\7/\2\2CD\7/\2")
        buf.write("\2DH\3\2\2\2EG\n\6\2\2FE\3\2\2\2GJ\3\2\2\2HF\3\2\2\2H")
        buf.write("I\3\2\2\2I\30\3\2\2\2JH\3\2\2\2KN\5\23\n\2LN\5\27\f\2")
        buf.write("MK\3\2\2\2ML\3\2\2\2NO\3\2\2\2OP\b\r\2\2P\32\3\2\2\2\n")
        buf.write("\2(-\649?HM\3\b\2\2")
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
    WS = 9
    NEWLINE = 10
    SKIP_ = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "':'", "'('", "')'", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "NUMBER", "OPERATOR", "WS", "NEWLINE", "SKIP_" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "IDENTIFIER", 
                  "NUMBER", "OPERATOR", "WS", "NEWLINE", "COMMENT", "SKIP_" ]

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


