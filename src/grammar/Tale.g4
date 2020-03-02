grammar Tale;

program: (statement NEWLINE)+;
statement: expression;

expression: unary
          | binary
          | keyword
          | primitive;

unary: unary IDENTIFIER
     | OPERATOR '(' expression ')'
     | '(' expression ')' IDENTIFIER
     | primitive IDENTIFIER;

binary: binary OPERATOR binaryOperand |
        binaryOperand OPERATOR binaryOperand;
binaryOperand: unary
             | primitive
             | OPERATOR '(' expression ')'
             | '(' expression ')';

keyword: (keywordName ':' keywordValue)+;
keywordName: IDENTIFIER;
keywordValue: unary
            | binary
            | primitive
            | OPERATOR '(' expression ')'
            | '(' expression ')';

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
NEWLINE : [\r\n];