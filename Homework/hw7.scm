; CS 61A Fall 2014
; Name: Kevin Chen
; Login: cs61a-sj

(define (assert-equal value expression)
  (if (equal? value (eval expression))
    (print 'ok)
    (print (list 'for expression ':
                 'expected value
                 'but 'got (eval expression)))))

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  ; YOUR CODE HERE
  (car (cdr s)))

(define (caddr s)
  ; YOUR CODE HERE
  (car (cdr (cdr s))))

(define (test-car-cadr)
  (assert-equal (list 3 4) '(cddr '(1 2 3 4)))
  (assert-equal 2          '(cadr '(1 2 3 4)))
  (assert-equal 3          '(caddr '(1 2 3 4))))

(test-car-cadr)

(define (sign x)
  ; YOUR CODE HERE
  (cond
      ((< x 0)-1)
      ((= x 0)0)
      (else 1)))

(define (test-sign)
  (assert-equal -1 '(sign -42))
  (assert-equal 0  '(sign 0))
  (assert-equal 1  '(sign 42)))

(test-sign)

(define (gcd m n)
  ; YOUR CODE HERE
  (cond
    ((= m n) m)
    ((< m n) (gcd m (- n m)))
    ((> m n) (gcd n (- m n)))))

(define (test-gcd)
  (assert-equal 4 '(gcd 12 8))
  (assert-equal 4 '(gcd 12 16))
  (assert-equal 8 '(gcd 16 8))
  (assert-equal 6 '(gcd 24 42))
  (assert-equal 5 '(gcd 5 5)))

(test-gcd)

(define (square x) (* x x))

(define (pow b n)
  ; YOUR CODE HERE
  (cond
    ((= n 1)b)
    ((even? n) (pow (square b) (/ n 2) ))
    ((odd?  n) (* b (pow b (- n 1))))))

(define (test-pow)
  (assert-equal 1024 '(pow 2 10))
  (assert-equal 1000 '(pow 10 3))
  (assert-equal 243  '(pow 3 5)))

(test-pow)

(define (ordered? lst)
  ; YOUR CODE HERE
  (cond
    ( ( eq? (cdr lst) ()) 'true)
    ( (>= (car lst) (cadr lst)) 'false)
    ( else (ordered? (cdr lst)))))


(define (test-ordered?)
  (assert-equal true  '(ordered? '(1 2 3 4 5)))
  (assert-equal false '(ordered? '(1 5 2 4 3))))

(test-ordered?)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) false)
          ; YOUR CODE HERE
          ((> (car s) v) false)
          ((= (car s) v) true)
          (else (contains? (cdr s) v))
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return len(s) == 0
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define odds (list 3 5 7 9))

(define (test-contains)
    (assert-equal true '(contains? odds 3))
    (assert-equal true '(contains? odds 9))
    (assert-equal false '(contains? odds 6)))

(test-contains)

(define (append s v)
    (cond ((empty? s) (list v))
          ; YOUR CODE HERE
          ((contains? s v ) s)
          ((< v (car s)) (cons v s)) 
          (else (cons (car s) (append (cdr s) v)))
          ))

(define (test-append)
    (assert-equal '(2 3 5 7 9)  '(append odds 2))
    (assert-equal '(3 5 7 9)    '(append odds 5))
    (assert-equal '(3 5 6 7 9)  '(append odds 6))
    (assert-equal '(3 5 7 9 10) '(append odds 10)))

(test-append)

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          ; YOUR CODE HERE
          (else 
            (cond 
              ((= (car s) (car t)) 
                (cons (car s) (intersect (cdr s) (cdr t))))
              ((< (car s) (car t))
                (intersect (cdr s) t))
              ((> (car s) (car t))
                (intersect s (cdr t)))
            ))))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define eight (list 1 2 3 4 5 6 7 8))

(define (test-intersect)
    (assert-equal '(3 5) '(intersect odds (list 2 3 4 5)))
    (assert-equal '()    '(intersect odds (list 2 4 6 8)))
    (assert-equal '(3 5 7)   '(intersect odds eight)))

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          ; YOUR CODE HERE
          (else             
            (cond 
              ((contains? t (car s)) 
                (union (cdr s) t))
              (else
                (define t (append t (car s)))
                (union (cdr s) t))))))

(define (test-union)
    (assert-equal '(2 3 4 5 7 9)       '(union odds (list 2 3 4 5)))
    (assert-equal '(2 3 4 5 6 7 8 9)   '(union odds (list 2 4 6 8)))
    (assert-equal '(1 2 3 4 5 6 7 8 9) '(union odds eight)))

(test-intersect)
(test-union)


; Binary search trees

; A data abstraction for binary trees where nil represents the empty tree
(define (tree entry left right) (list entry left right))
(define (entry t) (car t))
(define (left t) (cadr t))
(define (right t) (caddr t))
(define (empty? s) (null? s))
(define (leaf entry) (tree entry nil nil))

(define (in? t v)
    (cond ((empty? t) false)
          ; YOUR CODE HERE
          (( = (entry t) v) true)
          (( < (entry t) v) (in? (right t) v))
          (( > (entry t) v) (in? (left  t) v))))

; Equivalent Python code, for your reference:
;
; def contains(s, v):
;     if s.is_empty:
;         return False
;     elif s.entry == v:
;         return True
;     elif s.entry < v:
;         return contains(s.right, v)
;     elif s.entry > v:
;         return contains(s.left, v)

(define odd-tree (tree 3 (leaf 1)
                         (tree 7 (leaf 5)
                                 (tree 9 nil (leaf 11)))))

(define (test-in?)
    (assert-equal true  '(in? odd-tree 1))
    (assert-equal false '(in? odd-tree 2))
    (assert-equal true  '(in? odd-tree 3))
    (assert-equal false '(in? odd-tree 4))
    (assert-equal true  '(in? odd-tree 5)))

(test-in?)

(define (as-list t)
    ; YOUR CODE HERE
     (cond ((null? t) nil)
      (else
        (union (union (as-list (left t)) (cons (entry t) nil)) (as-list (right t))))))
      

(define (test-as-list)
    (assert-equal '(5 7 9 11) '(as-list (right odd-tree)))
    (assert-equal '(1 3 5 7 9 11) '(as-list odd-tree)))

(test-as-list)


