# Linked List 

#Constructor: 
def link(first, rest): 
 """Construct a linked list from its first element and the rest."""

#Selectors: 
def first(s): 
 """Return the first element of a linked list s."""

def rest(s): 
 """Return the rest of the elements of a linked list s."""

 link(1,2) # not ok
 link(1,empty)
 link(1,link(2,link(3,empty)))

 def extend(s,t):
 	"""Returns a linked list containing all elements of both linked list s and t."""
 	if s == empty:
 		return t
 	else:
 		return link(first(s), extend(rest(s),t))

 def apply_to_all_link(f,s):
 	if s == empty:
 		return empty
 	else:
 		return link(f(first(s)), apply_to_all_link(f,rest(s))

 def partitions(n,m):
 	"""Return a linked list of partitions of n using parts up to 2m. 
 	Partition is a linked list of numbers"""

 	if n==0:
 		return link(empty,empty)
 	elif n < 0 or m==0
 		return empty
 	else:
 		# Do I use m at least once?
 		yes = partitions(n-m,m)
 		no = partitions(n,m-1)
 		add_m = lambda s: link(m,s)
 		yes_with_m = apply_to_all_link(add_m,yes)
 		return extend(yes_with_m, no)

def print_partitions(n,m):
	lists = partitions(n,m)
	strings = apply_to_all_link(lambda s: join(s, ' + ', lists))
	print(join(strings, '/n')) # Separate into a new line

def join(s,separator):
	if s == empty:
		return ' '
	elif rest(s) == empty:
		return str(first(s))
	else:
		return str(first(s)) + separator + join(rest(s), separator)

def fib_tree(n):
	if n == 0 or n == 1:
		return rooted(n, [])
	else:
		left, right, fib_tree(n-2), fib_tree(n-1)
		root_value = root(left) + root(right)
		return rooted(root_value, [left,right])











