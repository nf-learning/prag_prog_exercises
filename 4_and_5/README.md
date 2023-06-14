# Exercise 4 & 5

## Exercise 4
We want to implement a mini-language to control a turtle-graphics system. The language consists of single-letter commands, some followed by a simple number.
For example the following input would draw a rectangle:

P 2 # select pen 2
D   # pen down
W 2 # draw west 2cm
N 1 # then north 1
E 2 # then east 2
S 1 # then back south
U   # pen up

Implement the code that parses this language. It should be designed so that it is simple to add new commands

(Ex 5)  - Implement it again as an internal language
---

## Solution
Peg grammar to return an object with the parsed command and arguments

## Execution
npm test
