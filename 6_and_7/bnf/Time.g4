/**
* Thought about enforcing semantics within the grammar. E.g. 24 hour format can only
* take 1-23 for hours, and in am/pm format only 1-12 for hours. Started running into
* problems with lexer rules precedence and ambiguity since the presence or absence of
* the AMPM string needs to be known to determine which rule to apply. There may be a
* way to fix this once I learn more of ANTLR.
*/
grammar Time;
prog:   time EOF;
time:   hour AMPM
    |   hour ':' minute
    |   hour ':' minute AMPM
    ;

hour:  DIGIT
    |  DIGIT DIGIT
    ;

minute: DIGIT DIGIT;


DIGIT: [0-9];
AMPM:   'AM'|'am'
    |   'PM'|'pm'
    ;
WS: [\r\n ]+ -> skip;

