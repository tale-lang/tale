grammar Tale;

// Root.
program: (statement NEWLINE)+;
statement: expression;

// Expression.
expression: unary
          | binary
          | keyword
          | primitive;
expressionInBrackets: '(' expression ')';
expressionInBracketsWithOperator: OPERATOR expressionInBrackets;

// Unary.
unary: unary IDENTIFIER
     | expressionInBracketsWithOperator IDENTIFIER
     | expressionInBrackets IDENTIFIER
     | primitive IDENTIFIER;

// Binary.
binary: binary OPERATOR binaryOperand |
        binaryOperand OPERATOR binaryOperand;
binaryOperand: unary
             | primitive
             | expressionInBracketsWithOperator
             | expressionInBrackets;

// Keyword.
keyword: keywordPrefix* (keywordName ':' keywordValue)+;
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

// Primitive.
primitive: primitiveWithOperator
         | IDENTIFIER
         | NUMBER;
primitiveWithOperator: OPERATOR IDENTIFIER
                     | OPERATOR NUMBER;

// Tokens.
IDENTIFIER: [a-zA-Z]+;
NUMBER: [0-9]+;
OPERATOR: '-'
        | '+'
        | '*'
        | '/';

WS: [ \t]+ -> skip;
NEWLINE : [\r\n];
