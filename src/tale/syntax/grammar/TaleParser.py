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
        buf.write("\u00f1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\3\2\3\2\7\2E\n\2\f\2\16\2H\13\2")
        buf.write("\3\2\3\2\3\3\3\3\5\3N\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\5\5Y\n\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\t\5\tf\n\t\3\t\3\t\3\t\6\tk\n\t\r\t\16\tl\3\n\3")
        buf.write("\n\3\13\3\13\5\13s\n\13\3\f\3\f\3\f\6\fx\n\f\r\f\16\f")
        buf.write("y\3\r\3\r\5\r~\n\r\3\16\3\16\3\16\3\16\5\16\u0084\n\16")
        buf.write("\3\16\3\16\3\17\3\17\5\17\u008a\n\17\3\20\3\20\3\21\3")
        buf.write("\21\3\22\3\22\5\22\u0092\n\22\3\23\3\23\3\24\3\24\3\24")
        buf.write("\6\24\u0099\n\24\r\24\16\24\u009a\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\5\25\u00a4\n\25\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\7\26\u00ac\n\26\f\26\16\26\u00af\13\26\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\5\27\u00b8\n\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u00c2\n\30\f\30\16")
        buf.write("\30\u00c5\13\30\3\31\3\31\5\31\u00c9\n\31\3\32\5\32\u00cc")
        buf.write("\n\32\3\32\3\32\3\32\3\32\6\32\u00d2\n\32\r\32\16\32\u00d3")
        buf.write("\3\33\3\33\3\33\5\33\u00d9\n\33\3\34\3\34\3\35\3\35\3")
        buf.write("\35\7\35\u00e0\n\35\f\35\16\35\u00e3\13\35\3\36\3\36\5")
        buf.write("\36\u00e7\n\36\3\37\3\37\5\37\u00eb\n\37\3 \3 \3!\3!\3")
        buf.write("!\3\u00e1\4*.\"\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@\2\2\2\u00f0\2F\3\2\2\2\4M\3")
        buf.write("\2\2\2\6O\3\2\2\2\bX\3\2\2\2\nZ\3\2\2\2\f]\3\2\2\2\16")
        buf.write("`\3\2\2\2\20e\3\2\2\2\22n\3\2\2\2\24r\3\2\2\2\26t\3\2")
        buf.write("\2\2\30}\3\2\2\2\32\177\3\2\2\2\34\u0089\3\2\2\2\36\u008b")
        buf.write("\3\2\2\2 \u008d\3\2\2\2\"\u0091\3\2\2\2$\u0093\3\2\2\2")
        buf.write("&\u0095\3\2\2\2(\u00a3\3\2\2\2*\u00a5\3\2\2\2,\u00b7\3")
        buf.write("\2\2\2.\u00b9\3\2\2\2\60\u00c8\3\2\2\2\62\u00cb\3\2\2")
        buf.write("\2\64\u00d8\3\2\2\2\66\u00da\3\2\2\28\u00dc\3\2\2\2:\u00e6")
        buf.write("\3\2\2\2<\u00ea\3\2\2\2>\u00ec\3\2\2\2@\u00ee\3\2\2\2")
        buf.write("BE\7\r\2\2CE\5\4\3\2DB\3\2\2\2DC\3\2\2\2EH\3\2\2\2FD\3")
        buf.write("\2\2\2FG\3\2\2\2GI\3\2\2\2HF\3\2\2\2IJ\7\2\2\3J\3\3\2")
        buf.write("\2\2KN\5\6\4\2LN\5(\25\2MK\3\2\2\2ML\3\2\2\2N\5\3\2\2")
        buf.write("\2OP\5\b\5\2PQ\7\3\2\2QR\5\"\22\2R\7\3\2\2\2SY\5\n\6\2")
        buf.write("TY\5\f\7\2UY\5\16\b\2VY\5\20\t\2WY\5\22\n\2XS\3\2\2\2")
        buf.write("XT\3\2\2\2XU\3\2\2\2XV\3\2\2\2XW\3\2\2\2Y\t\3\2\2\2Z[")
        buf.write("\5\24\13\2[\\\7\b\2\2\\\13\3\2\2\2]^\7\n\2\2^_\5\30\r")
        buf.write("\2_\r\3\2\2\2`a\5\24\13\2ab\7\n\2\2bc\5\24\13\2c\17\3")
        buf.write("\2\2\2df\5\24\13\2ed\3\2\2\2ef\3\2\2\2fj\3\2\2\2gh\7\b")
        buf.write("\2\2hi\7\4\2\2ik\5\24\13\2jg\3\2\2\2kl\3\2\2\2lj\3\2\2")
        buf.write("\2lm\3\2\2\2m\21\3\2\2\2no\7\b\2\2o\23\3\2\2\2ps\5\30")
        buf.write("\r\2qs\5\26\f\2rp\3\2\2\2rq\3\2\2\2s\25\3\2\2\2tw\5\30")
        buf.write("\r\2uv\7\5\2\2vx\5\30\r\2wu\3\2\2\2xy\3\2\2\2yw\3\2\2")
        buf.write("\2yz\3\2\2\2z\27\3\2\2\2{~\5\32\16\2|~\5\34\17\2}{\3\2")
        buf.write("\2\2}|\3\2\2\2~\31\3\2\2\2\177\u0080\7\6\2\2\u0080\u0083")
        buf.write("\5\36\20\2\u0081\u0082\7\4\2\2\u0082\u0084\5 \21\2\u0083")
        buf.write("\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0085\3\2\2\2")
        buf.write("\u0085\u0086\7\7\2\2\u0086\33\3\2\2\2\u0087\u008a\7\b")
        buf.write("\2\2\u0088\u008a\5<\37\2\u0089\u0087\3\2\2\2\u0089\u0088")
        buf.write("\3\2\2\2\u008a\35\3\2\2\2\u008b\u008c\7\b\2\2\u008c\37")
        buf.write("\3\2\2\2\u008d\u008e\7\b\2\2\u008e!\3\2\2\2\u008f\u0092")
        buf.write("\5$\23\2\u0090\u0092\5&\24\2\u0091\u008f\3\2\2\2\u0091")
        buf.write("\u0090\3\2\2\2\u0092#\3\2\2\2\u0093\u0094\5(\25\2\u0094")
        buf.write("%\3\2\2\2\u0095\u0098\7\17\2\2\u0096\u0099\7\r\2\2\u0097")
        buf.write("\u0099\5\4\3\2\u0098\u0096\3\2\2\2\u0098\u0097\3\2\2\2")
        buf.write("\u0099\u009a\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b\3")
        buf.write("\2\2\2\u009b\u009c\3\2\2\2\u009c\u009d\7\20\2\2\u009d")
        buf.write("\'\3\2\2\2\u009e\u00a4\5*\26\2\u009f\u00a4\5,\27\2\u00a0")
        buf.write("\u00a4\5.\30\2\u00a1\u00a4\5\62\32\2\u00a2\u00a4\58\35")
        buf.write("\2\u00a3\u009e\3\2\2\2\u00a3\u009f\3\2\2\2\u00a3\u00a0")
        buf.write("\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4")
        buf.write(")\3\2\2\2\u00a5\u00a6\b\26\1\2\u00a6\u00a7\58\35\2\u00a7")
        buf.write("\u00a8\7\b\2\2\u00a8\u00ad\3\2\2\2\u00a9\u00aa\f\4\2\2")
        buf.write("\u00aa\u00ac\7\b\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00af\3")
        buf.write("\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae+")
        buf.write("\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00b1\7\n\2\2\u00b1")
        buf.write("\u00b8\5:\36\2\u00b2\u00b3\7\n\2\2\u00b3\u00b4\7\6\2\2")
        buf.write("\u00b4\u00b5\5(\25\2\u00b5\u00b6\7\7\2\2\u00b6\u00b8\3")
        buf.write("\2\2\2\u00b7\u00b0\3\2\2\2\u00b7\u00b2\3\2\2\2\u00b8-")
        buf.write("\3\2\2\2\u00b9\u00ba\b\30\1\2\u00ba\u00bb\5\60\31\2\u00bb")
        buf.write("\u00bc\7\n\2\2\u00bc\u00bd\5\60\31\2\u00bd\u00c3\3\2\2")
        buf.write("\2\u00be\u00bf\f\4\2\2\u00bf\u00c0\7\n\2\2\u00c0\u00c2")
        buf.write("\5\60\31\2\u00c1\u00be\3\2\2\2\u00c2\u00c5\3\2\2\2\u00c3")
        buf.write("\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4/\3\2\2\2\u00c5")
        buf.write("\u00c3\3\2\2\2\u00c6\u00c9\5*\26\2\u00c7\u00c9\58\35\2")
        buf.write("\u00c8\u00c6\3\2\2\2\u00c8\u00c7\3\2\2\2\u00c9\61\3\2")
        buf.write("\2\2\u00ca\u00cc\5\64\33\2\u00cb\u00ca\3\2\2\2\u00cb\u00cc")
        buf.write("\3\2\2\2\u00cc\u00d1\3\2\2\2\u00cd\u00ce\5\66\34\2\u00ce")
        buf.write("\u00cf\7\4\2\2\u00cf\u00d0\5\64\33\2\u00d0\u00d2\3\2\2")
        buf.write("\2\u00d1\u00cd\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d1")
        buf.write("\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\63\3\2\2\2\u00d5\u00d9")
        buf.write("\5*\26\2\u00d6\u00d9\5.\30\2\u00d7\u00d9\58\35\2\u00d8")
        buf.write("\u00d5\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d7\3\2\2\2")
        buf.write("\u00d9\65\3\2\2\2\u00da\u00db\7\b\2\2\u00db\67\3\2\2\2")
        buf.write("\u00dc\u00e1\5:\36\2\u00dd\u00de\7\5\2\2\u00de\u00e0\5")
        buf.write(":\36\2\u00df\u00dd\3\2\2\2\u00e0\u00e3\3\2\2\2\u00e1\u00e2")
        buf.write("\3\2\2\2\u00e1\u00df\3\2\2\2\u00e29\3\2\2\2\u00e3\u00e1")
        buf.write("\3\2\2\2\u00e4\u00e7\7\b\2\2\u00e5\u00e7\5<\37\2\u00e6")
        buf.write("\u00e4\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7;\3\2\2\2\u00e8")
        buf.write("\u00eb\5> \2\u00e9\u00eb\5@!\2\u00ea\u00e8\3\2\2\2\u00ea")
        buf.write("\u00e9\3\2\2\2\u00eb=\3\2\2\2\u00ec\u00ed\7\t\2\2\u00ed")
        buf.write("?\3\2\2\2\u00ee\u00ef\7\13\2\2\u00efA\3\2\2\2\33DFMXe")
        buf.write("lry}\u0083\u0089\u0091\u0098\u009a\u00a3\u00ad\u00b7\u00c3")
        buf.write("\u00c8\u00cb\u00d3\u00d8\u00e1\u00e6\u00ea")
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
    RULE_prefixOperatorForm = 5
    RULE_binaryForm = 6
    RULE_keywordForm = 7
    RULE_primitiveForm = 8
    RULE_parameter = 9
    RULE_tupleParameter = 10
    RULE_singleParameter = 11
    RULE_simpleParameter = 12
    RULE_patternMatchingParameter = 13
    RULE_parameterName = 14
    RULE_parameterType = 15
    RULE_assignmentBody = 16
    RULE_simpleAssignmentBody = 17
    RULE_compoundAssignmentBody = 18
    RULE_expression = 19
    RULE_unary = 20
    RULE_prefixOperator = 21
    RULE_binary = 22
    RULE_binaryOperand = 23
    RULE_keyword = 24
    RULE_keywordArgument = 25
    RULE_keywordName = 26
    RULE_primitive = 27
    RULE_primitiveItem = 28
    RULE_literal = 29
    RULE_intLiteral = 30
    RULE_stringLiteral = 31

    ruleNames =  [ "program", "statement", "assignment", "form", "unaryForm", 
                   "prefixOperatorForm", "binaryForm", "keywordForm", "primitiveForm", 
                   "parameter", "tupleParameter", "singleParameter", "simpleParameter", 
                   "patternMatchingParameter", "parameterName", "parameterType", 
                   "assignmentBody", "simpleAssignmentBody", "compoundAssignmentBody", 
                   "expression", "unary", "prefixOperator", "binary", "binaryOperand", 
                   "keyword", "keywordArgument", "keywordName", "primitive", 
                   "primitiveItem", "literal", "intLiteral", "stringLiteral" ]

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
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TaleParser.T__3) | (1 << TaleParser.IDENTIFIER) | (1 << TaleParser.NUMBER) | (1 << TaleParser.OPERATOR) | (1 << TaleParser.STRING) | (1 << TaleParser.NEWLINE))) != 0):
                self.state = 66
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [TaleParser.NEWLINE]:
                    self.state = 64
                    self.match(TaleParser.NEWLINE)
                    pass
                elif token in [TaleParser.T__3, TaleParser.IDENTIFIER, TaleParser.NUMBER, TaleParser.OPERATOR, TaleParser.STRING]:
                    self.state = 65
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
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
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
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
            self.state = 77
            self.form()
            self.state = 78
            self.match(TaleParser.T__0)
            self.state = 79
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


        def prefixOperatorForm(self):
            return self.getTypedRuleContext(TaleParser.PrefixOperatorFormContext,0)


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
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.unaryForm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.prefixOperatorForm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.binaryForm()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 84
                self.keywordForm()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 85
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
            self.state = 88
            self.parameter()
            self.state = 89
            self.match(TaleParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrefixOperatorFormContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPERATOR(self):
            return self.getToken(TaleParser.OPERATOR, 0)

        def singleParameter(self):
            return self.getTypedRuleContext(TaleParser.SingleParameterContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_prefixOperatorForm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrefixOperatorForm" ):
                listener.enterPrefixOperatorForm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrefixOperatorForm" ):
                listener.exitPrefixOperatorForm(self)




    def prefixOperatorForm(self):

        localctx = TaleParser.PrefixOperatorFormContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_prefixOperatorForm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(TaleParser.OPERATOR)
            self.state = 92
            self.singleParameter()
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
            self.state = 94
            self.parameter()
            self.state = 95
            self.match(TaleParser.OPERATOR)
            self.state = 96
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
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 98
                self.parameter()


            self.state = 104 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 101
                self.match(TaleParser.IDENTIFIER)
                self.state = 102
                self.match(TaleParser.T__1)
                self.state = 103
                self.parameter()
                self.state = 106 
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
        self.enterRule(localctx, 16, self.RULE_primitiveForm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
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

        def singleParameter(self):
            return self.getTypedRuleContext(TaleParser.SingleParameterContext,0)


        def tupleParameter(self):
            return self.getTypedRuleContext(TaleParser.TupleParameterContext,0)


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
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.singleParameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.tupleParameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TupleParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TaleParser.SingleParameterContext)
            else:
                return self.getTypedRuleContext(TaleParser.SingleParameterContext,i)


        def getRuleIndex(self):
            return TaleParser.RULE_tupleParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTupleParameter" ):
                listener.enterTupleParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTupleParameter" ):
                listener.exitTupleParameter(self)




    def tupleParameter(self):

        localctx = TaleParser.TupleParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_tupleParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.singleParameter()
            self.state = 117 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 115
                self.match(TaleParser.T__2)
                self.state = 116
                self.singleParameter()
                self.state = 119 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==TaleParser.T__2):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleParameter(self):
            return self.getTypedRuleContext(TaleParser.SimpleParameterContext,0)


        def patternMatchingParameter(self):
            return self.getTypedRuleContext(TaleParser.PatternMatchingParameterContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_singleParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleParameter" ):
                listener.enterSingleParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleParameter" ):
                listener.exitSingleParameter(self)




    def singleParameter(self):

        localctx = TaleParser.SingleParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_singleParameter)
        try:
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.simpleParameter()
                pass
            elif token in [TaleParser.IDENTIFIER, TaleParser.NUMBER, TaleParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
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
        self.enterRule(localctx, 24, self.RULE_simpleParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(TaleParser.T__3)
            self.state = 126
            self.parameterName()
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TaleParser.T__1:
                self.state = 127
                self.match(TaleParser.T__1)
                self.state = 128
                self.parameterType()


            self.state = 131
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
        self.enterRule(localctx, 26, self.RULE_patternMatchingParameter)
        try:
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.match(TaleParser.IDENTIFIER)
                pass
            elif token in [TaleParser.NUMBER, TaleParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
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
        self.enterRule(localctx, 28, self.RULE_parameterName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
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
        self.enterRule(localctx, 30, self.RULE_parameterType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
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
        self.enterRule(localctx, 32, self.RULE_assignmentBody)
        try:
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.IDENTIFIER, TaleParser.NUMBER, TaleParser.OPERATOR, TaleParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.simpleAssignmentBody()
                pass
            elif token in [TaleParser.INDENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
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
        self.enterRule(localctx, 34, self.RULE_simpleAssignmentBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
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
            return TaleParser.RULE_compoundAssignmentBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundAssignmentBody" ):
                listener.enterCompoundAssignmentBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundAssignmentBody" ):
                listener.exitCompoundAssignmentBody(self)




    def compoundAssignmentBody(self):

        localctx = TaleParser.CompoundAssignmentBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_compoundAssignmentBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(TaleParser.INDENT)
            self.state = 150 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 150
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [TaleParser.NEWLINE]:
                    self.state = 148
                    self.match(TaleParser.NEWLINE)
                    pass
                elif token in [TaleParser.T__3, TaleParser.IDENTIFIER, TaleParser.NUMBER, TaleParser.OPERATOR, TaleParser.STRING]:
                    self.state = 149
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 152 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TaleParser.T__3) | (1 << TaleParser.IDENTIFIER) | (1 << TaleParser.NUMBER) | (1 << TaleParser.OPERATOR) | (1 << TaleParser.STRING) | (1 << TaleParser.NEWLINE))) != 0)):
                    break

            self.state = 154
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


        def prefixOperator(self):
            return self.getTypedRuleContext(TaleParser.PrefixOperatorContext,0)


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
        self.enterRule(localctx, 38, self.RULE_expression)
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.unary(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.prefixOperator()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 158
                self.binary(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 159
                self.keyword()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 160
                self.primitive()
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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_unary, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.primitive()
            self.state = 165
            self.match(TaleParser.IDENTIFIER)
            self._ctx.stop = self._input.LT(-1)
            self.state = 171
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TaleParser.UnaryContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_unary)
                    self.state = 167
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 168
                    self.match(TaleParser.IDENTIFIER) 
                self.state = 173
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrefixOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPERATOR(self):
            return self.getToken(TaleParser.OPERATOR, 0)

        def primitiveItem(self):
            return self.getTypedRuleContext(TaleParser.PrimitiveItemContext,0)


        def expression(self):
            return self.getTypedRuleContext(TaleParser.ExpressionContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_prefixOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrefixOperator" ):
                listener.enterPrefixOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrefixOperator" ):
                listener.exitPrefixOperator(self)




    def prefixOperator(self):

        localctx = TaleParser.PrefixOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_prefixOperator)
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(TaleParser.OPERATOR)
                self.state = 175
                self.primitiveItem()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.match(TaleParser.OPERATOR)
                self.state = 177
                self.match(TaleParser.T__3)
                self.state = 178
                self.expression()
                self.state = 179
                self.match(TaleParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_binary, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.binaryOperand()
            self.state = 185
            self.match(TaleParser.OPERATOR)
            self.state = 186
            self.binaryOperand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 193
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TaleParser.BinaryContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_binary)
                    self.state = 188
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 189
                    self.match(TaleParser.OPERATOR)
                    self.state = 190
                    self.binaryOperand() 
                self.state = 195
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        self.enterRule(localctx, 46, self.RULE_binaryOperand)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.unary(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
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
        self.enterRule(localctx, 48, self.RULE_keyword)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 200
                self.keywordArgument()


            self.state = 207 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 203
                    self.keywordName()
                    self.state = 204
                    self.match(TaleParser.T__1)
                    self.state = 205
                    self.keywordArgument()

                else:
                    raise NoViableAltException(self)
                self.state = 209 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
        self.enterRule(localctx, 50, self.RULE_keywordArgument)
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.unary(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.binary(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 213
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
        self.enterRule(localctx, 52, self.RULE_keywordName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
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
        self.enterRule(localctx, 54, self.RULE_primitive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.primitiveItem()
            self.state = 223
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 219
                    self.match(TaleParser.T__2)
                    self.state = 220
                    self.primitiveItem() 
                self.state = 225
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
        self.enterRule(localctx, 56, self.RULE_primitiveItem)
        try:
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.match(TaleParser.IDENTIFIER)
                pass
            elif token in [TaleParser.NUMBER, TaleParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
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
        self.enterRule(localctx, 58, self.RULE_literal)
        try:
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.intLiteral()
                pass
            elif token in [TaleParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
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
        self.enterRule(localctx, 60, self.RULE_intLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
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
        self.enterRule(localctx, 62, self.RULE_stringLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
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
        self._predicates[20] = self.unary_sempred
        self._predicates[22] = self.binary_sempred
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
         




