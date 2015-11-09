# Dynamic Scope

"""
Scope refers to the envinroment in which you're going to look up names, create names, etc.

Scheme and Python looks up names by lexical scope (or static scope)

Lexical scope: The parent of a frame is the environment in which a procedure was defined.
Dynamic scope: The parent of a frame is the environment in which a procedure was called.

mu: Special form to create dynamically scoped procedures.
"""

# Tail Recursion
"""
All functions are pure functions
No re-assignment and no mutable data types
Name-value bindings are permanent

Advantages of functional programming:
* The value of an expression is independent of the orderin which sub-expressions are evaluated
* Sub-expressions can safely be evaluated in parallel or on demand (lazily).
* Referential Transparency: The value of an expression does not change when we substitute one of 
  its subexpressions with the value of that subexpression.

But no for/while statements! Can we make basic iteration efficient? Yes!
"""

def factorial(n,k): # Linear time, Linear space
	if n == 0:
		return k
	else: 
		return factorial(n-1, k*n)

def factorial(n,k): # Linear time, constant space. Iterative is better
	while n>0:
		n,k = n-1, k*n
	return k 

""" 
We want a properly tail recursed language in which recursion runs as efficiently as iteration. 
For example, recursive factorial has frames we don't need to keep around.
"""

# Tail Calls
"""
A procedure call that has not yet returned is active. Some procedue calls are tail calls.
A Scheme interpreter should support an unbounded number of active tail calls using only a constant amount of space.

A tail call is a call expression in a tail context:
* The last obdy sub-expression in a lambda expression # (IMPORTANT)
* Sub-expressions 2&3 in a tail context if expression # (IMPORTANT)
* All non-predicate sub-expressions in a tail context cond
* The last sub-expression in a tail context and or or 
* The last sub-expression in a tail context begin

A call expression is not a tail call if more computation is still required in the calling procedure
Linear recursive procedures can often be re-written to use tail calls
Operand in call expression is not a tail context
"""

(define (reduce procedure s start)
  (if (null? s) start
  	(cdr s)
  	(procedure start (car s))))

(reduce * '(3 4 5)' 2)
(reduce (lambda (x y) (cons y x)) )











