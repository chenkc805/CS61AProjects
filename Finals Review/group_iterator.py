class LazyList( object ):
	def __init__ ( self ):
		self._list = []
		self._computed_indices = set()
	def append ( self , item ):
		self._list.append ( item )
	def __getitem__ ( self , index ):
		if index not in self._computed_indices :
			self._computed_indices.add ( index )
			self._list [ index ] = self . _list[ index ]()
		return self._list [ index ]
	def __iter__( self ):
	for index in range ( len ( self._list )):
		yield self[ index ]

def mystery ( n ):
	s = LazyList()
	i = 0
	while i < n :
		s . append( lambda : i )
		i += 1
	return s
result = mystery(4)[1]

def group_iterator(orig):
	elem, lst, last = [], [], None
	for tups in orig:
		if last == None:
			elem = elem + [tups[1]]
			last = tups[0]
		if tups[0] == last:
			elem = elem + [tups[1]]
		else:
			lst = lst + [(last,elem)]
			elem = [] + [tups[1]]
			last = tups[0]
	lst = lst+[(last,elem)]
	return lst
