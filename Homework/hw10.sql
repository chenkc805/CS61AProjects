-- CS 61A Fall 2014
-- Name: Kevin Chen
-- Login: cs61a-sj

create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------


-- The names of all "toy" and "mini" dogs
create table size_classifications as
  select name, size from dogs, sizes
    where height > min and height <= max;

select name from size_classifications
  where size = "toy" or size = "mini";
-- Expected output:
--   abraham
--   eisenhower
--   fillmore
--   grover
--   herbert

-- All dogs with parents ordered by decreasing height of their parent
select child from dogs as a, parents as b where b.parent = a.name 
  order by -height;
-- Expected output:
--   herbert
--   fillmore
--   abraham
--   delano
--   grover
--   barack
--   clinton

-- Sentences about siblings that are the same size
with 
  siblings(s1, s2, size) as (
    select a.child as s1, b.child as s2, d.size
      from parents as a, parents as b, size_classifications as c, size_classifications as d
      where a.parent = b.parent and a.child < b.child and 
            c.name = a.child and d.name = b.child and c.size = d.size)
  select s1 || " and " || s2 || " are " || size || " siblings" from siblings;
-- Expected output:
--   barack and clinton are standard siblings
--   abraham and grover are toy siblings

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
with
  stack(list, count, sum, previous) as (
    select a.name, 1, height, a.height from dogs as a union
    select list || ", " || b.name, count+1, sum+height, b.height
    from dogs as b, stack where count < 4 and b.height > previous)
select list, sum from stack where count = 4 and sum >= 170 order by sum;
-- Expected output:
--   abraham, delano, clinton, barack|171
--   grover, delano, clinton, barack|173
--   herbert, delano, clinton, barack|176
--   fillmore, delano, clinton, barack|177
--   eisenhower, delano, clinton, barack|180

-- All non-parent relations ordered by height difference
create table ordered_set as 
with
  relation(ancestor, descendent, height_difference) as (
    select a.parent, b.child, c.height - d.height 
      from parents as a, parents as b, dogs as c, dogs as d
      where c.name = a.parent and d.name = b.child and a.child = b.parent union
    select parent, descendent, c.height - d.height
      from relation, parents, dogs as c, dogs as d
      where child = ancestor and parent = c.name and descendent = d.name
      )
select * from relation union
select descendent, ancestor, -height_difference from relation order by height_difference;

select ancestor, descendent from ordered_set;
-- Expected output:
--   fillmore|barack
--   eisenhower|barack
--   fillmore|clinton
--   eisenhower|clinton
--   eisenhower|delano
--   abraham|eisenhower
--   grover|eisenhower
--   herbert|eisenhower
--   herbert|fillmore
--   fillmore|herbert
--   eisenhower|herbert
--   eisenhower|grover
--   eisenhower|abraham
--   delano|eisenhower
--   clinton|eisenhower
--   clinton|fillmore
--   barack|eisenhower
--   barack|fillmore


