empty = 'empty' 

def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1]))
def link(first, rest): 
	return [first, rest] 
def first(s): 
	return s[0] 
def rest(s): 
	return s[1] 
def len_link(s): 
	x = 0
	while s != empty: 
		s, x = rest(s), x+1
	return x
def getitem_link(s, i): 
	while i > 0: 
		s, i = rest(s), i - 1
	return first(s) 
def extend(s, t):
	assert is_link(s) and is_link(t) 
	if s == empty: 
		return t 
	else: 
		return link(first(s), extend(rest(s), t))
def apply_to_all_link(f, s):
	if s == empty: 
		return s 
	else: 
		return link(f(first(s)), apply_to_all_link(f, rest(s)))

def keep_if_link(filter_fn, s): 
	if s == empty:
		return s
	elif filter_fn(first(s)):
		return link(first(s), keep_if_link(filter_fn, rest(s)))
	else:
		return keep_if_link(filter_fn, rest(s))

def partitions(n, m):
	if n == 0:
		return link(empty, empty) 
	elif n < 0: 
		return empty 
	elif m == 0: 
		return empty 
	else: 
		# Do I use at least one m?
		yes = partitions(n-m, m) 
		no = partitions(n, m-1) 
		add_m = lambda s: link(m, s) 
		yes = apply_to_all_link(add_m, yes) 
		return extend(yes, no) 

def list_partitions(n,m,max_length):
	a = partitions(n,m)
	return keep_if_link(lambda x: max_length >= len_link(x), a)


