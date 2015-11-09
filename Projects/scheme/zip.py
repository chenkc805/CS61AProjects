def zip(s):
	"""  Takes in a list of pairs and converts it into a pair of lists, 
	where the first list contains all of the first elements of the original pairs, 
	and the second list contains all of the second elements.

	>>> zip([[1,2]])
	[[1], [2]]
	>>> zip([[1,2],[3,4],[5,6]])
	[[1, 3, 5], [2, 4, 6]]
	"""
	if len(s) == 1:
		return [[s[0][0]],[s[0][1]]]
	else:
		return [[s[0][0]] + zip(s[1:])[0], [s[0][1]] + zip(s[1:])[1]]