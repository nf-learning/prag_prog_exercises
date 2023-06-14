/**
* Thought about enforcing semantics within the grammar. E.g. 24 hour format can only
* take 1-23 for hours, and in am/pm format only 1-12 for hours. Started running into
* problems with lexer rules precedence and ambiguity since the presence or absence of
* the AMPM string needs to be known to determine which rule to apply. There may be a
* way to fix this once I learn more of ANTLR.
*/
grammar Time;
time:   hour am_pm
    |   hour ':' minute
    |   hour ':' minute am_pm
    ;

hour:  DIGIT
    |  DIGIT DIGIT
    ;

minute: DIGIT DIGIT;

am_pm: AM | PM;
AM: A M;
PM: P M;
DIGIT: [0-9];

fragment A: ('A' | 'a');
fragment M: 'M' | 'm';
fragment P: 'P' | 'p';

WS: [\r\n ]+ -> skip;

