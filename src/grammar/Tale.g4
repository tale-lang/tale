grammar Tale;

r: statement+;
statement: assignment;

assignment: name '=' body;
name: IDENTIFIER;
body: IDENTIFIER | NUMBER;

IDENTIFIER: [a-z]+;
NUMBER: [0-9]+;
WS: [ \t\r\n]+ -> skip;