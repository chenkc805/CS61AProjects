# Lecture 37

# Ambiguity
""" Syntactice Ambiguity in English
Programs must be written for people to read
"""

""" Representing Syntactic Structure
A Tree represents a phrase:
tag
barnches

A Leaf represents a since word:
tag 
word
"""

beasts = Leaf('N', 'buffalo')
intimidate = Leaf('V', 'buffalo')

s = Tree(S, [Tree(NP, [beasts]),
			 Tree(VP, [intimidate,
			 			Tree(NP, [beasts])])])

# Grammars 

def parse(line):

	def expand(start, end, tag):
		""" Yield all tress rooted by tag."""
		if end-start == 1:
			word = words[start]
			for leaf in lexicon:
				if tag == leaf.tag:
					yield leaf
		if tag in grammar:
			for tags in grammar[tag]:
				for branches in expands_all(tags):
					yield Tree(tag, branches)

	def expands_all(start, end, tags):
		""" Yield all sequences of branches for a sequence of tags."""
		if len(tags) == 1
			for branch in expands(tag[0]):
				yield [branch]
			else:
				first, rest = tags[0], tags[1:]
				for middle in range(start+1, end+1-len(rest)):
					for first_branch in expands(first):
						for rest_branches in expand_all(middle, end, rest):
							yield [first_branch] + rest_branches
	for tree in expand('S'):
		print_tree(tree)






