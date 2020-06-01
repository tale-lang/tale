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


program: (NEWLINE | statement)* EOF;
statement: assignment | expression;

assignment: form '=' assignmentBody;

form: unaryForm
    | unaryOperatorForm
    | binaryForm
    | keywordForm
    | primitiveForm;

unaryForm: parameter IDENTIFIER;
unaryOperatorForm: OPERATOR singleParameter;
binaryForm: parameter OPERATOR parameter;
keywordForm: parameter? (IDENTIFIER ':' parameter)+;
primitiveForm: IDENTIFIER;

parameter: singleParameter
         | tupleParameter;

tupleParameter: singleParameter (',' singleParameter)+;
singleParameter: simpleParameter
               | patternMatchingParameter;

simpleParameter: '(' parameterName (':' parameterType)? ')';
patternMatchingParameter: IDENTIFIER | literal;

parameterName: IDENTIFIER;
parameterType: IDENTIFIER;

assignmentBody: simpleAssignmentBody
              | compoundAssignmentBody;

simpleAssignmentBody: expression;
compoundAssignmentBody: INDENT (NEWLINE | statement)+ DEDENT;

expression: unary
          | unaryOperator
          | binary
          | keyword
          | primitive;

unary: unary IDENTIFIER
     | primitive IDENTIFIER;

unaryOperator: OPERATOR primitiveItem
             | OPERATOR '(' expression ')';

binary: binary OPERATOR binaryOperand |
        binaryOperand OPERATOR binaryOperand;
binaryOperand: unary
             | primitive;

keyword: keywordArgument? (keywordName ':' keywordArgument)+;
keywordArgument: unary
               | binary
               | primitive;
keywordName: IDENTIFIER;

primitive: primitiveItem (',' primitiveItem)*?;
primitiveItem: IDENTIFIER
             | literal;

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
