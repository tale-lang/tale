# Generated from tale/syntax/grammar/Tale.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("\u00e6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\3\2\3\2\7\2?\n\2\f\2\16\2B\13\2\3\3\3\3\5\3F\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\5\5Q\n\5\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\5\t^\n\t\3\t\3\t\3\t")
        buf.write("\6\tc\n\t\r\t\16\td\3\n\3\n\3\13\3\13\5\13k\n\13\3\f\3")
        buf.write("\f\3\f\3\f\5\fq\n\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17")
        buf.write("\3\20\3\20\5\20}\n\20\3\21\3\21\5\21\u0081\n\21\3\22\3")
        buf.write("\22\6\22\u0085\n\22\r\22\16\22\u0086\3\22\3\22\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\5\23\u0091\n\23\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\5\26\u00a4\n\26\3\26\3\26\7\26\u00a8\n")
        buf.write("\26\f\26\16\26\u00ab\13\26\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\3\27\7\27\u00b5\n\27\f\27\16\27\u00b8\13\27\3")
        buf.write("\30\3\30\3\30\3\30\5\30\u00be\n\30\3\31\5\31\u00c1\n\31")
        buf.write("\3\31\3\31\3\31\3\31\6\31\u00c7\n\31\r\31\16\31\u00c8")
        buf.write("\3\32\3\32\3\32\3\32\3\32\5\32\u00d0\n\32\3\33\3\33\3")
        buf.write("\34\3\34\3\34\3\34\3\34\5\34\u00d9\n\34\3\35\3\35\3\35")
        buf.write("\5\35\u00de\n\35\3\36\3\36\3\36\3\36\5\36\u00e4\n\36\3")
        buf.write("\36\2\4*,\37\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:\2\3\3\2\7\b\2\u00ed\2@\3\2\2\2\4")
        buf.write("E\3\2\2\2\6G\3\2\2\2\bP\3\2\2\2\nR\3\2\2\2\fU\3\2\2\2")
        buf.write("\16X\3\2\2\2\20]\3\2\2\2\22f\3\2\2\2\24j\3\2\2\2\26l\3")
        buf.write("\2\2\2\30t\3\2\2\2\32v\3\2\2\2\34x\3\2\2\2\36|\3\2\2\2")
        buf.write(" \u0080\3\2\2\2\"\u0082\3\2\2\2$\u0090\3\2\2\2&\u0092")
        buf.write("\3\2\2\2(\u0096\3\2\2\2*\u00a3\3\2\2\2,\u00ac\3\2\2\2")
        buf.write(".\u00bd\3\2\2\2\60\u00c0\3\2\2\2\62\u00cf\3\2\2\2\64\u00d1")
        buf.write("\3\2\2\2\66\u00d8\3\2\2\28\u00dd\3\2\2\2:\u00e3\3\2\2")
        buf.write("\2<?\7\13\2\2=?\5\4\3\2><\3\2\2\2>=\3\2\2\2?B\3\2\2\2")
        buf.write("@>\3\2\2\2@A\3\2\2\2A\3\3\2\2\2B@\3\2\2\2CF\5\6\4\2DF")
        buf.write("\5$\23\2EC\3\2\2\2ED\3\2\2\2F\5\3\2\2\2GH\5\b\5\2HI\7")
        buf.write("\3\2\2IJ\5\36\20\2J\7\3\2\2\2KQ\5\n\6\2LQ\5\f\7\2MQ\5")
        buf.write("\16\b\2NQ\5\20\t\2OQ\5\22\n\2PK\3\2\2\2PL\3\2\2\2PM\3")
        buf.write("\2\2\2PN\3\2\2\2PO\3\2\2\2Q\t\3\2\2\2RS\5\24\13\2ST\7")
        buf.write("\7\2\2T\13\3\2\2\2UV\7\t\2\2VW\5\24\13\2W\r\3\2\2\2XY")
        buf.write("\5\24\13\2YZ\7\t\2\2Z[\5\24\13\2[\17\3\2\2\2\\^\5\24\13")
        buf.write("\2]\\\3\2\2\2]^\3\2\2\2^b\3\2\2\2_`\7\7\2\2`a\7\4\2\2")
        buf.write("ac\5\24\13\2b_\3\2\2\2cd\3\2\2\2db\3\2\2\2de\3\2\2\2e")
        buf.write("\21\3\2\2\2fg\7\7\2\2g\23\3\2\2\2hk\5\26\f\2ik\5\30\r")
        buf.write("\2jh\3\2\2\2ji\3\2\2\2k\25\3\2\2\2lm\7\5\2\2mp\5\32\16")
        buf.write("\2no\7\4\2\2oq\5\34\17\2pn\3\2\2\2pq\3\2\2\2qr\3\2\2\2")
        buf.write("rs\7\6\2\2s\27\3\2\2\2tu\t\2\2\2u\31\3\2\2\2vw\7\7\2\2")
        buf.write("w\33\3\2\2\2xy\7\7\2\2y\35\3\2\2\2z}\5 \21\2{}\5\"\22")
        buf.write("\2|z\3\2\2\2|{\3\2\2\2}\37\3\2\2\2~\u0081\5$\23\2\177")
        buf.write("\u0081\5&\24\2\u0080~\3\2\2\2\u0080\177\3\2\2\2\u0081")
        buf.write("!\3\2\2\2\u0082\u0084\7\r\2\2\u0083\u0085\5\4\3\2\u0084")
        buf.write("\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0084\3\2\2\2")
        buf.write("\u0086\u0087\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089\7")
        buf.write("\16\2\2\u0089#\3\2\2\2\u008a\u0091\5*\26\2\u008b\u0091")
        buf.write("\5,\27\2\u008c\u0091\5\60\31\2\u008d\u008e\58\35\2\u008e")
        buf.write("\u008f\7\13\2\2\u008f\u0091\3\2\2\2\u0090\u008a\3\2\2")
        buf.write("\2\u0090\u008b\3\2\2\2\u0090\u008c\3\2\2\2\u0090\u008d")
        buf.write("\3\2\2\2\u0091%\3\2\2\2\u0092\u0093\7\5\2\2\u0093\u0094")
        buf.write("\5$\23\2\u0094\u0095\7\6\2\2\u0095\'\3\2\2\2\u0096\u0097")
        buf.write("\7\t\2\2\u0097\u0098\5&\24\2\u0098)\3\2\2\2\u0099\u009a")
        buf.write("\b\26\1\2\u009a\u009b\5(\25\2\u009b\u009c\7\7\2\2\u009c")
        buf.write("\u00a4\3\2\2\2\u009d\u009e\5&\24\2\u009e\u009f\7\7\2\2")
        buf.write("\u009f\u00a4\3\2\2\2\u00a0\u00a1\58\35\2\u00a1\u00a2\7")
        buf.write("\7\2\2\u00a2\u00a4\3\2\2\2\u00a3\u0099\3\2\2\2\u00a3\u009d")
        buf.write("\3\2\2\2\u00a3\u00a0\3\2\2\2\u00a4\u00a9\3\2\2\2\u00a5")
        buf.write("\u00a6\f\6\2\2\u00a6\u00a8\7\7\2\2\u00a7\u00a5\3\2\2\2")
        buf.write("\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3")
        buf.write("\2\2\2\u00aa+\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00ad")
        buf.write("\b\27\1\2\u00ad\u00ae\5.\30\2\u00ae\u00af\7\t\2\2\u00af")
        buf.write("\u00b0\5.\30\2\u00b0\u00b6\3\2\2\2\u00b1\u00b2\f\4\2\2")
        buf.write("\u00b2\u00b3\7\t\2\2\u00b3\u00b5\5.\30\2\u00b4\u00b1\3")
        buf.write("\2\2\2\u00b5\u00b8\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7")
        buf.write("\3\2\2\2\u00b7-\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b9\u00be")
        buf.write("\5*\26\2\u00ba\u00be\58\35\2\u00bb\u00be\5(\25\2\u00bc")
        buf.write("\u00be\5&\24\2\u00bd\u00b9\3\2\2\2\u00bd\u00ba\3\2\2\2")
        buf.write("\u00bd\u00bb\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be/\3\2\2")
        buf.write("\2\u00bf\u00c1\5\62\32\2\u00c0\u00bf\3\2\2\2\u00c0\u00c1")
        buf.write("\3\2\2\2\u00c1\u00c6\3\2\2\2\u00c2\u00c3\5\64\33\2\u00c3")
        buf.write("\u00c4\7\4\2\2\u00c4\u00c5\5\66\34\2\u00c5\u00c7\3\2\2")
        buf.write("\2\u00c6\u00c2\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c6")
        buf.write("\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\61\3\2\2\2\u00ca\u00d0")
        buf.write("\5*\26\2\u00cb\u00d0\5,\27\2\u00cc\u00d0\58\35\2\u00cd")
        buf.write("\u00d0\5(\25\2\u00ce\u00d0\5&\24\2\u00cf\u00ca\3\2\2\2")
        buf.write("\u00cf\u00cb\3\2\2\2\u00cf\u00cc\3\2\2\2\u00cf\u00cd\3")
        buf.write("\2\2\2\u00cf\u00ce\3\2\2\2\u00d0\63\3\2\2\2\u00d1\u00d2")
        buf.write("\7\7\2\2\u00d2\65\3\2\2\2\u00d3\u00d9\5*\26\2\u00d4\u00d9")
        buf.write("\5,\27\2\u00d5\u00d9\58\35\2\u00d6\u00d9\5(\25\2\u00d7")
        buf.write("\u00d9\5&\24\2\u00d8\u00d3\3\2\2\2\u00d8\u00d4\3\2\2\2")
        buf.write("\u00d8\u00d5\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d7\3")
        buf.write("\2\2\2\u00d9\67\3\2\2\2\u00da\u00de\5:\36\2\u00db\u00de")
        buf.write("\7\7\2\2\u00dc\u00de\7\b\2\2\u00dd\u00da\3\2\2\2\u00dd")
        buf.write("\u00db\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de9\3\2\2\2\u00df")
        buf.write("\u00e0\7\t\2\2\u00e0\u00e4\7\7\2\2\u00e1\u00e2\7\t\2\2")
        buf.write("\u00e2\u00e4\7\b\2\2\u00e3\u00df\3\2\2\2\u00e3\u00e1\3")
        buf.write("\2\2\2\u00e4;\3\2\2\2\30>@EP]djp|\u0080\u0086\u0090\u00a3")
        buf.write("\u00a9\u00b6\u00bd\u00c0\u00c8\u00cf\u00d8\u00dd\u00e3")
        return buf.getvalue()


class TaleParser ( Parser ):

    grammarFileName = "Tale.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "':'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IDENTIFIER", "NUMBER", "OPERATOR", "WS", 
                      "NEWLINE", "SKIP_", "INDENT", "DEDENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_assignmentForm = 3
    RULE_unaryForm = 4
    RULE_unaryOperatorForm = 5
    RULE_binaryForm = 6
    RULE_keywordForm = 7
    RULE_simpleForm = 8
    RULE_parameter = 9
    RULE_simpleParameter = 10
    RULE_patternMatchingParameter = 11
    RULE_parameterName = 12
    RULE_parameterType = 13
    RULE_assignmentBody = 14
    RULE_simpleAssignmentBody = 15
    RULE_compoundAssignmentBody = 16
    RULE_expression = 17
    RULE_expressionInBrackets = 18
    RULE_expressionInBracketsWithOperator = 19
    RULE_unary = 20
    RULE_binary = 21
    RULE_binaryOperand = 22
    RULE_keyword = 23
    RULE_keywordPrefix = 24
    RULE_keywordName = 25
    RULE_keywordValue = 26
    RULE_primitive = 27
    RULE_primitiveWithOperator = 28

    ruleNames =  [ "program", "statement", "assignment", "assignmentForm", 
                   "unaryForm", "unaryOperatorForm", "binaryForm", "keywordForm", 
                   "simpleForm", "parameter", "simpleParameter", "patternMatchingParameter", 
                   "parameterName", "parameterType", "assignmentBody", "simpleAssignmentBody", 
                   "compoundAssignmentBody", "expression", "expressionInBrackets", 
                   "expressionInBracketsWithOperator", "unary", "binary", 
                   "binaryOperand", "keyword", "keywordPrefix", "keywordName", 
                   "keywordValue", "primitive", "primitiveWithOperator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    IDENTIFIER=5
    NUMBER=6
    OPERATOR=7
    WS=8
    NEWLINE=9
    SKIP_=10
    INDENT=11
    DEDENT=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(TaleParser.NEWLINE)
            else:
                return self.getToken(TaleParser.NEWLINE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TaleParser.StatementContext)
            else:
                return self.getTypedRuleContext(TaleParser.StatementContext,i)


        def getRuleIndex(self):
            return TaleParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = TaleParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TaleParser.T__2) | (1 << TaleParser.IDENTIFIER) | (1 << TaleParser.NUMBER) | (1 << TaleParser.OPERATOR) | (1 << TaleParser.NEWLINE))) != 0):
                self.state = 60
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [TaleParser.NEWLINE]:
                    self.state = 58
                    self.match(TaleParser.NEWLINE)
                    pass
                elif token in [TaleParser.T__2, TaleParser.IDENTIFIER, TaleParser.NUMBER, TaleParser.OPERATOR]:
                    self.state = 59
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(TaleParser.AssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(TaleParser.ExpressionContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = TaleParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentForm(self):
            return self.getTypedRuleContext(TaleParser.AssignmentFormContext,0)


        def assignmentBody(self):
            return self.getTypedRuleContext(TaleParser.AssignmentBodyContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = TaleParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.assignmentForm()
            self.state = 70
            self.match(TaleParser.T__0)
            self.state = 71
            self.assignmentBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentFormContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryForm(self):
            return self.getTypedRuleContext(TaleParser.UnaryFormContext,0)


        def unaryOperatorForm(self):
            return self.getTypedRuleContext(TaleParser.UnaryOperatorFormContext,0)


        def binaryForm(self):
            return self.getTypedRuleContext(TaleParser.BinaryFormContext,0)


        def keywordForm(self):
            return self.getTypedRuleContext(TaleParser.KeywordFormContext,0)


        def simpleForm(self):
            return self.getTypedRuleContext(TaleParser.SimpleFormContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_assignmentForm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentForm" ):
                listener.enterAssignmentForm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentForm" ):
                listener.exitAssignmentForm(self)




    def assignmentForm(self):

        localctx = TaleParser.AssignmentFormContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignmentForm)
        try:
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.unaryForm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.unaryOperatorForm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.binaryForm()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 76
                self.keywordForm()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 77
                self.simpleForm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryFormContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(TaleParser.ParameterContext,0)


        def IDENTIFIER(self):
            return self.getToken(TaleParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return TaleParser.RULE_unaryForm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryForm" ):
                listener.enterUnaryForm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryForm" ):
                listener.exitUnaryForm(self)




    def unaryForm(self):

        localctx = TaleParser.UnaryFormContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_unaryForm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.parameter()
            self.state = 81
            self.match(TaleParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryOperatorFormContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPERATOR(self):
            return self.getToken(TaleParser.OPERATOR, 0)

        def parameter(self):
            return self.getTypedRuleContext(TaleParser.ParameterContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_unaryOperatorForm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOperatorForm" ):
                listener.enterUnaryOperatorForm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOperatorForm" ):
                listener.exitUnaryOperatorForm(self)




    def unaryOperatorForm(self):

        localctx = TaleParser.UnaryOperatorFormContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_unaryOperatorForm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(TaleParser.OPERATOR)
            self.state = 84
            self.parameter()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinaryFormContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TaleParser.ParameterContext)
            else:
                return self.getTypedRuleContext(TaleParser.ParameterContext,i)


        def OPERATOR(self):
            return self.getToken(TaleParser.OPERATOR, 0)

        def getRuleIndex(self):
            return TaleParser.RULE_binaryForm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryForm" ):
                listener.enterBinaryForm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryForm" ):
                listener.exitBinaryForm(self)




    def binaryForm(self):

        localctx = TaleParser.BinaryFormContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_binaryForm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.parameter()
            self.state = 87
            self.match(TaleParser.OPERATOR)
            self.state = 88
            self.parameter()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeywordFormContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TaleParser.ParameterContext)
            else:
                return self.getTypedRuleContext(TaleParser.ParameterContext,i)


        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(TaleParser.IDENTIFIER)
            else:
                return self.getToken(TaleParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return TaleParser.RULE_keywordForm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeywordForm" ):
                listener.enterKeywordForm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeywordForm" ):
                listener.exitKeywordForm(self)




    def keywordForm(self):

        localctx = TaleParser.KeywordFormContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_keywordForm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 90
                self.parameter()


            self.state = 96 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 93
                self.match(TaleParser.IDENTIFIER)
                self.state = 94
                self.match(TaleParser.T__1)
                self.state = 95
                self.parameter()
                self.state = 98 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==TaleParser.IDENTIFIER):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleFormContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TaleParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return TaleParser.RULE_simpleForm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleForm" ):
                listener.enterSimpleForm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleForm" ):
                listener.exitSimpleForm(self)




    def simpleForm(self):

        localctx = TaleParser.SimpleFormContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_simpleForm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(TaleParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleParameter(self):
            return self.getTypedRuleContext(TaleParser.SimpleParameterContext,0)


        def patternMatchingParameter(self):
            return self.getTypedRuleContext(TaleParser.PatternMatchingParameterContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = TaleParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parameter)
        try:
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.simpleParameter()
                pass
            elif token in [TaleParser.IDENTIFIER, TaleParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.patternMatchingParameter()
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


    class SimpleParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameterName(self):
            return self.getTypedRuleContext(TaleParser.ParameterNameContext,0)


        def parameterType(self):
            return self.getTypedRuleContext(TaleParser.ParameterTypeContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_simpleParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleParameter" ):
                listener.enterSimpleParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleParameter" ):
                listener.exitSimpleParameter(self)




    def simpleParameter(self):

        localctx = TaleParser.SimpleParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_simpleParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(TaleParser.T__2)
            self.state = 107
            self.parameterName()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TaleParser.T__1:
                self.state = 108
                self.match(TaleParser.T__1)
                self.state = 109
                self.parameterType()


            self.state = 112
            self.match(TaleParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PatternMatchingParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TaleParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(TaleParser.NUMBER, 0)

        def getRuleIndex(self):
            return TaleParser.RULE_patternMatchingParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternMatchingParameter" ):
                listener.enterPatternMatchingParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternMatchingParameter" ):
                listener.exitPatternMatchingParameter(self)




    def patternMatchingParameter(self):

        localctx = TaleParser.PatternMatchingParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_patternMatchingParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            _la = self._input.LA(1)
            if not(_la==TaleParser.IDENTIFIER or _la==TaleParser.NUMBER):
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


    class ParameterNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TaleParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return TaleParser.RULE_parameterName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterName" ):
                listener.enterParameterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterName" ):
                listener.exitParameterName(self)




    def parameterName(self):

        localctx = TaleParser.ParameterNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameterName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(TaleParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TaleParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return TaleParser.RULE_parameterType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterType" ):
                listener.enterParameterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterType" ):
                listener.exitParameterType(self)




    def parameterType(self):

        localctx = TaleParser.ParameterTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parameterType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(TaleParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentBodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleAssignmentBody(self):
            return self.getTypedRuleContext(TaleParser.SimpleAssignmentBodyContext,0)


        def compoundAssignmentBody(self):
            return self.getTypedRuleContext(TaleParser.CompoundAssignmentBodyContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_assignmentBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentBody" ):
                listener.enterAssignmentBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentBody" ):
                listener.exitAssignmentBody(self)




    def assignmentBody(self):

        localctx = TaleParser.AssignmentBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assignmentBody)
        try:
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.T__2, TaleParser.IDENTIFIER, TaleParser.NUMBER, TaleParser.OPERATOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.simpleAssignmentBody()
                pass
            elif token in [TaleParser.INDENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.compoundAssignmentBody()
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


    class SimpleAssignmentBodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(TaleParser.ExpressionContext,0)


        def expressionInBrackets(self):
            return self.getTypedRuleContext(TaleParser.ExpressionInBracketsContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_simpleAssignmentBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleAssignmentBody" ):
                listener.enterSimpleAssignmentBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleAssignmentBody" ):
                listener.exitSimpleAssignmentBody(self)




    def simpleAssignmentBody(self):

        localctx = TaleParser.SimpleAssignmentBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_simpleAssignmentBody)
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.expressionInBrackets()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundAssignmentBodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(TaleParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(TaleParser.DEDENT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TaleParser.StatementContext)
            else:
                return self.getTypedRuleContext(TaleParser.StatementContext,i)


        def getRuleIndex(self):
            return TaleParser.RULE_compoundAssignmentBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundAssignmentBody" ):
                listener.enterCompoundAssignmentBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundAssignmentBody" ):
                listener.exitCompoundAssignmentBody(self)




    def compoundAssignmentBody(self):

        localctx = TaleParser.CompoundAssignmentBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_compoundAssignmentBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(TaleParser.INDENT)
            self.state = 130 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 129
                self.statement()
                self.state = 132 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TaleParser.T__2) | (1 << TaleParser.IDENTIFIER) | (1 << TaleParser.NUMBER) | (1 << TaleParser.OPERATOR))) != 0)):
                    break

            self.state = 134
            self.match(TaleParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(TaleParser.UnaryContext,0)


        def binary(self):
            return self.getTypedRuleContext(TaleParser.BinaryContext,0)


        def keyword(self):
            return self.getTypedRuleContext(TaleParser.KeywordContext,0)


        def primitive(self):
            return self.getTypedRuleContext(TaleParser.PrimitiveContext,0)


        def NEWLINE(self):
            return self.getToken(TaleParser.NEWLINE, 0)

        def getRuleIndex(self):
            return TaleParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = TaleParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expression)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.unary(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.binary(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 138
                self.keyword()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 139
                self.primitive()
                self.state = 140
                self.match(TaleParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionInBracketsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(TaleParser.ExpressionContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_expressionInBrackets

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionInBrackets" ):
                listener.enterExpressionInBrackets(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionInBrackets" ):
                listener.exitExpressionInBrackets(self)




    def expressionInBrackets(self):

        localctx = TaleParser.ExpressionInBracketsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expressionInBrackets)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(TaleParser.T__2)
            self.state = 145
            self.expression()
            self.state = 146
            self.match(TaleParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionInBracketsWithOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPERATOR(self):
            return self.getToken(TaleParser.OPERATOR, 0)

        def expressionInBrackets(self):
            return self.getTypedRuleContext(TaleParser.ExpressionInBracketsContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_expressionInBracketsWithOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionInBracketsWithOperator" ):
                listener.enterExpressionInBracketsWithOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionInBracketsWithOperator" ):
                listener.exitExpressionInBracketsWithOperator(self)




    def expressionInBracketsWithOperator(self):

        localctx = TaleParser.ExpressionInBracketsWithOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expressionInBracketsWithOperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(TaleParser.OPERATOR)
            self.state = 149
            self.expressionInBrackets()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionInBracketsWithOperator(self):
            return self.getTypedRuleContext(TaleParser.ExpressionInBracketsWithOperatorContext,0)


        def IDENTIFIER(self):
            return self.getToken(TaleParser.IDENTIFIER, 0)

        def expressionInBrackets(self):
            return self.getTypedRuleContext(TaleParser.ExpressionInBracketsContext,0)


        def primitive(self):
            return self.getTypedRuleContext(TaleParser.PrimitiveContext,0)


        def unary(self):
            return self.getTypedRuleContext(TaleParser.UnaryContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_unary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)



    def unary(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TaleParser.UnaryContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_unary, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 152
                self.expressionInBracketsWithOperator()
                self.state = 153
                self.match(TaleParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 155
                self.expressionInBrackets()
                self.state = 156
                self.match(TaleParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.state = 158
                self.primitive()
                self.state = 159
                self.match(TaleParser.IDENTIFIER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 167
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TaleParser.UnaryContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_unary)
                    self.state = 163
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 164
                    self.match(TaleParser.IDENTIFIER) 
                self.state = 169
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BinaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def binaryOperand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TaleParser.BinaryOperandContext)
            else:
                return self.getTypedRuleContext(TaleParser.BinaryOperandContext,i)


        def OPERATOR(self):
            return self.getToken(TaleParser.OPERATOR, 0)

        def binary(self):
            return self.getTypedRuleContext(TaleParser.BinaryContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_binary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary" ):
                listener.enterBinary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary" ):
                listener.exitBinary(self)



    def binary(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TaleParser.BinaryContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_binary, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.binaryOperand()
            self.state = 172
            self.match(TaleParser.OPERATOR)
            self.state = 173
            self.binaryOperand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 180
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TaleParser.BinaryContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_binary)
                    self.state = 175
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 176
                    self.match(TaleParser.OPERATOR)
                    self.state = 177
                    self.binaryOperand() 
                self.state = 182
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BinaryOperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(TaleParser.UnaryContext,0)


        def primitive(self):
            return self.getTypedRuleContext(TaleParser.PrimitiveContext,0)


        def expressionInBracketsWithOperator(self):
            return self.getTypedRuleContext(TaleParser.ExpressionInBracketsWithOperatorContext,0)


        def expressionInBrackets(self):
            return self.getTypedRuleContext(TaleParser.ExpressionInBracketsContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_binaryOperand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryOperand" ):
                listener.enterBinaryOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryOperand" ):
                listener.exitBinaryOperand(self)




    def binaryOperand(self):

        localctx = TaleParser.BinaryOperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_binaryOperand)
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.unary(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.primitive()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                self.expressionInBracketsWithOperator()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 186
                self.expressionInBrackets()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeywordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keywordPrefix(self):
            return self.getTypedRuleContext(TaleParser.KeywordPrefixContext,0)


        def keywordName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TaleParser.KeywordNameContext)
            else:
                return self.getTypedRuleContext(TaleParser.KeywordNameContext,i)


        def keywordValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TaleParser.KeywordValueContext)
            else:
                return self.getTypedRuleContext(TaleParser.KeywordValueContext,i)


        def getRuleIndex(self):
            return TaleParser.RULE_keyword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyword" ):
                listener.enterKeyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyword" ):
                listener.exitKeyword(self)




    def keyword(self):

        localctx = TaleParser.KeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_keyword)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 189
                self.keywordPrefix()


            self.state = 196 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 192
                    self.keywordName()
                    self.state = 193
                    self.match(TaleParser.T__1)
                    self.state = 194
                    self.keywordValue()

                else:
                    raise NoViableAltException(self)
                self.state = 198 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeywordPrefixContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(TaleParser.UnaryContext,0)


        def binary(self):
            return self.getTypedRuleContext(TaleParser.BinaryContext,0)


        def primitive(self):
            return self.getTypedRuleContext(TaleParser.PrimitiveContext,0)


        def expressionInBracketsWithOperator(self):
            return self.getTypedRuleContext(TaleParser.ExpressionInBracketsWithOperatorContext,0)


        def expressionInBrackets(self):
            return self.getTypedRuleContext(TaleParser.ExpressionInBracketsContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_keywordPrefix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeywordPrefix" ):
                listener.enterKeywordPrefix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeywordPrefix" ):
                listener.exitKeywordPrefix(self)




    def keywordPrefix(self):

        localctx = TaleParser.KeywordPrefixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_keywordPrefix)
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.unary(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.binary(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 202
                self.primitive()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 203
                self.expressionInBracketsWithOperator()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 204
                self.expressionInBrackets()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeywordNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TaleParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return TaleParser.RULE_keywordName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeywordName" ):
                listener.enterKeywordName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeywordName" ):
                listener.exitKeywordName(self)




    def keywordName(self):

        localctx = TaleParser.KeywordNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_keywordName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(TaleParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeywordValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(TaleParser.UnaryContext,0)


        def binary(self):
            return self.getTypedRuleContext(TaleParser.BinaryContext,0)


        def primitive(self):
            return self.getTypedRuleContext(TaleParser.PrimitiveContext,0)


        def expressionInBracketsWithOperator(self):
            return self.getTypedRuleContext(TaleParser.ExpressionInBracketsWithOperatorContext,0)


        def expressionInBrackets(self):
            return self.getTypedRuleContext(TaleParser.ExpressionInBracketsContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_keywordValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeywordValue" ):
                listener.enterKeywordValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeywordValue" ):
                listener.exitKeywordValue(self)




    def keywordValue(self):

        localctx = TaleParser.KeywordValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_keywordValue)
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.unary(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.binary(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 211
                self.primitive()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 212
                self.expressionInBracketsWithOperator()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 213
                self.expressionInBrackets()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveWithOperator(self):
            return self.getTypedRuleContext(TaleParser.PrimitiveWithOperatorContext,0)


        def IDENTIFIER(self):
            return self.getToken(TaleParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(TaleParser.NUMBER, 0)

        def getRuleIndex(self):
            return TaleParser.RULE_primitive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitive" ):
                listener.enterPrimitive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitive" ):
                listener.exitPrimitive(self)




    def primitive(self):

        localctx = TaleParser.PrimitiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_primitive)
        try:
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.OPERATOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.primitiveWithOperator()
                pass
            elif token in [TaleParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.match(TaleParser.IDENTIFIER)
                pass
            elif token in [TaleParser.NUMBER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 218
                self.match(TaleParser.NUMBER)
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


    class PrimitiveWithOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPERATOR(self):
            return self.getToken(TaleParser.OPERATOR, 0)

        def IDENTIFIER(self):
            return self.getToken(TaleParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(TaleParser.NUMBER, 0)

        def getRuleIndex(self):
            return TaleParser.RULE_primitiveWithOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveWithOperator" ):
                listener.enterPrimitiveWithOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveWithOperator" ):
                listener.exitPrimitiveWithOperator(self)




    def primitiveWithOperator(self):

        localctx = TaleParser.PrimitiveWithOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_primitiveWithOperator)
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(TaleParser.OPERATOR)
                self.state = 222
                self.match(TaleParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.match(TaleParser.OPERATOR)
                self.state = 224
                self.match(TaleParser.NUMBER)
                pass


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
        self._predicates[20] = self.unary_sempred
        self._predicates[21] = self.binary_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def unary_sempred(self, localctx:UnaryContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

    def binary_sempred(self, localctx:BinaryContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




