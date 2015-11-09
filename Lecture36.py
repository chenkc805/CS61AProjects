# Lecture 36

# Unix 
""" Computer Systems
Systems research enables the development of applications by defining and implementing abstractions:

* Operating systems provide a stable, consistent interface to unreliable, inconsistent hardware
* Networks provide a robust data transfer interface to constatly evolving communications infrastructure
* Databases provide a declarative interface to software that stores and retrieves information efficiently
* Distributed systems provide a unified interface to a cluster of multiple machines

A unifying property of effective systems:
** Hide complexity, but retain flexibility **
"""

""" The Unix Operating System
Essential features of the Unix operating systems
* Portability: The same operating system on different hardware
* Multi-tasking: many processes run concurrently on a machine
* Plain Text: Data is stored and shared in text format
* Modularity: small tools are composed flexibly via pipes

ls hw* | grep -v html | cut -d '.' -f 2 | sort -u 
"""

""" Python Programs in a Unix Environment
"""
try:
	while True:
		print("hw" + input())
except EOFError:
	pass

import sys

for line in sys.stdin:
    print(' '.join(line[:-1]))

# MapReduce
""" Big Data Processing
MapReduce is a framework for batch processing of big data
* Framework: A system used by programmers to build applications
* Batch processing: All the data is available at the outset, and results aren't used until processing completes
* Big Data: Used to describe data sets so large and comprehensive that they can reveal facts about a whole population,
usually from statistical analysis

The MapReduce idea:
* Data sets are too big to be analyzed by one machine
* Using multiple machines has the same complications, regardless of the application/analysis
* Pure functions enable an abstraction barrier
"""

""" MapReduce Evaluation Model
Map phase: Apply a mapper function to lal inputs, emitting intermediate key-value pairs
* The mapper takes an iterable value containing inputs, such as lines of text
* The napper yields zero or more key-vaule pairs for each input
"""

# MapReduce Execution Model
""" MapReduce Assumptions

Constraints on the mapper and reducer:
* The mapper must be equivalent to applying a deterministic pure function to each input independently
* The reducer must be equivalent to applying a deterministic pure function to the sequence of values for each key

Benefits of functional programming:
* Pure functions evaluate call expressions in order, lazily, in parallel
"""

# HADOOP
""" What does the HADOOP Framework Provide
Fault tolerance: A machine or hard drive might crash
* The MapReduce framework automatically re-runs failed tasks
Speed: Some machine might be slow because it is overloaded
* The framework can run multiple copies of a task and keep the result of the one that finishes first
Network locality
Monitoring














