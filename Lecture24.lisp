"Lecture 24"

Primitive Expressions: 2, 3.3, true, + , quotient, ...
Combinations: (quotient 10 2), (not true)

Numbers are self-evaluating ; symbols are bound to values
Call expressions include an operator and 0 or more operands in parenthesis

ex)
> (quotient 10 2)
5

"quotient" names Scheme's built-in integer division procedure (i.e., function)
Combinations can span multiple lines (spacing does not matter)

There are no for and while statements, just recursion!

# Lambda expressions evaluate to anonymous procedures
(lambda (<formal-parameters>) <body>)

Two equivalent ways:
(define (plus4 x) (+ x 4))
(define puls4 (lambda (x) (+ x 4)))

"In the late 1950s, computer scientists used confusing names"

cons: Two-argument procedure that creates a pair
car: Procedure that returns the first element of a pair
cdr: Procedure that returns the second element of a pair
nil: The empty list

They also used a non-obvious notation for linked lists
> (define x (cons 1 2))
> x 
(1 . 2)
> (car x)
1 
> (cdr x)
2
> (cons 1 (cons 2 ( cons 3 (cons 4 nil))))
(1 2 3 4)

Quotation prevents evaluation












