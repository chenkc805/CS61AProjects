# Lecture 35

# Distributed Computing
""" 
Multiple programs running on multiple computers that together 
coordinate to perform some task. 
"""

# Network Messages
"""
Computers communicate via messages: sequences of bytes transmitted
over a network.

Messages can serve many purposes:
Send data to another computersRequest data from another computer
Instruct a program to call a function on some arguments
Transfer a program to be executed by another computer.
"""

"""
Messages conform to a message protocol adopted by both the sender
and the receiver
"""

# Internet Protocol
"""
The Internet Protocol (IP) specifies how to transfer packets of data
among networks.

Networks are inherently unrelialbe at any point
The structure of a network is dynamic, not static
No system exists to monitor or track communications
"""

# Transmission Control Protocol
"""
Ordered, reliable transmission of arbitrary byte streams
Implemented using the IP. Every TCP connection involves sending IP
packets
Each packet in a TCP session has a sequence order 
* Receiver can correctly order packets
* Receiver can ignore duplicate packets
"""

# TCP Handshakes
"""
All TCP connections begin with a sequence of messages called a 'handshake'
which verifies that communication is possible

Handshake Goals:
Computer A knows it can send data to and receive data from Computer B 
Computer B knows it can send data to and receive data from Computer A 
Lots of separate connections can exist without any confusion
The number of required messages is minimized

Communication Rules
Computer A can send an initial messsage to Computer B request a new connection
Computer B can respond to A and vice versa
"""

# Client/Server Architecture
"""
In WWW, Web browser and Web server talk to each other. 
A web browser is an interpreter for a bunch of different programming languages
"""

# Peer-to-peer architecture
"""
Skype is a Voice Over IP (VOIP) system that uses a hybrid peer-to-peer architecture
Login and contacts are handled via a centralized server

Conversations between two computers that cannot send messages
to each other can send to a third party computer, a supernode. 
"""












