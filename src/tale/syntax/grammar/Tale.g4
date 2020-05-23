grammar Tale;

program: (statement NEWLINE*)*;
statement: assignment | expression;


assignment: assignmentName '=' (expression | expressionInBrackets);
assignmentName: assignmentForm | IDENTIFIER;

assignmentForm: unaryForm
              | unaryOperatorForm
              | binaryForm
              | keywordForm
              | IDENTIFIER;

unaryForm: argument IDENTIFIER;

unaryOperatorForm: OPERATOR argument;

binaryForm: argument OPERATOR argument;

keywordForm: argument? (IDENTIFIER ':' argument)+;

argument: '(' argumentName (':' argumentType)? ')';
argumentName: IDENTIFIER;
argumentType: IDENTIFIER;


expression: unary
          | binary
          | keyword
          | primitive;
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
NEWLINE : [\r\n];