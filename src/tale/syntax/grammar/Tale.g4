grammar Tale;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from .TaleParser import TaleParser
}

@lexer::members {
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
}


program: (NEWLINE | statement)*;
statement: assignment | expression;

assignment: assignmentForm '=' assignmentBody;

assignmentForm: unaryForm
              | unaryOperatorForm
              | binaryForm
              | keywordForm
              | simpleForm;

unaryForm: argument IDENTIFIER;
unaryOperatorForm: OPERATOR argument;
binaryForm: argument OPERATOR argument;
keywordForm: argument? (IDENTIFIER ':' argument)+;
simpleForm: IDENTIFIER;

argument: simpleArgument
        | patternMatchingArgument;

simpleArgument: '(' argumentName (':' argumentType)? ')';
patternMatchingArgument: IDENTIFIER
                       | NUMBER;
argumentName: IDENTIFIER;
argumentType: IDENTIFIER;

assignmentBody: simpleAssignmentBody
              | compoundAssignmentBody;

simpleAssignmentBody: expression | expressionInBrackets;
compoundAssignmentBody: INDENT statement+ DEDENT;

expression: unary
          | binary
          | keyword
          | primitive NEWLINE;
expressionInBrackets: '(' expression ')';
expressionInBracketsWithOperator: OPERATOR expressionInBrackets;

unary: unary IDENTIFIER
     | expressionInBracketsWithOperator IDENTIFIER
     | expressionInBrackets IDENTIFIER
     | primitive IDENTIFIER;

binary: binary OPERATOR binaryOperand |
        binaryOperand OPERATOR binaryOperand;
binaryOperand: unary
             | primitive
             | expressionInBracketsWithOperator
             | expressionInBrackets;

keyword: keywordPrefix? (keywordName ':' keywordValue)+;
keywordPrefix: unary
             | binary
             | primitive
             | expressionInBracketsWithOperator
             | expressionInBrackets;
keywordName: IDENTIFIER;
keywordValue: unary
            | binary
            | primitive
            | expressionInBracketsWithOperator
            | expressionInBrackets;

primitive: primitiveWithOperator
         | IDENTIFIER
         | NUMBER;
primitiveWithOperator: OPERATOR IDENTIFIER
                     | OPERATOR NUMBER;


IDENTIFIER: [a-zA-Z]+;
NUMBER: [0-9]+;
OPERATOR: '-'
        | '+'
        | '*'
        | '/';

WS: [ \t]+ -> skip;
NEWLINE: ('\r'? '\n' ' '*);
