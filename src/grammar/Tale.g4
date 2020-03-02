grammar Tale;

program: (statement NEWLINE)+;
statement: expression;

expression: unary
          | binary
          | keyword
          | primitive;
expressionInBrackets: '(' expression ')';
expressionWithOperator: OPERATOR expressionInBrackets;

unary: unary IDENTIFIER
     | expressionWithOperator IDENTIFIER
     | expressionInBrackets IDENTIFIER
     | primitive IDENTIFIER;

binary: binary OPERATOR binaryOperand |
        binaryOperand OPERATOR binaryOperand;
binaryOperand: unary
             | primitive
             | expressionWithOperator
             | expressionInBrackets;

keyword: keywordPrefix* (keywordName ':' keywordValue)+;
keywordPrefix: unary
             | binary
             | primitive
             | expressionWithOperator
             | expressionInBrackets;
keywordName: IDENTIFIER;
keywordValue: unary
            | binary
            | primitive
            | expressionWithOperator
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
NEWLINE : [\r\n];
