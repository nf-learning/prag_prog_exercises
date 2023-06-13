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

