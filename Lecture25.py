""" Today's Topic: Handling Errors """

Exceptions:
A built in mechanism in a programming language to declare and respond to exceptional conditions

Python raises an exception whenever an error occurs

Exceptions can be handled by the program, preventing the interpreter from halting

Unhandled exceptions will cause Python to half execution and print a stack trace.

Mastering Exceptions:
Exceptions are objects! They have classes with constructors
They enable non-local continuations of control
Steps can be skipped when you raise exceptions

Assert statements raise an exception of type AssertionError
asser <expression>, <string>

Whether assertions are enabled is governed by a bool __debug__

""" Raise Statements """
Exceptions are raised with a raise statement
raise <expression>

Exceptions are constructed like any other object. Eg TypeError('Bad argument!')
TypeError -- A function was passed the wrong number/type of argument
NameError -- A name wasnt found
KeyError -- No key found in dictionary
RuntimeError -- Recursion depth exceeded

""" Try Statements """
try:
	<try suite>
except <exception class> as <name>:
	<except suite>

""" Interpreters """ 
A Scheme list is written as elements in parentheses:
The task of pasing a language involves coercing a string representation of an expression to the expression itself
Parsers must validate that expressions are well-formed
