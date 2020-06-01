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
        buf.write("\u00df\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\3\2\3\2\7\2A\n\2\f\2\16\2D\13\2\3\2\3\2\3\3")
        buf.write("\3\3\5\3J\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5T\n\5")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\5\b^\n\b\3\b\3\b\3\b")
        buf.write("\6\bc\n\b\r\b\16\bd\3\t\3\t\3\n\3\n\5\nk\n\n\3\13\3\13")
        buf.write("\3\13\6\13p\n\13\r\13\16\13q\3\f\3\f\5\fv\n\f\3\r\3\r")
        buf.write("\3\r\3\r\5\r|\n\r\3\r\3\r\3\16\3\16\5\16\u0082\n\16\3")
        buf.write("\17\3\17\3\20\3\20\3\21\3\21\5\21\u008a\n\21\3\22\3\22")
        buf.write("\3\23\3\23\3\23\6\23\u0091\n\23\r\23\16\23\u0092\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\5\24\u009b\n\24\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\7\25\u00a3\n\25\f\25\16\25\u00a6\13")
        buf.write("\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u00b0")
        buf.write("\n\26\f\26\16\26\u00b3\13\26\3\27\3\27\5\27\u00b7\n\27")
        buf.write("\3\30\5\30\u00ba\n\30\3\30\3\30\3\30\3\30\6\30\u00c0\n")
        buf.write("\30\r\30\16\30\u00c1\3\31\3\31\3\31\5\31\u00c7\n\31\3")
        buf.write("\32\3\32\3\33\3\33\3\33\7\33\u00ce\n\33\f\33\16\33\u00d1")
        buf.write("\13\33\3\34\3\34\5\34\u00d5\n\34\3\35\3\35\5\35\u00d9")
        buf.write("\n\35\3\36\3\36\3\37\3\37\3\37\3\u00cf\4(* \2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write("\2\2\2\u00dd\2B\3\2\2\2\4I\3\2\2\2\6K\3\2\2\2\bS\3\2\2")
        buf.write("\2\nU\3\2\2\2\fX\3\2\2\2\16]\3\2\2\2\20f\3\2\2\2\22j\3")
        buf.write("\2\2\2\24l\3\2\2\2\26u\3\2\2\2\30w\3\2\2\2\32\u0081\3")
        buf.write("\2\2\2\34\u0083\3\2\2\2\36\u0085\3\2\2\2 \u0089\3\2\2")
        buf.write("\2\"\u008b\3\2\2\2$\u008d\3\2\2\2&\u009a\3\2\2\2(\u009c")
        buf.write("\3\2\2\2*\u00a7\3\2\2\2,\u00b6\3\2\2\2.\u00b9\3\2\2\2")
        buf.write("\60\u00c6\3\2\2\2\62\u00c8\3\2\2\2\64\u00ca\3\2\2\2\66")
        buf.write("\u00d4\3\2\2\28\u00d8\3\2\2\2:\u00da\3\2\2\2<\u00dc\3")
        buf.write("\2\2\2>A\7\r\2\2?A\5\4\3\2@>\3\2\2\2@?\3\2\2\2AD\3\2\2")
        buf.write("\2B@\3\2\2\2BC\3\2\2\2CE\3\2\2\2DB\3\2\2\2EF\7\2\2\3F")
        buf.write("\3\3\2\2\2GJ\5\6\4\2HJ\5&\24\2IG\3\2\2\2IH\3\2\2\2J\5")
        buf.write("\3\2\2\2KL\5\b\5\2LM\7\3\2\2MN\5 \21\2N\7\3\2\2\2OT\5")
        buf.write("\n\6\2PT\5\f\7\2QT\5\16\b\2RT\5\20\t\2SO\3\2\2\2SP\3\2")
        buf.write("\2\2SQ\3\2\2\2SR\3\2\2\2T\t\3\2\2\2UV\5\22\n\2VW\7\b\2")
        buf.write("\2W\13\3\2\2\2XY\5\22\n\2YZ\7\n\2\2Z[\5\22\n\2[\r\3\2")
        buf.write("\2\2\\^\5\22\n\2]\\\3\2\2\2]^\3\2\2\2^b\3\2\2\2_`\7\b")
        buf.write("\2\2`a\7\4\2\2ac\5\22\n\2b_\3\2\2\2cd\3\2\2\2db\3\2\2")
        buf.write("\2de\3\2\2\2e\17\3\2\2\2fg\7\b\2\2g\21\3\2\2\2hk\5\26")
        buf.write("\f\2ik\5\24\13\2jh\3\2\2\2ji\3\2\2\2k\23\3\2\2\2lo\5\26")
        buf.write("\f\2mn\7\5\2\2np\5\26\f\2om\3\2\2\2pq\3\2\2\2qo\3\2\2")
        buf.write("\2qr\3\2\2\2r\25\3\2\2\2sv\5\30\r\2tv\5\32\16\2us\3\2")
        buf.write("\2\2ut\3\2\2\2v\27\3\2\2\2wx\7\6\2\2x{\5\34\17\2yz\7\4")
        buf.write("\2\2z|\5\36\20\2{y\3\2\2\2{|\3\2\2\2|}\3\2\2\2}~\7\7\2")
        buf.write("\2~\31\3\2\2\2\177\u0082\7\b\2\2\u0080\u0082\58\35\2\u0081")
        buf.write("\177\3\2\2\2\u0081\u0080\3\2\2\2\u0082\33\3\2\2\2\u0083")
        buf.write("\u0084\7\b\2\2\u0084\35\3\2\2\2\u0085\u0086\7\b\2\2\u0086")
        buf.write("\37\3\2\2\2\u0087\u008a\5\"\22\2\u0088\u008a\5$\23\2\u0089")
        buf.write("\u0087\3\2\2\2\u0089\u0088\3\2\2\2\u008a!\3\2\2\2\u008b")
        buf.write("\u008c\5&\24\2\u008c#\3\2\2\2\u008d\u0090\7\17\2\2\u008e")
        buf.write("\u0091\7\r\2\2\u008f\u0091\5\4\3\2\u0090\u008e\3\2\2\2")
        buf.write("\u0090\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0090\3")
        buf.write("\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095")
        buf.write("\7\20\2\2\u0095%\3\2\2\2\u0096\u009b\5(\25\2\u0097\u009b")
        buf.write("\5*\26\2\u0098\u009b\5.\30\2\u0099\u009b\5\64\33\2\u009a")
        buf.write("\u0096\3\2\2\2\u009a\u0097\3\2\2\2\u009a\u0098\3\2\2\2")
        buf.write("\u009a\u0099\3\2\2\2\u009b\'\3\2\2\2\u009c\u009d\b\25")
        buf.write("\1\2\u009d\u009e\5\64\33\2\u009e\u009f\7\b\2\2\u009f\u00a4")
        buf.write("\3\2\2\2\u00a0\u00a1\f\4\2\2\u00a1\u00a3\7\b\2\2\u00a2")
        buf.write("\u00a0\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2")
        buf.write("\u00a4\u00a5\3\2\2\2\u00a5)\3\2\2\2\u00a6\u00a4\3\2\2")
        buf.write("\2\u00a7\u00a8\b\26\1\2\u00a8\u00a9\5,\27\2\u00a9\u00aa")
        buf.write("\7\n\2\2\u00aa\u00ab\5,\27\2\u00ab\u00b1\3\2\2\2\u00ac")
        buf.write("\u00ad\f\4\2\2\u00ad\u00ae\7\n\2\2\u00ae\u00b0\5,\27\2")
        buf.write("\u00af\u00ac\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1\u00af\3")
        buf.write("\2\2\2\u00b1\u00b2\3\2\2\2\u00b2+\3\2\2\2\u00b3\u00b1")
        buf.write("\3\2\2\2\u00b4\u00b7\5(\25\2\u00b5\u00b7\5\64\33\2\u00b6")
        buf.write("\u00b4\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7-\3\2\2\2\u00b8")
        buf.write("\u00ba\5\60\31\2\u00b9\u00b8\3\2\2\2\u00b9\u00ba\3\2\2")
        buf.write("\2\u00ba\u00bf\3\2\2\2\u00bb\u00bc\5\62\32\2\u00bc\u00bd")
        buf.write("\7\4\2\2\u00bd\u00be\5\60\31\2\u00be\u00c0\3\2\2\2\u00bf")
        buf.write("\u00bb\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00bf\3\2\2\2")
        buf.write("\u00c1\u00c2\3\2\2\2\u00c2/\3\2\2\2\u00c3\u00c7\5(\25")
        buf.write("\2\u00c4\u00c7\5*\26\2\u00c5\u00c7\5\64\33\2\u00c6\u00c3")
        buf.write("\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7")
        buf.write("\61\3\2\2\2\u00c8\u00c9\7\b\2\2\u00c9\63\3\2\2\2\u00ca")
        buf.write("\u00cf\5\66\34\2\u00cb\u00cc\7\5\2\2\u00cc\u00ce\5\66")
        buf.write("\34\2\u00cd\u00cb\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00d0")
        buf.write("\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\65\3\2\2\2\u00d1\u00cf")
        buf.write("\3\2\2\2\u00d2\u00d5\7\b\2\2\u00d3\u00d5\58\35\2\u00d4")
        buf.write("\u00d2\3\2\2\2\u00d4\u00d3\3\2\2\2\u00d5\67\3\2\2\2\u00d6")
        buf.write("\u00d9\5:\36\2\u00d7\u00d9\5<\37\2\u00d8\u00d6\3\2\2\2")
        buf.write("\u00d8\u00d7\3\2\2\2\u00d99\3\2\2\2\u00da\u00db\7\t\2")
        buf.write("\2\u00db;\3\2\2\2\u00dc\u00dd\7\13\2\2\u00dd=\3\2\2\2")
        buf.write("\32@BIS]djqu{\u0081\u0089\u0090\u0092\u009a\u00a4\u00b1")
        buf.write("\u00b6\u00b9\u00c1\u00c6\u00cf\u00d4\u00d8")
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
    RULE_parameter = 8
    RULE_tupleParameter = 9
    RULE_singleParameter = 10
    RULE_simpleParameter = 11
    RULE_patternMatchingParameter = 12
    RULE_parameterName = 13
    RULE_parameterType = 14
    RULE_assignmentBody = 15
    RULE_simpleAssignmentBody = 16
    RULE_compoundAssignmentBody = 17
    RULE_expression = 18
    RULE_unary = 19
    RULE_binary = 20
    RULE_binaryOperand = 21
    RULE_keyword = 22
    RULE_keywordArgument = 23
    RULE_keywordName = 24
    RULE_primitive = 25
    RULE_primitiveItem = 26
    RULE_literal = 27
    RULE_intLiteral = 28
    RULE_stringLiteral = 29

    ruleNames =  [ "program", "statement", "assignment", "form", "unaryForm", 
                   "binaryForm", "keywordForm", "primitiveForm", "parameter", 
                   "tupleParameter", "singleParameter", "simpleParameter", 
                   "patternMatchingParameter", "parameterName", "parameterType", 
                   "assignmentBody", "simpleAssignmentBody", "compoundAssignmentBody", 
                   "expression", "unary", "binary", "binaryOperand", "keyword", 
                   "keywordArgument", "keywordName", "primitive", "primitiveItem", 
                   "literal", "intLiteral", "stringLiteral" ]

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
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TaleParser.T__3) | (1 << TaleParser.IDENTIFIER) | (1 << TaleParser.NUMBER) | (1 << TaleParser.STRING) | (1 << TaleParser.NEWLINE))) != 0):
                self.state = 62
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [TaleParser.NEWLINE]:
                    self.state = 60
                    self.match(TaleParser.NEWLINE)
                    pass
                elif token in [TaleParser.T__3, TaleParser.IDENTIFIER, TaleParser.NUMBER, TaleParser.STRING]:
                    self.state = 61
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
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
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
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
            self.state = 73
            self.form()
            self.state = 74
            self.match(TaleParser.T__0)
            self.state = 75
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
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.unaryForm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.binaryForm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 79
                self.keywordForm()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 80
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
            self.state = 83
            self.parameter()
            self.state = 84
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
        self.enterRule(localctx, 10, self.RULE_binaryForm)
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
        self.enterRule(localctx, 12, self.RULE_keywordForm)
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
        self.enterRule(localctx, 16, self.RULE_parameter)
        try:
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.singleParameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
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
        self.enterRule(localctx, 18, self.RULE_tupleParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.singleParameter()
            self.state = 109 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 107
                self.match(TaleParser.T__2)
                self.state = 108
                self.singleParameter()
                self.state = 111 
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
        self.enterRule(localctx, 20, self.RULE_singleParameter)
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.simpleParameter()
                pass
            elif token in [TaleParser.IDENTIFIER, TaleParser.NUMBER, TaleParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
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
        self.enterRule(localctx, 22, self.RULE_simpleParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(TaleParser.T__3)
            self.state = 118
            self.parameterName()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TaleParser.T__1:
                self.state = 119
                self.match(TaleParser.T__1)
                self.state = 120
                self.parameterType()


            self.state = 123
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
        self.enterRule(localctx, 24, self.RULE_patternMatchingParameter)
        try:
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.match(TaleParser.IDENTIFIER)
                pass
            elif token in [TaleParser.NUMBER, TaleParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
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
        self.enterRule(localctx, 26, self.RULE_parameterName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
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
        self.enterRule(localctx, 28, self.RULE_parameterType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
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
        self.enterRule(localctx, 30, self.RULE_assignmentBody)
        try:
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.IDENTIFIER, TaleParser.NUMBER, TaleParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.simpleAssignmentBody()
                pass
            elif token in [TaleParser.INDENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
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
        self.enterRule(localctx, 32, self.RULE_simpleAssignmentBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
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
        self.enterRule(localctx, 34, self.RULE_compoundAssignmentBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(TaleParser.INDENT)
            self.state = 142 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 142
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [TaleParser.NEWLINE]:
                    self.state = 140
                    self.match(TaleParser.NEWLINE)
                    pass
                elif token in [TaleParser.T__3, TaleParser.IDENTIFIER, TaleParser.NUMBER, TaleParser.STRING]:
                    self.state = 141
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 144 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TaleParser.T__3) | (1 << TaleParser.IDENTIFIER) | (1 << TaleParser.NUMBER) | (1 << TaleParser.STRING) | (1 << TaleParser.NEWLINE))) != 0)):
                    break

            self.state = 146
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
        self.enterRule(localctx, 36, self.RULE_expression)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.unary(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.binary(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.keyword()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 151
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
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_unary, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.primitive()
            self.state = 156
            self.match(TaleParser.IDENTIFIER)
            self._ctx.stop = self._input.LT(-1)
            self.state = 162
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TaleParser.UnaryContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_unary)
                    self.state = 158
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 159
                    self.match(TaleParser.IDENTIFIER) 
                self.state = 164
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_binary, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.binaryOperand()
            self.state = 167
            self.match(TaleParser.OPERATOR)
            self.state = 168
            self.binaryOperand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 175
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TaleParser.BinaryContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_binary)
                    self.state = 170
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 171
                    self.match(TaleParser.OPERATOR)
                    self.state = 172
                    self.binaryOperand() 
                self.state = 177
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        self.enterRule(localctx, 42, self.RULE_binaryOperand)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.unary(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
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
        self.enterRule(localctx, 44, self.RULE_keyword)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 182
                self.keywordArgument()


            self.state = 189 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 185
                    self.keywordName()
                    self.state = 186
                    self.match(TaleParser.T__1)
                    self.state = 187
                    self.keywordArgument()

                else:
                    raise NoViableAltException(self)
                self.state = 191 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        self.enterRule(localctx, 46, self.RULE_keywordArgument)
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.unary(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.binary(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 195
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
        self.enterRule(localctx, 48, self.RULE_keywordName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
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
        self.enterRule(localctx, 50, self.RULE_primitive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.primitiveItem()
            self.state = 205
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 201
                    self.match(TaleParser.T__2)
                    self.state = 202
                    self.primitiveItem() 
                self.state = 207
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        self.enterRule(localctx, 52, self.RULE_primitiveItem)
        try:
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.match(TaleParser.IDENTIFIER)
                pass
            elif token in [TaleParser.NUMBER, TaleParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
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
        self.enterRule(localctx, 54, self.RULE_literal)
        try:
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.intLiteral()
                pass
            elif token in [TaleParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
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
        self.enterRule(localctx, 56, self.RULE_intLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
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
        self.enterRule(localctx, 58, self.RULE_stringLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
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
        self._predicates[19] = self.unary_sempred
        self._predicates[20] = self.binary_sempred
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
         




