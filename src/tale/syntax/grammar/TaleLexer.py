# Generated from tale/syntax/grammar/Tale.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from antlr_denter.DenterHelper import DenterHelper
from .TaleParser import TaleParser



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write(":\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3")
        buf.write("\5\3\6\6\6\37\n\6\r\6\16\6 \3\7\6\7$\n\7\r\7\16\7%\3\b")
        buf.write("\3\b\3\t\6\t+\n\t\r\t\16\t,\3\t\3\t\3\n\5\n\62\n\n\3\n")
        buf.write("\3\n\7\n\66\n\n\f\n\16\n9\13\n\2\2\13\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\3\2\6\4\2C\\c|\3\2\62;\5\2,")
        buf.write("-//\61\61\4\2\13\13\"\"\2>\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\3\25\3\2\2\2\5\27\3\2\2")
        buf.write("\2\7\31\3\2\2\2\t\33\3\2\2\2\13\36\3\2\2\2\r#\3\2\2\2")
        buf.write("\17\'\3\2\2\2\21*\3\2\2\2\23\61\3\2\2\2\25\26\7?\2\2\26")
        buf.write("\4\3\2\2\2\27\30\7<\2\2\30\6\3\2\2\2\31\32\7*\2\2\32\b")
        buf.write("\3\2\2\2\33\34\7+\2\2\34\n\3\2\2\2\35\37\t\2\2\2\36\35")
        buf.write("\3\2\2\2\37 \3\2\2\2 \36\3\2\2\2 !\3\2\2\2!\f\3\2\2\2")
        buf.write("\"$\t\3\2\2#\"\3\2\2\2$%\3\2\2\2%#\3\2\2\2%&\3\2\2\2&")
        buf.write("\16\3\2\2\2\'(\t\4\2\2(\20\3\2\2\2)+\t\5\2\2*)\3\2\2\2")
        buf.write("+,\3\2\2\2,*\3\2\2\2,-\3\2\2\2-.\3\2\2\2./\b\t\2\2/\22")
        buf.write("\3\2\2\2\60\62\7\17\2\2\61\60\3\2\2\2\61\62\3\2\2\2\62")
        buf.write("\63\3\2\2\2\63\67\7\f\2\2\64\66\7\"\2\2\65\64\3\2\2\2")
        buf.write("\669\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28\24\3\2\2\29\67")
        buf.write("\3\2\2\2\b\2 %,\61\67\3\b\2\2")
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
    WS = 8
    NEWLINE = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "':'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "NUMBER", "OPERATOR", "WS", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "IDENTIFIER", "NUMBER", 
                  "OPERATOR", "WS", "NEWLINE" ]

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


