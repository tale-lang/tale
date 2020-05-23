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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("\u00da\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\3\2\3\2\7\29\n\2\f\2\16\2<\13")
        buf.write("\2\3\3\3\3\5\3@\n\3\3\4\3\4\5\4D\n\4\3\5\3\5\3\5\3\5\5")
        buf.write("\5J\n\5\3\6\3\6\3\6\3\6\6\6P\n\6\r\6\16\6Q\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\5\7[\n\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\13\5\13h\n\13\3\13\3\13\3\13\6\13m\n\13")
        buf.write("\r\13\16\13n\3\f\3\f\3\r\3\r\3\r\3\r\5\rw\n\r\3\r\3\r")
        buf.write("\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\5\20")
        buf.write("\u0085\n\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0098")
        buf.write("\n\23\3\23\3\23\7\23\u009c\n\23\f\23\16\23\u009f\13\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u00a9\n")
        buf.write("\24\f\24\16\24\u00ac\13\24\3\25\3\25\3\25\3\25\5\25\u00b2")
        buf.write("\n\25\3\26\5\26\u00b5\n\26\3\26\3\26\3\26\3\26\6\26\u00bb")
        buf.write("\n\26\r\26\16\26\u00bc\3\27\3\27\3\27\3\27\3\27\5\27\u00c4")
        buf.write("\n\27\3\30\3\30\3\31\3\31\3\31\3\31\3\31\5\31\u00cd\n")
        buf.write("\31\3\32\3\32\3\32\5\32\u00d2\n\32\3\33\3\33\3\33\3\33")
        buf.write("\5\33\u00d8\n\33\3\33\2\4$&\34\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\2\2\2\u00e3\2:\3\2\2")
        buf.write("\2\4?\3\2\2\2\6C\3\2\2\2\bE\3\2\2\2\nK\3\2\2\2\fZ\3\2")
        buf.write("\2\2\16\\\3\2\2\2\20_\3\2\2\2\22b\3\2\2\2\24g\3\2\2\2")
        buf.write("\26p\3\2\2\2\30r\3\2\2\2\32z\3\2\2\2\34|\3\2\2\2\36\u0084")
        buf.write("\3\2\2\2 \u0086\3\2\2\2\"\u008a\3\2\2\2$\u0097\3\2\2\2")
        buf.write("&\u00a0\3\2\2\2(\u00b1\3\2\2\2*\u00b4\3\2\2\2,\u00c3\3")
        buf.write("\2\2\2.\u00c5\3\2\2\2\60\u00cc\3\2\2\2\62\u00d1\3\2\2")
        buf.write("\2\64\u00d7\3\2\2\2\669\7\13\2\2\679\5\4\3\28\66\3\2\2")
        buf.write("\28\67\3\2\2\29<\3\2\2\2:8\3\2\2\2:;\3\2\2\2;\3\3\2\2")
        buf.write("\2<:\3\2\2\2=@\5\6\4\2>@\5\36\20\2?=\3\2\2\2?>\3\2\2\2")
        buf.write("@\5\3\2\2\2AD\5\b\5\2BD\5\n\6\2CA\3\2\2\2CB\3\2\2\2D\7")
        buf.write("\3\2\2\2EF\5\f\7\2FI\7\3\2\2GJ\5\36\20\2HJ\5 \21\2IG\3")
        buf.write("\2\2\2IH\3\2\2\2J\t\3\2\2\2KL\5\f\7\2LM\7\3\2\2MO\7\f")
        buf.write("\2\2NP\5\4\3\2ON\3\2\2\2PQ\3\2\2\2QO\3\2\2\2QR\3\2\2\2")
        buf.write("RS\3\2\2\2ST\7\r\2\2T\13\3\2\2\2U[\5\16\b\2V[\5\20\t\2")
        buf.write("W[\5\22\n\2X[\5\24\13\2Y[\5\26\f\2ZU\3\2\2\2ZV\3\2\2\2")
        buf.write("ZW\3\2\2\2ZX\3\2\2\2ZY\3\2\2\2[\r\3\2\2\2\\]\5\30\r\2")
        buf.write("]^\7\7\2\2^\17\3\2\2\2_`\7\t\2\2`a\5\30\r\2a\21\3\2\2")
        buf.write("\2bc\5\30\r\2cd\7\t\2\2de\5\30\r\2e\23\3\2\2\2fh\5\30")
        buf.write("\r\2gf\3\2\2\2gh\3\2\2\2hl\3\2\2\2ij\7\7\2\2jk\7\4\2\2")
        buf.write("km\5\30\r\2li\3\2\2\2mn\3\2\2\2nl\3\2\2\2no\3\2\2\2o\25")
        buf.write("\3\2\2\2pq\7\7\2\2q\27\3\2\2\2rs\7\5\2\2sv\5\32\16\2t")
        buf.write("u\7\4\2\2uw\5\34\17\2vt\3\2\2\2vw\3\2\2\2wx\3\2\2\2xy")
        buf.write("\7\6\2\2y\31\3\2\2\2z{\7\7\2\2{\33\3\2\2\2|}\7\7\2\2}")
        buf.write("\35\3\2\2\2~\u0085\5$\23\2\177\u0085\5&\24\2\u0080\u0085")
        buf.write("\5*\26\2\u0081\u0082\5\62\32\2\u0082\u0083\7\13\2\2\u0083")
        buf.write("\u0085\3\2\2\2\u0084~\3\2\2\2\u0084\177\3\2\2\2\u0084")
        buf.write("\u0080\3\2\2\2\u0084\u0081\3\2\2\2\u0085\37\3\2\2\2\u0086")
        buf.write("\u0087\7\5\2\2\u0087\u0088\5\36\20\2\u0088\u0089\7\6\2")
        buf.write("\2\u0089!\3\2\2\2\u008a\u008b\7\t\2\2\u008b\u008c\5 \21")
        buf.write("\2\u008c#\3\2\2\2\u008d\u008e\b\23\1\2\u008e\u008f\5\"")
        buf.write("\22\2\u008f\u0090\7\7\2\2\u0090\u0098\3\2\2\2\u0091\u0092")
        buf.write("\5 \21\2\u0092\u0093\7\7\2\2\u0093\u0098\3\2\2\2\u0094")
        buf.write("\u0095\5\62\32\2\u0095\u0096\7\7\2\2\u0096\u0098\3\2\2")
        buf.write("\2\u0097\u008d\3\2\2\2\u0097\u0091\3\2\2\2\u0097\u0094")
        buf.write("\3\2\2\2\u0098\u009d\3\2\2\2\u0099\u009a\f\6\2\2\u009a")
        buf.write("\u009c\7\7\2\2\u009b\u0099\3\2\2\2\u009c\u009f\3\2\2\2")
        buf.write("\u009d\u009b\3\2\2\2\u009d\u009e\3\2\2\2\u009e%\3\2\2")
        buf.write("\2\u009f\u009d\3\2\2\2\u00a0\u00a1\b\24\1\2\u00a1\u00a2")
        buf.write("\5(\25\2\u00a2\u00a3\7\t\2\2\u00a3\u00a4\5(\25\2\u00a4")
        buf.write("\u00aa\3\2\2\2\u00a5\u00a6\f\4\2\2\u00a6\u00a7\7\t\2\2")
        buf.write("\u00a7\u00a9\5(\25\2\u00a8\u00a5\3\2\2\2\u00a9\u00ac\3")
        buf.write("\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\'")
        buf.write("\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ad\u00b2\5$\23\2\u00ae")
        buf.write("\u00b2\5\62\32\2\u00af\u00b2\5\"\22\2\u00b0\u00b2\5 \21")
        buf.write("\2\u00b1\u00ad\3\2\2\2\u00b1\u00ae\3\2\2\2\u00b1\u00af")
        buf.write("\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2)\3\2\2\2\u00b3\u00b5")
        buf.write("\5,\27\2\u00b4\u00b3\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5")
        buf.write("\u00ba\3\2\2\2\u00b6\u00b7\5.\30\2\u00b7\u00b8\7\4\2\2")
        buf.write("\u00b8\u00b9\5\60\31\2\u00b9\u00bb\3\2\2\2\u00ba\u00b6")
        buf.write("\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc")
        buf.write("\u00bd\3\2\2\2\u00bd+\3\2\2\2\u00be\u00c4\5$\23\2\u00bf")
        buf.write("\u00c4\5&\24\2\u00c0\u00c4\5\62\32\2\u00c1\u00c4\5\"\22")
        buf.write("\2\u00c2\u00c4\5 \21\2\u00c3\u00be\3\2\2\2\u00c3\u00bf")
        buf.write("\3\2\2\2\u00c3\u00c0\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3")
        buf.write("\u00c2\3\2\2\2\u00c4-\3\2\2\2\u00c5\u00c6\7\7\2\2\u00c6")
        buf.write("/\3\2\2\2\u00c7\u00cd\5$\23\2\u00c8\u00cd\5&\24\2\u00c9")
        buf.write("\u00cd\5\62\32\2\u00ca\u00cd\5\"\22\2\u00cb\u00cd\5 \21")
        buf.write("\2\u00cc\u00c7\3\2\2\2\u00cc\u00c8\3\2\2\2\u00cc\u00c9")
        buf.write("\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cb\3\2\2\2\u00cd")
        buf.write("\61\3\2\2\2\u00ce\u00d2\5\64\33\2\u00cf\u00d2\7\7\2\2")
        buf.write("\u00d0\u00d2\7\b\2\2\u00d1\u00ce\3\2\2\2\u00d1\u00cf\3")
        buf.write("\2\2\2\u00d1\u00d0\3\2\2\2\u00d2\63\3\2\2\2\u00d3\u00d4")
        buf.write("\7\t\2\2\u00d4\u00d8\7\7\2\2\u00d5\u00d6\7\t\2\2\u00d6")
        buf.write("\u00d8\7\b\2\2\u00d7\u00d3\3\2\2\2\u00d7\u00d5\3\2\2\2")
        buf.write("\u00d8\65\3\2\2\2\278:?CIQZgnv\u0084\u0097\u009d\u00aa")
        buf.write("\u00b1\u00b4\u00bc\u00c3\u00cc\u00d1\u00d7")
        return buf.getvalue()


class TaleParser ( Parser ):

    grammarFileName = "Tale.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "':'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IDENTIFIER", "NUMBER", "OPERATOR", "WS", 
                      "NEWLINE", "INDENT", "DEDENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_simpleAssignment = 3
    RULE_compoundAssignment = 4
    RULE_assignmentForm = 5
    RULE_unaryForm = 6
    RULE_unaryOperatorForm = 7
    RULE_binaryForm = 8
    RULE_keywordForm = 9
    RULE_simpleForm = 10
    RULE_argument = 11
    RULE_argumentName = 12
    RULE_argumentType = 13
    RULE_expression = 14
    RULE_expressionInBrackets = 15
    RULE_expressionInBracketsWithOperator = 16
    RULE_unary = 17
    RULE_binary = 18
    RULE_binaryOperand = 19
    RULE_keyword = 20
    RULE_keywordPrefix = 21
    RULE_keywordName = 22
    RULE_keywordValue = 23
    RULE_primitive = 24
    RULE_primitiveWithOperator = 25

    ruleNames =  [ "program", "statement", "assignment", "simpleAssignment", 
                   "compoundAssignment", "assignmentForm", "unaryForm", 
                   "unaryOperatorForm", "binaryForm", "keywordForm", "simpleForm", 
                   "argument", "argumentName", "argumentType", "expression", 
                   "expressionInBrackets", "expressionInBracketsWithOperator", 
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
    INDENT=10
    DEDENT=11

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
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TaleParser.T__2) | (1 << TaleParser.IDENTIFIER) | (1 << TaleParser.NUMBER) | (1 << TaleParser.OPERATOR) | (1 << TaleParser.NEWLINE))) != 0):
                self.state = 54
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [TaleParser.NEWLINE]:
                    self.state = 52
                    self.match(TaleParser.NEWLINE)
                    pass
                elif token in [TaleParser.T__2, TaleParser.IDENTIFIER, TaleParser.NUMBER, TaleParser.OPERATOR]:
                    self.state = 53
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 58
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
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
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

        def simpleAssignment(self):
            return self.getTypedRuleContext(TaleParser.SimpleAssignmentContext,0)


        def compoundAssignment(self):
            return self.getTypedRuleContext(TaleParser.CompoundAssignmentContext,0)


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
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.simpleAssignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.compoundAssignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleAssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentForm(self):
            return self.getTypedRuleContext(TaleParser.AssignmentFormContext,0)


        def expression(self):
            return self.getTypedRuleContext(TaleParser.ExpressionContext,0)


        def expressionInBrackets(self):
            return self.getTypedRuleContext(TaleParser.ExpressionInBracketsContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_simpleAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleAssignment" ):
                listener.enterSimpleAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleAssignment" ):
                listener.exitSimpleAssignment(self)




    def simpleAssignment(self):

        localctx = TaleParser.SimpleAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_simpleAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.assignmentForm()
            self.state = 68
            self.match(TaleParser.T__0)
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 69
                self.expression()
                pass

            elif la_ == 2:
                self.state = 70
                self.expressionInBrackets()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundAssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentForm(self):
            return self.getTypedRuleContext(TaleParser.AssignmentFormContext,0)


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
            return TaleParser.RULE_compoundAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundAssignment" ):
                listener.enterCompoundAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundAssignment" ):
                listener.exitCompoundAssignment(self)




    def compoundAssignment(self):

        localctx = TaleParser.CompoundAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_compoundAssignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.assignmentForm()
            self.state = 74
            self.match(TaleParser.T__0)
            self.state = 75
            self.match(TaleParser.INDENT)
            self.state = 77 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 76
                self.statement()
                self.state = 79 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TaleParser.T__2) | (1 << TaleParser.IDENTIFIER) | (1 << TaleParser.NUMBER) | (1 << TaleParser.OPERATOR))) != 0)):
                    break

            self.state = 81
            self.match(TaleParser.DEDENT)
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
        self.enterRule(localctx, 10, self.RULE_assignmentForm)
        try:
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.unaryForm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.unaryOperatorForm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.binaryForm()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.keywordForm()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 87
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
        self.enterRule(localctx, 12, self.RULE_unaryForm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.argument()
            self.state = 91
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
        self.enterRule(localctx, 14, self.RULE_unaryOperatorForm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(TaleParser.OPERATOR)
            self.state = 94
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
        self.enterRule(localctx, 16, self.RULE_binaryForm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.argument()
            self.state = 97
            self.match(TaleParser.OPERATOR)
            self.state = 98
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
        self.enterRule(localctx, 18, self.RULE_keywordForm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TaleParser.T__2:
                self.state = 100
                self.argument()


            self.state = 106 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 103
                self.match(TaleParser.IDENTIFIER)
                self.state = 104
                self.match(TaleParser.T__1)
                self.state = 105
                self.argument()
                self.state = 108 
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
        self.enterRule(localctx, 20, self.RULE_simpleForm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(TaleParser.IDENTIFIER)
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
        self.enterRule(localctx, 22, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(TaleParser.T__2)
            self.state = 113
            self.argumentName()
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TaleParser.T__1:
                self.state = 114
                self.match(TaleParser.T__1)
                self.state = 115
                self.argumentType()


            self.state = 118
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
        self.enterRule(localctx, 24, self.RULE_argumentName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
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
        self.enterRule(localctx, 26, self.RULE_argumentType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
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
        self.enterRule(localctx, 28, self.RULE_expression)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.unary(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.binary(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.keyword()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.primitive()
                self.state = 128
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
        self.enterRule(localctx, 30, self.RULE_expressionInBrackets)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(TaleParser.T__2)
            self.state = 133
            self.expression()
            self.state = 134
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
        self.enterRule(localctx, 32, self.RULE_expressionInBracketsWithOperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(TaleParser.OPERATOR)
            self.state = 137
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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_unary, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 140
                self.expressionInBracketsWithOperator()
                self.state = 141
                self.match(TaleParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 143
                self.expressionInBrackets()
                self.state = 144
                self.match(TaleParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.state = 146
                self.primitive()
                self.state = 147
                self.match(TaleParser.IDENTIFIER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 155
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TaleParser.UnaryContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_unary)
                    self.state = 151
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 152
                    self.match(TaleParser.IDENTIFIER) 
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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_binary, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.binaryOperand()
            self.state = 160
            self.match(TaleParser.OPERATOR)
            self.state = 161
            self.binaryOperand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 168
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TaleParser.BinaryContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_binary)
                    self.state = 163
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 164
                    self.match(TaleParser.OPERATOR)
                    self.state = 165
                    self.binaryOperand() 
                self.state = 170
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        self.enterRule(localctx, 38, self.RULE_binaryOperand)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.unary(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.primitive()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 173
                self.expressionInBracketsWithOperator()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 174
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
        self.enterRule(localctx, 40, self.RULE_keyword)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 177
                self.keywordPrefix()


            self.state = 184 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 180
                    self.keywordName()
                    self.state = 181
                    self.match(TaleParser.T__1)
                    self.state = 182
                    self.keywordValue()

                else:
                    raise NoViableAltException(self)
                self.state = 186 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        self.enterRule(localctx, 42, self.RULE_keywordPrefix)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.unary(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.binary(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                self.primitive()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 191
                self.expressionInBracketsWithOperator()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 192
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
        self.enterRule(localctx, 44, self.RULE_keywordName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
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
        self.enterRule(localctx, 46, self.RULE_keywordValue)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.unary(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.binary(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 199
                self.primitive()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 200
                self.expressionInBracketsWithOperator()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 201
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
        self.enterRule(localctx, 48, self.RULE_primitive)
        try:
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.OPERATOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.primitiveWithOperator()
                pass
            elif token in [TaleParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.match(TaleParser.IDENTIFIER)
                pass
            elif token in [TaleParser.NUMBER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 206
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
        self.enterRule(localctx, 50, self.RULE_primitiveWithOperator)
        try:
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.match(TaleParser.OPERATOR)
                self.state = 210
                self.match(TaleParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.match(TaleParser.OPERATOR)
                self.state = 212
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
        self._predicates[17] = self.unary_sempred
        self._predicates[18] = self.binary_sempred
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
         




