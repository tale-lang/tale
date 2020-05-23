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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("\u00cd\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\3\2\3\2\7\2\65\n\2\f\2\16\28\13\2\7\2:\n\2\f\2\16")
        buf.write("\2=\13\2\3\3\3\3\5\3A\n\3\3\4\3\4\3\4\3\4\5\4G\n\4\3\5")
        buf.write("\3\5\5\5K\n\5\3\6\3\6\3\6\3\6\3\6\5\6R\n\6\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\5\n_\n\n\3\n\3\n\3\n")
        buf.write("\6\nd\n\n\r\n\16\ne\3\13\3\13\3\13\3\13\5\13l\n\13\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\5\16x\n\16\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u008b\n\21\3\21\3")
        buf.write("\21\7\21\u008f\n\21\f\21\16\21\u0092\13\21\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\7\22\u009c\n\22\f\22\16\22")
        buf.write("\u009f\13\22\3\23\3\23\3\23\3\23\5\23\u00a5\n\23\3\24")
        buf.write("\5\24\u00a8\n\24\3\24\3\24\3\24\3\24\6\24\u00ae\n\24\r")
        buf.write("\24\16\24\u00af\3\25\3\25\3\25\3\25\3\25\5\25\u00b7\n")
        buf.write("\25\3\26\3\26\3\27\3\27\3\27\3\27\3\27\5\27\u00c0\n\27")
        buf.write("\3\30\3\30\3\30\5\30\u00c5\n\30\3\31\3\31\3\31\3\31\5")
        buf.write("\31\u00cb\n\31\3\31\2\4 \"\32\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\2\2\2\u00d7\2;\3\2\2\2\4@")
        buf.write("\3\2\2\2\6B\3\2\2\2\bJ\3\2\2\2\nQ\3\2\2\2\fS\3\2\2\2\16")
        buf.write("V\3\2\2\2\20Y\3\2\2\2\22^\3\2\2\2\24g\3\2\2\2\26o\3\2")
        buf.write("\2\2\30q\3\2\2\2\32w\3\2\2\2\34y\3\2\2\2\36}\3\2\2\2 ")
        buf.write("\u008a\3\2\2\2\"\u0093\3\2\2\2$\u00a4\3\2\2\2&\u00a7\3")
        buf.write("\2\2\2(\u00b6\3\2\2\2*\u00b8\3\2\2\2,\u00bf\3\2\2\2.\u00c4")
        buf.write("\3\2\2\2\60\u00ca\3\2\2\2\62\66\5\4\3\2\63\65\7\13\2\2")
        buf.write("\64\63\3\2\2\2\658\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2")
        buf.write("\67:\3\2\2\28\66\3\2\2\29\62\3\2\2\2:=\3\2\2\2;9\3\2\2")
        buf.write("\2;<\3\2\2\2<\3\3\2\2\2=;\3\2\2\2>A\5\6\4\2?A\5\32\16")
        buf.write("\2@>\3\2\2\2@?\3\2\2\2A\5\3\2\2\2BC\5\b\5\2CF\7\3\2\2")
        buf.write("DG\5\32\16\2EG\5\34\17\2FD\3\2\2\2FE\3\2\2\2G\7\3\2\2")
        buf.write("\2HK\5\n\6\2IK\7\7\2\2JH\3\2\2\2JI\3\2\2\2K\t\3\2\2\2")
        buf.write("LR\5\f\7\2MR\5\16\b\2NR\5\20\t\2OR\5\22\n\2PR\7\7\2\2")
        buf.write("QL\3\2\2\2QM\3\2\2\2QN\3\2\2\2QO\3\2\2\2QP\3\2\2\2R\13")
        buf.write("\3\2\2\2ST\5\24\13\2TU\7\7\2\2U\r\3\2\2\2VW\7\t\2\2WX")
        buf.write("\5\24\13\2X\17\3\2\2\2YZ\5\24\13\2Z[\7\t\2\2[\\\5\24\13")
        buf.write("\2\\\21\3\2\2\2]_\5\24\13\2^]\3\2\2\2^_\3\2\2\2_c\3\2")
        buf.write("\2\2`a\7\7\2\2ab\7\4\2\2bd\5\24\13\2c`\3\2\2\2de\3\2\2")
        buf.write("\2ec\3\2\2\2ef\3\2\2\2f\23\3\2\2\2gh\7\5\2\2hk\5\26\f")
        buf.write("\2ij\7\4\2\2jl\5\30\r\2ki\3\2\2\2kl\3\2\2\2lm\3\2\2\2")
        buf.write("mn\7\6\2\2n\25\3\2\2\2op\7\7\2\2p\27\3\2\2\2qr\7\7\2\2")
        buf.write("r\31\3\2\2\2sx\5 \21\2tx\5\"\22\2ux\5&\24\2vx\5.\30\2")
        buf.write("ws\3\2\2\2wt\3\2\2\2wu\3\2\2\2wv\3\2\2\2x\33\3\2\2\2y")
        buf.write("z\7\5\2\2z{\5\32\16\2{|\7\6\2\2|\35\3\2\2\2}~\7\t\2\2")
        buf.write("~\177\5\34\17\2\177\37\3\2\2\2\u0080\u0081\b\21\1\2\u0081")
        buf.write("\u0082\5\36\20\2\u0082\u0083\7\7\2\2\u0083\u008b\3\2\2")
        buf.write("\2\u0084\u0085\5\34\17\2\u0085\u0086\7\7\2\2\u0086\u008b")
        buf.write("\3\2\2\2\u0087\u0088\5.\30\2\u0088\u0089\7\7\2\2\u0089")
        buf.write("\u008b\3\2\2\2\u008a\u0080\3\2\2\2\u008a\u0084\3\2\2\2")
        buf.write("\u008a\u0087\3\2\2\2\u008b\u0090\3\2\2\2\u008c\u008d\f")
        buf.write("\6\2\2\u008d\u008f\7\7\2\2\u008e\u008c\3\2\2\2\u008f\u0092")
        buf.write("\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091")
        buf.write("!\3\2\2\2\u0092\u0090\3\2\2\2\u0093\u0094\b\22\1\2\u0094")
        buf.write("\u0095\5$\23\2\u0095\u0096\7\t\2\2\u0096\u0097\5$\23\2")
        buf.write("\u0097\u009d\3\2\2\2\u0098\u0099\f\4\2\2\u0099\u009a\7")
        buf.write("\t\2\2\u009a\u009c\5$\23\2\u009b\u0098\3\2\2\2\u009c\u009f")
        buf.write("\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009e\3\2\2\2\u009e")
        buf.write("#\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u00a5\5 \21\2\u00a1")
        buf.write("\u00a5\5.\30\2\u00a2\u00a5\5\36\20\2\u00a3\u00a5\5\34")
        buf.write("\17\2\u00a4\u00a0\3\2\2\2\u00a4\u00a1\3\2\2\2\u00a4\u00a2")
        buf.write("\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5%\3\2\2\2\u00a6\u00a8")
        buf.write("\5(\25\2\u00a7\u00a6\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8")
        buf.write("\u00ad\3\2\2\2\u00a9\u00aa\5*\26\2\u00aa\u00ab\7\4\2\2")
        buf.write("\u00ab\u00ac\5,\27\2\u00ac\u00ae\3\2\2\2\u00ad\u00a9\3")
        buf.write("\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0")
        buf.write("\3\2\2\2\u00b0\'\3\2\2\2\u00b1\u00b7\5 \21\2\u00b2\u00b7")
        buf.write("\5\"\22\2\u00b3\u00b7\5.\30\2\u00b4\u00b7\5\36\20\2\u00b5")
        buf.write("\u00b7\5\34\17\2\u00b6\u00b1\3\2\2\2\u00b6\u00b2\3\2\2")
        buf.write("\2\u00b6\u00b3\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b5")
        buf.write("\3\2\2\2\u00b7)\3\2\2\2\u00b8\u00b9\7\7\2\2\u00b9+\3\2")
        buf.write("\2\2\u00ba\u00c0\5 \21\2\u00bb\u00c0\5\"\22\2\u00bc\u00c0")
        buf.write("\5.\30\2\u00bd\u00c0\5\36\20\2\u00be\u00c0\5\34\17\2\u00bf")
        buf.write("\u00ba\3\2\2\2\u00bf\u00bb\3\2\2\2\u00bf\u00bc\3\2\2\2")
        buf.write("\u00bf\u00bd\3\2\2\2\u00bf\u00be\3\2\2\2\u00c0-\3\2\2")
        buf.write("\2\u00c1\u00c5\5\60\31\2\u00c2\u00c5\7\7\2\2\u00c3\u00c5")
        buf.write("\7\b\2\2\u00c4\u00c1\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4")
        buf.write("\u00c3\3\2\2\2\u00c5/\3\2\2\2\u00c6\u00c7\7\t\2\2\u00c7")
        buf.write("\u00cb\7\7\2\2\u00c8\u00c9\7\t\2\2\u00c9\u00cb\7\b\2\2")
        buf.write("\u00ca\u00c6\3\2\2\2\u00ca\u00c8\3\2\2\2\u00cb\61\3\2")
        buf.write("\2\2\26\66;@FJQ^ekw\u008a\u0090\u009d\u00a4\u00a7\u00af")
        buf.write("\u00b6\u00bf\u00c4\u00ca")
        return buf.getvalue()


class TaleParser ( Parser ):

    grammarFileName = "Tale.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "':'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IDENTIFIER", "NUMBER", "OPERATOR", "WS", 
                      "NEWLINE" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_assignmentName = 3
    RULE_assignmentForm = 4
    RULE_unaryForm = 5
    RULE_unaryOperatorForm = 6
    RULE_binaryForm = 7
    RULE_keywordForm = 8
    RULE_argument = 9
    RULE_argumentName = 10
    RULE_argumentType = 11
    RULE_expression = 12
    RULE_expressionInBrackets = 13
    RULE_expressionInBracketsWithOperator = 14
    RULE_unary = 15
    RULE_binary = 16
    RULE_binaryOperand = 17
    RULE_keyword = 18
    RULE_keywordPrefix = 19
    RULE_keywordName = 20
    RULE_keywordValue = 21
    RULE_primitive = 22
    RULE_primitiveWithOperator = 23

    ruleNames =  [ "program", "statement", "assignment", "assignmentName", 
                   "assignmentForm", "unaryForm", "unaryOperatorForm", "binaryForm", 
                   "keywordForm", "argument", "argumentName", "argumentType", 
                   "expression", "expressionInBrackets", "expressionInBracketsWithOperator", 
                   "unary", "binary", "binaryOperand", "keyword", "keywordPrefix", 
                   "keywordName", "keywordValue", "primitive", "primitiveWithOperator" ]

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

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TaleParser.StatementContext)
            else:
                return self.getTypedRuleContext(TaleParser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(TaleParser.NEWLINE)
            else:
                return self.getToken(TaleParser.NEWLINE, i)

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
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TaleParser.T__2) | (1 << TaleParser.IDENTIFIER) | (1 << TaleParser.NUMBER) | (1 << TaleParser.OPERATOR))) != 0):
                self.state = 48
                self.statement()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==TaleParser.NEWLINE:
                    self.state = 49
                    self.match(TaleParser.NEWLINE)
                    self.state = 54
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 59
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
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
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

        def assignmentName(self):
            return self.getTypedRuleContext(TaleParser.AssignmentNameContext,0)


        def expression(self):
            return self.getTypedRuleContext(TaleParser.ExpressionContext,0)


        def expressionInBrackets(self):
            return self.getTypedRuleContext(TaleParser.ExpressionInBracketsContext,0)


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
            self.state = 64
            self.assignmentName()
            self.state = 65
            self.match(TaleParser.T__0)
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 66
                self.expression()
                pass

            elif la_ == 2:
                self.state = 67
                self.expressionInBrackets()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentForm(self):
            return self.getTypedRuleContext(TaleParser.AssignmentFormContext,0)


        def IDENTIFIER(self):
            return self.getToken(TaleParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return TaleParser.RULE_assignmentName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentName" ):
                listener.enterAssignmentName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentName" ):
                listener.exitAssignmentName(self)




    def assignmentName(self):

        localctx = TaleParser.AssignmentNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignmentName)
        try:
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.assignmentForm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.match(TaleParser.IDENTIFIER)
                pass


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


        def IDENTIFIER(self):
            return self.getToken(TaleParser.IDENTIFIER, 0)

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
        self.enterRule(localctx, 8, self.RULE_assignmentForm)
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.unaryForm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.unaryOperatorForm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.binaryForm()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 77
                self.keywordForm()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 78
                self.match(TaleParser.IDENTIFIER)
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

        def argument(self):
            return self.getTypedRuleContext(TaleParser.ArgumentContext,0)


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
        self.enterRule(localctx, 10, self.RULE_unaryForm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.argument()
            self.state = 82
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

        def argument(self):
            return self.getTypedRuleContext(TaleParser.ArgumentContext,0)


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
        self.enterRule(localctx, 12, self.RULE_unaryOperatorForm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(TaleParser.OPERATOR)
            self.state = 85
            self.argument()
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

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TaleParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(TaleParser.ArgumentContext,i)


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
        self.enterRule(localctx, 14, self.RULE_binaryForm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.argument()
            self.state = 88
            self.match(TaleParser.OPERATOR)
            self.state = 89
            self.argument()
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

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TaleParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(TaleParser.ArgumentContext,i)


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
        self.enterRule(localctx, 16, self.RULE_keywordForm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TaleParser.T__2:
                self.state = 91
                self.argument()


            self.state = 97 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 94
                self.match(TaleParser.IDENTIFIER)
                self.state = 95
                self.match(TaleParser.T__1)
                self.state = 96
                self.argument()
                self.state = 99 
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


    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argumentName(self):
            return self.getTypedRuleContext(TaleParser.ArgumentNameContext,0)


        def argumentType(self):
            return self.getTypedRuleContext(TaleParser.ArgumentTypeContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)




    def argument(self):

        localctx = TaleParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(TaleParser.T__2)
            self.state = 102
            self.argumentName()
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TaleParser.T__1:
                self.state = 103
                self.match(TaleParser.T__1)
                self.state = 104
                self.argumentType()


            self.state = 107
            self.match(TaleParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TaleParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return TaleParser.RULE_argumentName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentName" ):
                listener.enterArgumentName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentName" ):
                listener.exitArgumentName(self)




    def argumentName(self):

        localctx = TaleParser.ArgumentNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_argumentName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(TaleParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TaleParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return TaleParser.RULE_argumentType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentType" ):
                listener.enterArgumentType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentType" ):
                listener.exitArgumentType(self)




    def argumentType(self):

        localctx = TaleParser.ArgumentTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_argumentType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(TaleParser.IDENTIFIER)
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
        self.enterRule(localctx, 24, self.RULE_expression)
        try:
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.unary(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.binary(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 115
                self.keyword()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 116
                self.primitive()
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
        self.enterRule(localctx, 26, self.RULE_expressionInBrackets)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(TaleParser.T__2)
            self.state = 120
            self.expression()
            self.state = 121
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
        self.enterRule(localctx, 28, self.RULE_expressionInBracketsWithOperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(TaleParser.OPERATOR)
            self.state = 124
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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_unary, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 127
                self.expressionInBracketsWithOperator()
                self.state = 128
                self.match(TaleParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 130
                self.expressionInBrackets()
                self.state = 131
                self.match(TaleParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.state = 133
                self.primitive()
                self.state = 134
                self.match(TaleParser.IDENTIFIER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 142
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TaleParser.UnaryContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_unary)
                    self.state = 138
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 139
                    self.match(TaleParser.IDENTIFIER) 
                self.state = 144
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_binary, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.binaryOperand()
            self.state = 147
            self.match(TaleParser.OPERATOR)
            self.state = 148
            self.binaryOperand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 155
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TaleParser.BinaryContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_binary)
                    self.state = 150
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 151
                    self.match(TaleParser.OPERATOR)
                    self.state = 152
                    self.binaryOperand() 
                self.state = 157
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        self.enterRule(localctx, 34, self.RULE_binaryOperand)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.unary(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.primitive()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 160
                self.expressionInBracketsWithOperator()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 161
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
        self.enterRule(localctx, 36, self.RULE_keyword)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 164
                self.keywordPrefix()


            self.state = 171 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 167
                    self.keywordName()
                    self.state = 168
                    self.match(TaleParser.T__1)
                    self.state = 169
                    self.keywordValue()

                else:
                    raise NoViableAltException(self)
                self.state = 173 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        self.enterRule(localctx, 38, self.RULE_keywordPrefix)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.unary(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.binary(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 177
                self.primitive()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 178
                self.expressionInBracketsWithOperator()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 179
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
        self.enterRule(localctx, 40, self.RULE_keywordName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
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
        self.enterRule(localctx, 42, self.RULE_keywordValue)
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.unary(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.binary(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 186
                self.primitive()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 187
                self.expressionInBracketsWithOperator()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 188
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
        self.enterRule(localctx, 44, self.RULE_primitive)
        try:
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.OPERATOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.primitiveWithOperator()
                pass
            elif token in [TaleParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.match(TaleParser.IDENTIFIER)
                pass
            elif token in [TaleParser.NUMBER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 193
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
        self.enterRule(localctx, 46, self.RULE_primitiveWithOperator)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.match(TaleParser.OPERATOR)
                self.state = 197
                self.match(TaleParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.match(TaleParser.OPERATOR)
                self.state = 199
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
        self._predicates[15] = self.unary_sempred
        self._predicates[16] = self.binary_sempred
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
         




