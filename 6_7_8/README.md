# Exercise 6,7 and 8

## Exercise 6
Design a BNF grammar to parse a time specification. All of the following 
examples should be accepted.
4pm, 7:38pm, 23:42, 3:16, 3:16am

### Solution
[Time.g4](./bnf/Time.g4)

---

## Exercise 7 
Implement a parser for the BNF grammar using a PEG parser generator in the
language of your choice. Output should be an integer containing the number of
minutes past midnight.


### Solution
[Java](./java) solution using ANTLR Listener

### Execution
./gradlew test

## Exercise 8 
Implement the time parser using a scripting language and regular expressions


### Solution
[Python](./python) solution using regexes

### Execution
./python time_tests.py
