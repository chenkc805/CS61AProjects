# Sets as Unordered Sequences

# Proposal 1: A set is represented by a linked list that contains no duplicate items

# Sets implemented as linked lists with no repeats

def empty(s):
	return s is Link.empty

def set_contains(s,v):
	"""Return whether set s contains value v.

	>>> s = Link(1, Link(2, Link(3)))
	>>> set_contains(s,2)
	True
	"""
	if empty(s):
		return False
	elif s.first == v:
		return True
	else:
		return set_contains(s.rest, v)

def adjoin_set(s, v):
	if set_contains(s,v):
		return s
	else:
		return Link(v,s)

def intersect_set(set1, set2):
	in_set2 = lambda v: set_contains(set2, v)
	return keep_if(set1, in_set2)

def union_set(set1, set2):
	not_in_set2 = lambda v: not set_contains(set2, v)
	set1_not_set2 = keep_if(set1, not_in_set2)
	return extend(set1_not_set2, set2)

def extend(s, t):
	if s is Link.empty:
		return t
	else:
		return Link(s.first, extend(s.rest,t))

def keep_if(s,filter_fn):
	if s is Link.empty:
		return s
	else:
		kept = keep_if(s.rest, filter_fn)
		if filter_fn(s.first):
			return Link(s.first, kept)
		else:
			return kept

# Binary Tree Class

""" A binary tree is a tree that has a left branch and a right branch
	Every binary tree has exactly two branches
	No duplicates























