# Local Tables
"""
A create table statement names a table globally
A with clause of a select statement names a table that is local to the statement
"""

create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table parents as 
	select "abraham" as parent, "barack" as child union
	...
with 
	best(dog) as (
		select "eisenhower" union
		select "barack"
	)
select parent from parents, best where child=dog;

"""
parents is a global table
best is a local table, it
"""

# Local Tables can be Declared Recursively

"""
An ancestor is your parent or an ancestor of your parent
"""

with
	ancestors(ancestor, descendent) as (
	select ancestor, child
		from ancestor, parents
		where parent = descendent
	)
select ancestor from ancestors where descendent = "herbert" ;

To create a table with a global name, you need to select the contents of the local table

create table odds as 
	with 
		odds(n) as (
			select 1 union
			select n+2 from odds where n <15
		)
	select n from odds

"""Which names above can change without affecting the result?"""

# Limits on Recursive Select Statements

"""
Recurisve table definitions are only possible within a with clause
No mutual recursion: two or more tables cannot be defined in terms of each other
No tree recursion: the table being defined can only appear once in a from clause
"""

# Language is Recursive
"""
Noun phrases can contain relative pronouns that introduce relative clauses
"""













