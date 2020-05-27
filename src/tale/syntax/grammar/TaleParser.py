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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("\u00e1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\3\2\3\2\7\2?\n\2\f\2\16\2B\13\2\3\2\3\2\3\3\3\3\5\3H")
        buf.write("\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5R\n\5\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\b\5\b\\\n\b\3\b\3\b\3\b\6\ba\n")
        buf.write("\b\r\b\16\bb\3\t\3\t\3\n\3\n\3\n\7\nj\n\n\f\n\16\nm\13")
        buf.write("\n\3\13\3\13\5\13q\n\13\3\f\3\f\3\f\3\f\5\fw\n\f\3\f\3")
        buf.write("\f\3\r\3\r\5\r}\n\r\3\16\3\16\3\17\3\17\3\20\3\20\5\20")
        buf.write("\u0085\n\20\3\21\3\21\3\22\3\22\6\22\u008b\n\22\r\22\16")
        buf.write("\22\u008c\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\5\23\u009d\n\23\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\7\24\u00a5\n\24\f\24\16\24\u00a8\13")
        buf.write("\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u00b2")
        buf.write("\n\25\f\25\16\25\u00b5\13\25\3\26\3\26\5\26\u00b9\n\26")
        buf.write("\3\27\5\27\u00bc\n\27\3\27\3\27\3\27\3\27\6\27\u00c2\n")
        buf.write("\27\r\27\16\27\u00c3\3\30\3\30\3\30\5\30\u00c9\n\30\3")
        buf.write("\31\3\31\3\32\3\32\3\32\7\32\u00d0\n\32\f\32\16\32\u00d3")
        buf.write("\13\32\3\33\3\33\5\33\u00d7\n\33\3\34\3\34\5\34\u00db")
        buf.write("\n\34\3\35\3\35\3\36\3\36\3\36\3\u00d1\4&(\37\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":\2\2\2\u00de\2@\3\2\2\2\4G\3\2\2\2\6I\3\2\2\2\bQ\3\2")
        buf.write("\2\2\nS\3\2\2\2\fV\3\2\2\2\16[\3\2\2\2\20d\3\2\2\2\22")
        buf.write("f\3\2\2\2\24p\3\2\2\2\26r\3\2\2\2\30|\3\2\2\2\32~\3\2")
        buf.write("\2\2\34\u0080\3\2\2\2\36\u0084\3\2\2\2 \u0086\3\2\2\2")
        buf.write("\"\u0088\3\2\2\2$\u009c\3\2\2\2&\u009e\3\2\2\2(\u00a9")
        buf.write("\3\2\2\2*\u00b8\3\2\2\2,\u00bb\3\2\2\2.\u00c8\3\2\2\2")
        buf.write("\60\u00ca\3\2\2\2\62\u00cc\3\2\2\2\64\u00d6\3\2\2\2\66")
        buf.write("\u00da\3\2\2\28\u00dc\3\2\2\2:\u00de\3\2\2\2<?\7\r\2\2")
        buf.write("=?\5\4\3\2><\3\2\2\2>=\3\2\2\2?B\3\2\2\2@>\3\2\2\2@A\3")
        buf.write("\2\2\2AC\3\2\2\2B@\3\2\2\2CD\7\2\2\3D\3\3\2\2\2EH\5\6")
        buf.write("\4\2FH\5$\23\2GE\3\2\2\2GF\3\2\2\2H\5\3\2\2\2IJ\5\b\5")
        buf.write("\2JK\7\3\2\2KL\5\36\20\2L\7\3\2\2\2MR\5\n\6\2NR\5\f\7")
        buf.write("\2OR\5\16\b\2PR\5\20\t\2QM\3\2\2\2QN\3\2\2\2QO\3\2\2\2")
        buf.write("QP\3\2\2\2R\t\3\2\2\2ST\5\22\n\2TU\7\b\2\2U\13\3\2\2\2")
        buf.write("VW\5\22\n\2WX\7\n\2\2XY\5\22\n\2Y\r\3\2\2\2Z\\\5\22\n")
        buf.write("\2[Z\3\2\2\2[\\\3\2\2\2\\`\3\2\2\2]^\7\b\2\2^_\7\4\2\2")
        buf.write("_a\5\22\n\2`]\3\2\2\2ab\3\2\2\2b`\3\2\2\2bc\3\2\2\2c\17")
        buf.write("\3\2\2\2de\7\b\2\2e\21\3\2\2\2fk\5\24\13\2gh\7\5\2\2h")
        buf.write("j\5\24\13\2ig\3\2\2\2jm\3\2\2\2ki\3\2\2\2kl\3\2\2\2l\23")
        buf.write("\3\2\2\2mk\3\2\2\2nq\5\26\f\2oq\5\30\r\2pn\3\2\2\2po\3")
        buf.write("\2\2\2q\25\3\2\2\2rs\7\6\2\2sv\5\32\16\2tu\7\4\2\2uw\5")
        buf.write("\34\17\2vt\3\2\2\2vw\3\2\2\2wx\3\2\2\2xy\7\7\2\2y\27\3")
        buf.write("\2\2\2z}\7\b\2\2{}\5\66\34\2|z\3\2\2\2|{\3\2\2\2}\31\3")
        buf.write("\2\2\2~\177\7\b\2\2\177\33\3\2\2\2\u0080\u0081\7\b\2\2")
        buf.write("\u0081\35\3\2\2\2\u0082\u0085\5 \21\2\u0083\u0085\5\"")
        buf.write("\22\2\u0084\u0082\3\2\2\2\u0084\u0083\3\2\2\2\u0085\37")
        buf.write("\3\2\2\2\u0086\u0087\5$\23\2\u0087!\3\2\2\2\u0088\u008a")
        buf.write("\7\17\2\2\u0089\u008b\5\4\3\2\u008a\u0089\3\2\2\2\u008b")
        buf.write("\u008c\3\2\2\2\u008c\u008a\3\2\2\2\u008c\u008d\3\2\2\2")
        buf.write("\u008d\u008e\3\2\2\2\u008e\u008f\7\20\2\2\u008f#\3\2\2")
        buf.write("\2\u0090\u0091\5&\24\2\u0091\u0092\7\r\2\2\u0092\u009d")
        buf.write("\3\2\2\2\u0093\u0094\5(\25\2\u0094\u0095\7\r\2\2\u0095")
        buf.write("\u009d\3\2\2\2\u0096\u0097\5,\27\2\u0097\u0098\7\r\2\2")
        buf.write("\u0098\u009d\3\2\2\2\u0099\u009a\5\62\32\2\u009a\u009b")
        buf.write("\7\r\2\2\u009b\u009d\3\2\2\2\u009c\u0090\3\2\2\2\u009c")
        buf.write("\u0093\3\2\2\2\u009c\u0096\3\2\2\2\u009c\u0099\3\2\2\2")
        buf.write("\u009d%\3\2\2\2\u009e\u009f\b\24\1\2\u009f\u00a0\5\62")
        buf.write("\32\2\u00a0\u00a1\7\b\2\2\u00a1\u00a6\3\2\2\2\u00a2\u00a3")
        buf.write("\f\4\2\2\u00a3\u00a5\7\b\2\2\u00a4\u00a2\3\2\2\2\u00a5")
        buf.write("\u00a8\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2")
        buf.write("\u00a7\'\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a9\u00aa\b\25")
        buf.write("\1\2\u00aa\u00ab\5*\26\2\u00ab\u00ac\7\n\2\2\u00ac\u00ad")
        buf.write("\5*\26\2\u00ad\u00b3\3\2\2\2\u00ae\u00af\f\4\2\2\u00af")
        buf.write("\u00b0\7\n\2\2\u00b0\u00b2\5*\26\2\u00b1\u00ae\3\2\2\2")
        buf.write("\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3")
        buf.write("\2\2\2\u00b4)\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b9")
        buf.write("\5&\24\2\u00b7\u00b9\5\62\32\2\u00b8\u00b6\3\2\2\2\u00b8")
        buf.write("\u00b7\3\2\2\2\u00b9+\3\2\2\2\u00ba\u00bc\5.\30\2\u00bb")
        buf.write("\u00ba\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00c1\3\2\2\2")
        buf.write("\u00bd\u00be\5\60\31\2\u00be\u00bf\7\4\2\2\u00bf\u00c0")
        buf.write("\5.\30\2\u00c0\u00c2\3\2\2\2\u00c1\u00bd\3\2\2\2\u00c2")
        buf.write("\u00c3\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2")
        buf.write("\u00c4-\3\2\2\2\u00c5\u00c9\5&\24\2\u00c6\u00c9\5(\25")
        buf.write("\2\u00c7\u00c9\5\62\32\2\u00c8\u00c5\3\2\2\2\u00c8\u00c6")
        buf.write("\3\2\2\2\u00c8\u00c7\3\2\2\2\u00c9/\3\2\2\2\u00ca\u00cb")
        buf.write("\7\b\2\2\u00cb\61\3\2\2\2\u00cc\u00d1\5\64\33\2\u00cd")
        buf.write("\u00ce\7\5\2\2\u00ce\u00d0\5\64\33\2\u00cf\u00cd\3\2\2")
        buf.write("\2\u00d0\u00d3\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d1\u00cf")
        buf.write("\3\2\2\2\u00d2\63\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d4\u00d7")
        buf.write("\7\b\2\2\u00d5\u00d7\5\66\34\2\u00d6\u00d4\3\2\2\2\u00d6")
        buf.write("\u00d5\3\2\2\2\u00d7\65\3\2\2\2\u00d8\u00db\58\35\2\u00d9")
        buf.write("\u00db\5:\36\2\u00da\u00d8\3\2\2\2\u00da\u00d9\3\2\2\2")
        buf.write("\u00db\67\3\2\2\2\u00dc\u00dd\7\t\2\2\u00dd9\3\2\2\2\u00de")
        buf.write("\u00df\7\13\2\2\u00df;\3\2\2\2\30>@GQ[bkpv|\u0084\u008c")
        buf.write("\u009c\u00a6\u00b3\u00b8\u00bb\u00c3\u00c8\u00d1\u00d6")
        buf.write("\u00da")
        return buf.getvalue()


class TaleParser ( Parser ):

    grammarFileName = "Tale.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "':'", "','", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IDENTIFIER", "NUMBER", 
                      "OPERATOR", "STRING", "WS", "NEWLINE", "SKIP_", "INDENT", 
                      "DEDENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_form = 3
    RULE_unaryForm = 4
    RULE_binaryForm = 5
    RULE_keywordForm = 6
    RULE_primitiveForm = 7
    RULE_parameters = 8
    RULE_parameter = 9
    RULE_simpleParameter = 10
    RULE_patternMatchingParameter = 11
    RULE_parameterName = 12
    RULE_parameterType = 13
    RULE_assignmentBody = 14
    RULE_simpleAssignmentBody = 15
    RULE_compoundAssignmentBody = 16
    RULE_expression = 17
    RULE_unary = 18
    RULE_binary = 19
    RULE_binaryOperand = 20
    RULE_keyword = 21
    RULE_keywordArgument = 22
    RULE_keywordName = 23
    RULE_primitive = 24
    RULE_primitiveItem = 25
    RULE_literal = 26
    RULE_intLiteral = 27
    RULE_stringLiteral = 28

    ruleNames =  [ "program", "statement", "assignment", "form", "unaryForm", 
                   "binaryForm", "keywordForm", "primitiveForm", "parameters", 
                   "parameter", "simpleParameter", "patternMatchingParameter", 
                   "parameterName", "parameterType", "assignmentBody", "simpleAssignmentBody", 
                   "compoundAssignmentBody", "expression", "unary", "binary", 
                   "binaryOperand", "keyword", "keywordArgument", "keywordName", 
                   "primitive", "primitiveItem", "literal", "intLiteral", 
                   "stringLiteral" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    IDENTIFIER=6
    NUMBER=7
    OPERATOR=8
    STRING=9
    WS=10
    NEWLINE=11
    SKIP_=12
    INDENT=13
    DEDENT=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TaleParser.EOF, 0)

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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TaleParser.T__3) | (1 << TaleParser.IDENTIFIER) | (1 << TaleParser.NUMBER) | (1 << TaleParser.STRING) | (1 << TaleParser.NEWLINE))) != 0):
                self.state = 60
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [TaleParser.NEWLINE]:
                    self.state = 58
                    self.match(TaleParser.NEWLINE)
                    pass
                elif token in [TaleParser.T__3, TaleParser.IDENTIFIER, TaleParser.NUMBER, TaleParser.STRING]:
                    self.state = 59
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
            self.match(TaleParser.EOF)
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
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
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

        def form(self):
            return self.getTypedRuleContext(TaleParser.FormContext,0)


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
            self.state = 71
            self.form()
            self.state = 72
            self.match(TaleParser.T__0)
            self.state = 73
            self.assignmentBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryForm(self):
            return self.getTypedRuleContext(TaleParser.UnaryFormContext,0)


        def binaryForm(self):
            return self.getTypedRuleContext(TaleParser.BinaryFormContext,0)


        def keywordForm(self):
            return self.getTypedRuleContext(TaleParser.KeywordFormContext,0)


        def primitiveForm(self):
            return self.getTypedRuleContext(TaleParser.PrimitiveFormContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_form

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForm" ):
                listener.enterForm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForm" ):
                listener.exitForm(self)




    def form(self):

        localctx = TaleParser.FormContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_form)
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.unaryForm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.binaryForm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                self.keywordForm()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 78
                self.primitiveForm()
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

        def parameters(self):
            return self.getTypedRuleContext(TaleParser.ParametersContext,0)


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
            self.state = 81
            self.parameters()
            self.state = 82
            self.match(TaleParser.IDENTIFIER)
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

        def parameters(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TaleParser.ParametersContext)
            else:
                return self.getTypedRuleContext(TaleParser.ParametersContext,i)


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
        self.enterRule(localctx, 10, self.RULE_binaryForm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.parameters()
            self.state = 85
            self.match(TaleParser.OPERATOR)
            self.state = 86
            self.parameters()
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

        def parameters(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TaleParser.ParametersContext)
            else:
                return self.getTypedRuleContext(TaleParser.ParametersContext,i)


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
        self.enterRule(localctx, 12, self.RULE_keywordForm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 88
                self.parameters()


            self.state = 94 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 91
                self.match(TaleParser.IDENTIFIER)
                self.state = 92
                self.match(TaleParser.T__1)
                self.state = 93
                self.parameters()
                self.state = 96 
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


    class PrimitiveFormContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TaleParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return TaleParser.RULE_primitiveForm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveForm" ):
                listener.enterPrimitiveForm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveForm" ):
                listener.exitPrimitiveForm(self)




    def primitiveForm(self):

        localctx = TaleParser.PrimitiveFormContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_primitiveForm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(TaleParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TaleParser.ParameterContext)
            else:
                return self.getTypedRuleContext(TaleParser.ParameterContext,i)


        def getRuleIndex(self):
            return TaleParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = TaleParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.parameter()
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TaleParser.T__2:
                self.state = 101
                self.match(TaleParser.T__2)
                self.state = 102
                self.parameter()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.simpleParameter()
                pass
            elif token in [TaleParser.IDENTIFIER, TaleParser.NUMBER, TaleParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
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
            self.state = 112
            self.match(TaleParser.T__3)
            self.state = 113
            self.parameterName()
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TaleParser.T__1:
                self.state = 114
                self.match(TaleParser.T__1)
                self.state = 115
                self.parameterType()


            self.state = 118
            self.match(TaleParser.T__4)
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

        def literal(self):
            return self.getTypedRuleContext(TaleParser.LiteralContext,0)


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
        try:
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.match(TaleParser.IDENTIFIER)
                pass
            elif token in [TaleParser.NUMBER, TaleParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.literal()
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
            self.state = 124
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
            self.state = 126
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
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.IDENTIFIER, TaleParser.NUMBER, TaleParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.simpleAssignmentBody()
                pass
            elif token in [TaleParser.INDENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
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
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.expression()
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
            self.state = 134
            self.match(TaleParser.INDENT)
            self.state = 136 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 135
                self.statement()
                self.state = 138 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TaleParser.T__3) | (1 << TaleParser.IDENTIFIER) | (1 << TaleParser.NUMBER) | (1 << TaleParser.STRING))) != 0)):
                    break

            self.state = 140
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


        def NEWLINE(self):
            return self.getToken(TaleParser.NEWLINE, 0)

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
        self.enterRule(localctx, 34, self.RULE_expression)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.unary(0)
                self.state = 143
                self.match(TaleParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.binary(0)
                self.state = 146
                self.match(TaleParser.NEWLINE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self.keyword()
                self.state = 149
                self.match(TaleParser.NEWLINE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 151
                self.primitive()
                self.state = 152
                self.match(TaleParser.NEWLINE)
                pass


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

        def primitive(self):
            return self.getTypedRuleContext(TaleParser.PrimitiveContext,0)


        def IDENTIFIER(self):
            return self.getToken(TaleParser.IDENTIFIER, 0)

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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_unary, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.primitive()
            self.state = 158
            self.match(TaleParser.IDENTIFIER)
            self._ctx.stop = self._input.LT(-1)
            self.state = 164
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TaleParser.UnaryContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_unary)
                    self.state = 160
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 161
                    self.match(TaleParser.IDENTIFIER) 
                self.state = 166
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
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_binary, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.binaryOperand()
            self.state = 169
            self.match(TaleParser.OPERATOR)
            self.state = 170
            self.binaryOperand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 177
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TaleParser.BinaryContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_binary)
                    self.state = 172
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 173
                    self.match(TaleParser.OPERATOR)
                    self.state = 174
                    self.binaryOperand() 
                self.state = 179
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
        self.enterRule(localctx, 40, self.RULE_binaryOperand)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.unary(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.primitive()
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

        def keywordArgument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TaleParser.KeywordArgumentContext)
            else:
                return self.getTypedRuleContext(TaleParser.KeywordArgumentContext,i)


        def keywordName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TaleParser.KeywordNameContext)
            else:
                return self.getTypedRuleContext(TaleParser.KeywordNameContext,i)


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
        self.enterRule(localctx, 42, self.RULE_keyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 184
                self.keywordArgument()


            self.state = 191 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 187
                self.keywordName()
                self.state = 188
                self.match(TaleParser.T__1)
                self.state = 189
                self.keywordArgument()
                self.state = 193 
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


    class KeywordArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(TaleParser.UnaryContext,0)


        def binary(self):
            return self.getTypedRuleContext(TaleParser.BinaryContext,0)


        def primitive(self):
            return self.getTypedRuleContext(TaleParser.PrimitiveContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_keywordArgument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeywordArgument" ):
                listener.enterKeywordArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeywordArgument" ):
                listener.exitKeywordArgument(self)




    def keywordArgument(self):

        localctx = TaleParser.KeywordArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_keywordArgument)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.unary(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.binary(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 197
                self.primitive()
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
        self.enterRule(localctx, 46, self.RULE_keywordName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(TaleParser.IDENTIFIER)
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

        def primitiveItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TaleParser.PrimitiveItemContext)
            else:
                return self.getTypedRuleContext(TaleParser.PrimitiveItemContext,i)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.primitiveItem()
            self.state = 207
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 203
                    self.match(TaleParser.T__2)
                    self.state = 204
                    self.primitiveItem() 
                self.state = 209
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TaleParser.IDENTIFIER, 0)

        def literal(self):
            return self.getTypedRuleContext(TaleParser.LiteralContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_primitiveItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveItem" ):
                listener.enterPrimitiveItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveItem" ):
                listener.exitPrimitiveItem(self)




    def primitiveItem(self):

        localctx = TaleParser.PrimitiveItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_primitiveItem)
        try:
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.match(TaleParser.IDENTIFIER)
                pass
            elif token in [TaleParser.NUMBER, TaleParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.literal()
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


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def intLiteral(self):
            return self.getTypedRuleContext(TaleParser.IntLiteralContext,0)


        def stringLiteral(self):
            return self.getTypedRuleContext(TaleParser.StringLiteralContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = TaleParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_literal)
        try:
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.intLiteral()
                pass
            elif token in [TaleParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.stringLiteral()
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


    class IntLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(TaleParser.NUMBER, 0)

        def getRuleIndex(self):
            return TaleParser.RULE_intLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntLiteral" ):
                listener.enterIntLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntLiteral" ):
                listener.exitIntLiteral(self)




    def intLiteral(self):

        localctx = TaleParser.IntLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_intLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(TaleParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TaleParser.STRING, 0)

        def getRuleIndex(self):
            return TaleParser.RULE_stringLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)




    def stringLiteral(self):

        localctx = TaleParser.StringLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_stringLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(TaleParser.STRING)
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
        self._predicates[18] = self.unary_sempred
        self._predicates[19] = self.binary_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def unary_sempred(self, localctx:UnaryContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def binary_sempred(self, localctx:BinaryContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




