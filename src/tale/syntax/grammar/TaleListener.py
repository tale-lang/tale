# Generated from tale/syntax/grammar/Tale.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TaleParser import TaleParser
else:
    from TaleParser import TaleParser

# This class defines a complete listener for a parse tree produced by TaleParser.
class TaleListener(ParseTreeListener):

    # Enter a parse tree produced by TaleParser#program.
    def enterProgram(self, ctx:TaleParser.ProgramContext):
        pass

    # Exit a parse tree produced by TaleParser#program.
    def exitProgram(self, ctx:TaleParser.ProgramContext):
        pass


    # Enter a parse tree produced by TaleParser#statement.
    def enterStatement(self, ctx:TaleParser.StatementContext):
        pass

    # Exit a parse tree produced by TaleParser#statement.
    def exitStatement(self, ctx:TaleParser.StatementContext):
        pass


    # Enter a parse tree produced by TaleParser#assignment.
    def enterAssignment(self, ctx:TaleParser.AssignmentContext):
        pass

    # Exit a parse tree produced by TaleParser#assignment.
    def exitAssignment(self, ctx:TaleParser.AssignmentContext):
        pass


    # Enter a parse tree produced by TaleParser#assignmentName.
    def enterAssignmentName(self, ctx:TaleParser.AssignmentNameContext):
        pass

    # Exit a parse tree produced by TaleParser#assignmentName.
    def exitAssignmentName(self, ctx:TaleParser.AssignmentNameContext):
        pass


    # Enter a parse tree produced by TaleParser#assignmentForm.
    def enterAssignmentForm(self, ctx:TaleParser.AssignmentFormContext):
        pass

    # Exit a parse tree produced by TaleParser#assignmentForm.
    def exitAssignmentForm(self, ctx:TaleParser.AssignmentFormContext):
        pass


    # Enter a parse tree produced by TaleParser#unaryForm.
    def enterUnaryForm(self, ctx:TaleParser.UnaryFormContext):
        pass

    # Exit a parse tree produced by TaleParser#unaryForm.
    def exitUnaryForm(self, ctx:TaleParser.UnaryFormContext):
        pass


    # Enter a parse tree produced by TaleParser#unaryOperatorForm.
    def enterUnaryOperatorForm(self, ctx:TaleParser.UnaryOperatorFormContext):
        pass

    # Exit a parse tree produced by TaleParser#unaryOperatorForm.
    def exitUnaryOperatorForm(self, ctx:TaleParser.UnaryOperatorFormContext):
        pass


    # Enter a parse tree produced by TaleParser#binaryForm.
    def enterBinaryForm(self, ctx:TaleParser.BinaryFormContext):
        pass

    # Exit a parse tree produced by TaleParser#binaryForm.
    def exitBinaryForm(self, ctx:TaleParser.BinaryFormContext):
        pass


    # Enter a parse tree produced by TaleParser#keywordForm.
    def enterKeywordForm(self, ctx:TaleParser.KeywordFormContext):
        pass

    # Exit a parse tree produced by TaleParser#keywordForm.
    def exitKeywordForm(self, ctx:TaleParser.KeywordFormContext):
        pass


    # Enter a parse tree produced by TaleParser#argument.
    def enterArgument(self, ctx:TaleParser.ArgumentContext):
        pass

    # Exit a parse tree produced by TaleParser#argument.
    def exitArgument(self, ctx:TaleParser.ArgumentContext):
        pass


    # Enter a parse tree produced by TaleParser#argumentName.
    def enterArgumentName(self, ctx:TaleParser.ArgumentNameContext):
        pass

    # Exit a parse tree produced by TaleParser#argumentName.
    def exitArgumentName(self, ctx:TaleParser.ArgumentNameContext):
        pass


    # Enter a parse tree produced by TaleParser#argumentType.
    def enterArgumentType(self, ctx:TaleParser.ArgumentTypeContext):
        pass

    # Exit a parse tree produced by TaleParser#argumentType.
    def exitArgumentType(self, ctx:TaleParser.ArgumentTypeContext):
        pass


    # Enter a parse tree produced by TaleParser#expression.
    def enterExpression(self, ctx:TaleParser.ExpressionContext):
        pass

    # Exit a parse tree produced by TaleParser#expression.
    def exitExpression(self, ctx:TaleParser.ExpressionContext):
        pass


    # Enter a parse tree produced by TaleParser#expressionInBrackets.
    def enterExpressionInBrackets(self, ctx:TaleParser.ExpressionInBracketsContext):
        pass

    # Exit a parse tree produced by TaleParser#expressionInBrackets.
    def exitExpressionInBrackets(self, ctx:TaleParser.ExpressionInBracketsContext):
        pass


    # Enter a parse tree produced by TaleParser#expressionInBracketsWithOperator.
    def enterExpressionInBracketsWithOperator(self, ctx:TaleParser.ExpressionInBracketsWithOperatorContext):
        pass

    # Exit a parse tree produced by TaleParser#expressionInBracketsWithOperator.
    def exitExpressionInBracketsWithOperator(self, ctx:TaleParser.ExpressionInBracketsWithOperatorContext):
        pass


    # Enter a parse tree produced by TaleParser#unary.
    def enterUnary(self, ctx:TaleParser.UnaryContext):
        pass

    # Exit a parse tree produced by TaleParser#unary.
    def exitUnary(self, ctx:TaleParser.UnaryContext):
        pass


    # Enter a parse tree produced by TaleParser#binary.
    def enterBinary(self, ctx:TaleParser.BinaryContext):
        pass

    # Exit a parse tree produced by TaleParser#binary.
    def exitBinary(self, ctx:TaleParser.BinaryContext):
        pass


    # Enter a parse tree produced by TaleParser#binaryOperand.
    def enterBinaryOperand(self, ctx:TaleParser.BinaryOperandContext):
        pass

    # Exit a parse tree produced by TaleParser#binaryOperand.
    def exitBinaryOperand(self, ctx:TaleParser.BinaryOperandContext):
        pass


    # Enter a parse tree produced by TaleParser#keyword.
    def enterKeyword(self, ctx:TaleParser.KeywordContext):
        pass

    # Exit a parse tree produced by TaleParser#keyword.
    def exitKeyword(self, ctx:TaleParser.KeywordContext):
        pass


    # Enter a parse tree produced by TaleParser#keywordPrefix.
    def enterKeywordPrefix(self, ctx:TaleParser.KeywordPrefixContext):
        pass

    # Exit a parse tree produced by TaleParser#keywordPrefix.
    def exitKeywordPrefix(self, ctx:TaleParser.KeywordPrefixContext):
        pass


    # Enter a parse tree produced by TaleParser#keywordName.
    def enterKeywordName(self, ctx:TaleParser.KeywordNameContext):
        pass

    # Exit a parse tree produced by TaleParser#keywordName.
    def exitKeywordName(self, ctx:TaleParser.KeywordNameContext):
        pass


    # Enter a parse tree produced by TaleParser#keywordValue.
    def enterKeywordValue(self, ctx:TaleParser.KeywordValueContext):
        pass

    # Exit a parse tree produced by TaleParser#keywordValue.
    def exitKeywordValue(self, ctx:TaleParser.KeywordValueContext):
        pass


    # Enter a parse tree produced by TaleParser#primitive.
    def enterPrimitive(self, ctx:TaleParser.PrimitiveContext):
        pass

    # Exit a parse tree produced by TaleParser#primitive.
    def exitPrimitive(self, ctx:TaleParser.PrimitiveContext):
        pass


    # Enter a parse tree produced by TaleParser#primitiveWithOperator.
    def enterPrimitiveWithOperator(self, ctx:TaleParser.PrimitiveWithOperatorContext):
        pass

    # Exit a parse tree produced by TaleParser#primitiveWithOperator.
    def exitPrimitiveWithOperator(self, ctx:TaleParser.PrimitiveWithOperatorContext):
        pass



del TaleParser