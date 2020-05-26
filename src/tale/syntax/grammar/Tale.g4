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

unaryForm: parameters IDENTIFIER;
unaryOperatorForm: OPERATOR parameters;
binaryForm: parameters OPERATOR parameters;
keywordForm: parameters? (IDENTIFIER ':' parameters)+;
simpleForm: IDENTIFIER;

parameters: parameter (',' parameter)*;
parameter: simpleParameter
         | patternMatchingParameter;

simpleParameter: '(' parameterName (':' parameterType)? ')';
patternMatchingParameter: IDENTIFIER
                        | literal;
parameterName: IDENTIFIER;
parameterType: IDENTIFIER;

assignmentBody: simpleAssignmentBody
              | compoundAssignmentBody;

simpleAssignmentBody: expression | expressionInBrackets;
compoundAssignmentBody: INDENT statement+ DEDENT;

expression: unary NEWLINE
          | binary NEWLINE
          | keyword NEWLINE
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

primitive: primitiveItem (',' primitiveItem)*?;
primitiveItem: primitiveWithOperator
         | IDENTIFIER
         | literal;
primitiveWithOperator: OPERATOR IDENTIFIER
                     | OPERATOR literal;

literal: intLiteral
       | stringLiteral;

intLiteral: NUMBER;
stringLiteral: STRING;

IDENTIFIER: [a-zA-Z]+;
NUMBER: [0-9]+;
OPERATOR: '-'
        | '+'
        | '*'
        | '/';
STRING: '"' (.)*? '"';

WS: [ \t]+ -> skip;
NEWLINE: ('\r'? '\n' ' '*);

fragment COMMENT: '--' ~[\r\n\f]*;

SKIP_: (WS | COMMENT) -> skip;
