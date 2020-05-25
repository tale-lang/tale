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
        buf.write("\u0106\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\3\2\7\2G\n\2\f\2\16")
        buf.write("\2J\13\2\3\3\3\3\5\3N\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\5\5Y\n\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\t\5\tf\n\t\3\t\3\t\3\t\6\tk\n\t\r\t\16\tl\3\n\3")
        buf.write("\n\3\13\3\13\5\13s\n\13\3\f\3\f\3\f\3\f\5\fy\n\f\3\f\3")
        buf.write("\f\3\r\3\r\5\r\177\n\r\3\16\3\16\3\17\3\17\3\20\3\20\5")
        buf.write("\20\u0087\n\20\3\21\3\21\5\21\u008b\n\21\3\22\3\22\6\22")
        buf.write("\u008f\n\22\r\22\16\22\u0090\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00a1")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u00b4\n\26\3")
        buf.write("\26\3\26\7\26\u00b8\n\26\f\26\16\26\u00bb\13\26\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u00c5\n\27\f\27")
        buf.write("\16\27\u00c8\13\27\3\30\3\30\3\30\3\30\5\30\u00ce\n\30")
        buf.write("\3\31\5\31\u00d1\n\31\3\31\3\31\3\31\3\31\6\31\u00d7\n")
        buf.write("\31\r\31\16\31\u00d8\3\32\3\32\3\32\3\32\3\32\5\32\u00e0")
        buf.write("\n\32\3\33\3\33\3\34\3\34\3\34\3\34\3\34\5\34\u00e9\n")
        buf.write("\34\3\35\3\35\3\35\7\35\u00ee\n\35\f\35\16\35\u00f1\13")
        buf.write("\35\3\36\3\36\3\36\5\36\u00f6\n\36\3\37\3\37\3\37\3\37")
        buf.write("\5\37\u00fc\n\37\3 \3 \5 \u0100\n \3!\3!\3\"\3\"\3\"\3")
        buf.write("\u00ef\4*,#\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@B\2\2\2\u010c\2H\3\2\2\2\4M\3\2")
        buf.write("\2\2\6O\3\2\2\2\bX\3\2\2\2\nZ\3\2\2\2\f]\3\2\2\2\16`\3")
        buf.write("\2\2\2\20e\3\2\2\2\22n\3\2\2\2\24r\3\2\2\2\26t\3\2\2\2")
        buf.write("\30~\3\2\2\2\32\u0080\3\2\2\2\34\u0082\3\2\2\2\36\u0086")
        buf.write("\3\2\2\2 \u008a\3\2\2\2\"\u008c\3\2\2\2$\u00a0\3\2\2\2")
        buf.write("&\u00a2\3\2\2\2(\u00a6\3\2\2\2*\u00b3\3\2\2\2,\u00bc\3")
        buf.write("\2\2\2.\u00cd\3\2\2\2\60\u00d0\3\2\2\2\62\u00df\3\2\2")
        buf.write("\2\64\u00e1\3\2\2\2\66\u00e8\3\2\2\28\u00ea\3\2\2\2:\u00f5")
        buf.write("\3\2\2\2<\u00fb\3\2\2\2>\u00ff\3\2\2\2@\u0101\3\2\2\2")
        buf.write("B\u0103\3\2\2\2DG\7\r\2\2EG\5\4\3\2FD\3\2\2\2FE\3\2\2")
        buf.write("\2GJ\3\2\2\2HF\3\2\2\2HI\3\2\2\2I\3\3\2\2\2JH\3\2\2\2")
        buf.write("KN\5\6\4\2LN\5$\23\2MK\3\2\2\2ML\3\2\2\2N\5\3\2\2\2OP")
        buf.write("\5\b\5\2PQ\7\3\2\2QR\5\36\20\2R\7\3\2\2\2SY\5\n\6\2TY")
        buf.write("\5\f\7\2UY\5\16\b\2VY\5\20\t\2WY\5\22\n\2XS\3\2\2\2XT")
        buf.write("\3\2\2\2XU\3\2\2\2XV\3\2\2\2XW\3\2\2\2Y\t\3\2\2\2Z[\5")
        buf.write("\24\13\2[\\\7\b\2\2\\\13\3\2\2\2]^\7\n\2\2^_\5\24\13\2")
        buf.write("_\r\3\2\2\2`a\5\24\13\2ab\7\n\2\2bc\5\24\13\2c\17\3\2")
        buf.write("\2\2df\5\24\13\2ed\3\2\2\2ef\3\2\2\2fj\3\2\2\2gh\7\b\2")
        buf.write("\2hi\7\4\2\2ik\5\24\13\2jg\3\2\2\2kl\3\2\2\2lj\3\2\2\2")
        buf.write("lm\3\2\2\2m\21\3\2\2\2no\7\b\2\2o\23\3\2\2\2ps\5\26\f")
        buf.write("\2qs\5\30\r\2rp\3\2\2\2rq\3\2\2\2s\25\3\2\2\2tu\7\5\2")
        buf.write("\2ux\5\32\16\2vw\7\4\2\2wy\5\34\17\2xv\3\2\2\2xy\3\2\2")
        buf.write("\2yz\3\2\2\2z{\7\6\2\2{\27\3\2\2\2|\177\7\b\2\2}\177\5")
        buf.write("> \2~|\3\2\2\2~}\3\2\2\2\177\31\3\2\2\2\u0080\u0081\7")
        buf.write("\b\2\2\u0081\33\3\2\2\2\u0082\u0083\7\b\2\2\u0083\35\3")
        buf.write("\2\2\2\u0084\u0087\5 \21\2\u0085\u0087\5\"\22\2\u0086")
        buf.write("\u0084\3\2\2\2\u0086\u0085\3\2\2\2\u0087\37\3\2\2\2\u0088")
        buf.write("\u008b\5$\23\2\u0089\u008b\5&\24\2\u008a\u0088\3\2\2\2")
        buf.write("\u008a\u0089\3\2\2\2\u008b!\3\2\2\2\u008c\u008e\7\17\2")
        buf.write("\2\u008d\u008f\5\4\3\2\u008e\u008d\3\2\2\2\u008f\u0090")
        buf.write("\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091")
        buf.write("\u0092\3\2\2\2\u0092\u0093\7\20\2\2\u0093#\3\2\2\2\u0094")
        buf.write("\u0095\5*\26\2\u0095\u0096\7\r\2\2\u0096\u00a1\3\2\2\2")
        buf.write("\u0097\u0098\5,\27\2\u0098\u0099\7\r\2\2\u0099\u00a1\3")
        buf.write("\2\2\2\u009a\u009b\5\60\31\2\u009b\u009c\7\r\2\2\u009c")
        buf.write("\u00a1\3\2\2\2\u009d\u009e\58\35\2\u009e\u009f\7\r\2\2")
        buf.write("\u009f\u00a1\3\2\2\2\u00a0\u0094\3\2\2\2\u00a0\u0097\3")
        buf.write("\2\2\2\u00a0\u009a\3\2\2\2\u00a0\u009d\3\2\2\2\u00a1%")
        buf.write("\3\2\2\2\u00a2\u00a3\7\5\2\2\u00a3\u00a4\5$\23\2\u00a4")
        buf.write("\u00a5\7\6\2\2\u00a5\'\3\2\2\2\u00a6\u00a7\7\n\2\2\u00a7")
        buf.write("\u00a8\5&\24\2\u00a8)\3\2\2\2\u00a9\u00aa\b\26\1\2\u00aa")
        buf.write("\u00ab\5(\25\2\u00ab\u00ac\7\b\2\2\u00ac\u00b4\3\2\2\2")
        buf.write("\u00ad\u00ae\5&\24\2\u00ae\u00af\7\b\2\2\u00af\u00b4\3")
        buf.write("\2\2\2\u00b0\u00b1\58\35\2\u00b1\u00b2\7\b\2\2\u00b2\u00b4")
        buf.write("\3\2\2\2\u00b3\u00a9\3\2\2\2\u00b3\u00ad\3\2\2\2\u00b3")
        buf.write("\u00b0\3\2\2\2\u00b4\u00b9\3\2\2\2\u00b5\u00b6\f\6\2\2")
        buf.write("\u00b6\u00b8\7\b\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00bb\3")
        buf.write("\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba+")
        buf.write("\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc\u00bd\b\27\1\2\u00bd")
        buf.write("\u00be\5.\30\2\u00be\u00bf\7\n\2\2\u00bf\u00c0\5.\30\2")
        buf.write("\u00c0\u00c6\3\2\2\2\u00c1\u00c2\f\4\2\2\u00c2\u00c3\7")
        buf.write("\n\2\2\u00c3\u00c5\5.\30\2\u00c4\u00c1\3\2\2\2\u00c5\u00c8")
        buf.write("\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7")
        buf.write("-\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00ce\5*\26\2\u00ca")
        buf.write("\u00ce\58\35\2\u00cb\u00ce\5(\25\2\u00cc\u00ce\5&\24\2")
        buf.write("\u00cd\u00c9\3\2\2\2\u00cd\u00ca\3\2\2\2\u00cd\u00cb\3")
        buf.write("\2\2\2\u00cd\u00cc\3\2\2\2\u00ce/\3\2\2\2\u00cf\u00d1")
        buf.write("\5\62\32\2\u00d0\u00cf\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1")
        buf.write("\u00d6\3\2\2\2\u00d2\u00d3\5\64\33\2\u00d3\u00d4\7\4\2")
        buf.write("\2\u00d4\u00d5\5\66\34\2\u00d5\u00d7\3\2\2\2\u00d6\u00d2")
        buf.write("\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8")
        buf.write("\u00d9\3\2\2\2\u00d9\61\3\2\2\2\u00da\u00e0\5*\26\2\u00db")
        buf.write("\u00e0\5,\27\2\u00dc\u00e0\58\35\2\u00dd\u00e0\5(\25\2")
        buf.write("\u00de\u00e0\5&\24\2\u00df\u00da\3\2\2\2\u00df\u00db\3")
        buf.write("\2\2\2\u00df\u00dc\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00de")
        buf.write("\3\2\2\2\u00e0\63\3\2\2\2\u00e1\u00e2\7\b\2\2\u00e2\65")
        buf.write("\3\2\2\2\u00e3\u00e9\5*\26\2\u00e4\u00e9\5,\27\2\u00e5")
        buf.write("\u00e9\58\35\2\u00e6\u00e9\5(\25\2\u00e7\u00e9\5&\24\2")
        buf.write("\u00e8\u00e3\3\2\2\2\u00e8\u00e4\3\2\2\2\u00e8\u00e5\3")
        buf.write("\2\2\2\u00e8\u00e6\3\2\2\2\u00e8\u00e7\3\2\2\2\u00e9\67")
        buf.write("\3\2\2\2\u00ea\u00ef\5:\36\2\u00eb\u00ec\7\7\2\2\u00ec")
        buf.write("\u00ee\5:\36\2\u00ed\u00eb\3\2\2\2\u00ee\u00f1\3\2\2\2")
        buf.write("\u00ef\u00f0\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f09\3\2\2")
        buf.write("\2\u00f1\u00ef\3\2\2\2\u00f2\u00f6\5<\37\2\u00f3\u00f6")
        buf.write("\7\b\2\2\u00f4\u00f6\5> \2\u00f5\u00f2\3\2\2\2\u00f5\u00f3")
        buf.write("\3\2\2\2\u00f5\u00f4\3\2\2\2\u00f6;\3\2\2\2\u00f7\u00f8")
        buf.write("\7\n\2\2\u00f8\u00fc\7\b\2\2\u00f9\u00fa\7\n\2\2\u00fa")
        buf.write("\u00fc\5> \2\u00fb\u00f7\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fc")
        buf.write("=\3\2\2\2\u00fd\u0100\5@!\2\u00fe\u0100\5B\"\2\u00ff\u00fd")
        buf.write("\3\2\2\2\u00ff\u00fe\3\2\2\2\u0100?\3\2\2\2\u0101\u0102")
        buf.write("\7\t\2\2\u0102A\3\2\2\2\u0103\u0104\7\13\2\2\u0104C\3")
        buf.write("\2\2\2\33FHMXelrx~\u0086\u008a\u0090\u00a0\u00b3\u00b9")
        buf.write("\u00c6\u00cd\u00d0\u00d8\u00df\u00e8\u00ef\u00f5\u00fb")
        buf.write("\u00ff")
        return buf.getvalue()


class TaleParser ( Parser ):

    grammarFileName = "Tale.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "':'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IDENTIFIER", "NUMBER", 
                      "OPERATOR", "STRING", "WS", "NEWLINE", "SKIP_", "INDENT", 
                      "DEDENT" ]

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
    RULE_primitiveValue = 28
    RULE_primitiveWithOperator = 29
    RULE_literal = 30
    RULE_intLiteral = 31
    RULE_stringLiteral = 32

    ruleNames =  [ "program", "statement", "assignment", "assignmentForm", 
                   "unaryForm", "unaryOperatorForm", "binaryForm", "keywordForm", 
                   "simpleForm", "parameter", "simpleParameter", "patternMatchingParameter", 
                   "parameterName", "parameterType", "assignmentBody", "simpleAssignmentBody", 
                   "compoundAssignmentBody", "expression", "expressionInBrackets", 
                   "expressionInBracketsWithOperator", "unary", "binary", 
                   "binaryOperand", "keyword", "keywordPrefix", "keywordName", 
                   "keywordValue", "primitive", "primitiveValue", "primitiveWithOperator", 
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
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TaleParser.T__2) | (1 << TaleParser.IDENTIFIER) | (1 << TaleParser.NUMBER) | (1 << TaleParser.OPERATOR) | (1 << TaleParser.STRING) | (1 << TaleParser.NEWLINE))) != 0):
                self.state = 68
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [TaleParser.NEWLINE]:
                    self.state = 66
                    self.match(TaleParser.NEWLINE)
                    pass
                elif token in [TaleParser.T__2, TaleParser.IDENTIFIER, TaleParser.NUMBER, TaleParser.OPERATOR, TaleParser.STRING]:
                    self.state = 67
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 72
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
            self.state = 77
            self.assignmentForm()
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
                self.unaryOperatorForm()
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
            self.state = 91
            self.match(TaleParser.OPERATOR)
            self.state = 92
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
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.simpleParameter()
                pass
            elif token in [TaleParser.IDENTIFIER, TaleParser.NUMBER, TaleParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
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
            self.state = 114
            self.match(TaleParser.T__2)
            self.state = 115
            self.parameterName()
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TaleParser.T__1:
                self.state = 116
                self.match(TaleParser.T__1)
                self.state = 117
                self.parameterType()


            self.state = 120
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
            self.state = 124
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.match(TaleParser.IDENTIFIER)
                pass
            elif token in [TaleParser.NUMBER, TaleParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
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
            self.state = 126
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
            self.state = 128
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
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.T__2, TaleParser.IDENTIFIER, TaleParser.NUMBER, TaleParser.OPERATOR, TaleParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.simpleAssignmentBody()
                pass
            elif token in [TaleParser.INDENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
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
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
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
            self.state = 138
            self.match(TaleParser.INDENT)
            self.state = 140 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 139
                self.statement()
                self.state = 142 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TaleParser.T__2) | (1 << TaleParser.IDENTIFIER) | (1 << TaleParser.NUMBER) | (1 << TaleParser.OPERATOR) | (1 << TaleParser.STRING))) != 0)):
                    break

            self.state = 144
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
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.unary(0)
                self.state = 147
                self.match(TaleParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.binary(0)
                self.state = 150
                self.match(TaleParser.NEWLINE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 152
                self.keyword()
                self.state = 153
                self.match(TaleParser.NEWLINE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 155
                self.primitive()
                self.state = 156
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
            self.state = 160
            self.match(TaleParser.T__2)
            self.state = 161
            self.expression()
            self.state = 162
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
            self.state = 164
            self.match(TaleParser.OPERATOR)
            self.state = 165
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
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 168
                self.expressionInBracketsWithOperator()
                self.state = 169
                self.match(TaleParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 171
                self.expressionInBrackets()
                self.state = 172
                self.match(TaleParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.state = 174
                self.primitive()
                self.state = 175
                self.match(TaleParser.IDENTIFIER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 183
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TaleParser.UnaryContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_unary)
                    self.state = 179
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 180
                    self.match(TaleParser.IDENTIFIER) 
                self.state = 185
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
            self.state = 187
            self.binaryOperand()
            self.state = 188
            self.match(TaleParser.OPERATOR)
            self.state = 189
            self.binaryOperand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 196
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TaleParser.BinaryContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_binary)
                    self.state = 191
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 192
                    self.match(TaleParser.OPERATOR)
                    self.state = 193
                    self.binaryOperand() 
                self.state = 198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.unary(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.primitive()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 201
                self.expressionInBracketsWithOperator()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 202
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 205
                self.keywordPrefix()


            self.state = 212 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 208
                self.keywordName()
                self.state = 209
                self.match(TaleParser.T__1)
                self.state = 210
                self.keywordValue()
                self.state = 214 
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
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.unary(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.binary(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 218
                self.primitive()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 219
                self.expressionInBracketsWithOperator()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 220
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
            self.state = 223
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
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.unary(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.binary(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.primitive()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 228
                self.expressionInBracketsWithOperator()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 229
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

        def primitiveValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TaleParser.PrimitiveValueContext)
            else:
                return self.getTypedRuleContext(TaleParser.PrimitiveValueContext,i)


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
            self.state = 232
            self.primitiveValue()
            self.state = 237
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 233
                    self.match(TaleParser.T__4)
                    self.state = 234
                    self.primitiveValue() 
                self.state = 239
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveWithOperator(self):
            return self.getTypedRuleContext(TaleParser.PrimitiveWithOperatorContext,0)


        def IDENTIFIER(self):
            return self.getToken(TaleParser.IDENTIFIER, 0)

        def literal(self):
            return self.getTypedRuleContext(TaleParser.LiteralContext,0)


        def getRuleIndex(self):
            return TaleParser.RULE_primitiveValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveValue" ):
                listener.enterPrimitiveValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveValue" ):
                listener.exitPrimitiveValue(self)




    def primitiveValue(self):

        localctx = TaleParser.PrimitiveValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_primitiveValue)
        try:
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.OPERATOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.primitiveWithOperator()
                pass
            elif token in [TaleParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.match(TaleParser.IDENTIFIER)
                pass
            elif token in [TaleParser.NUMBER, TaleParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
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


    class PrimitiveWithOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPERATOR(self):
            return self.getToken(TaleParser.OPERATOR, 0)

        def IDENTIFIER(self):
            return self.getToken(TaleParser.IDENTIFIER, 0)

        def literal(self):
            return self.getTypedRuleContext(TaleParser.LiteralContext,0)


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
        self.enterRule(localctx, 58, self.RULE_primitiveWithOperator)
        try:
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.match(TaleParser.OPERATOR)
                self.state = 246
                self.match(TaleParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.match(TaleParser.OPERATOR)
                self.state = 248
                self.literal()
                pass


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
        self.enterRule(localctx, 60, self.RULE_literal)
        try:
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TaleParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.intLiteral()
                pass
            elif token in [TaleParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
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
        self.enterRule(localctx, 62, self.RULE_intLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
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
        self.enterRule(localctx, 64, self.RULE_stringLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
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
         




