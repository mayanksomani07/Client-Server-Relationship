# Server-Client-Communication-using-socket-programming


The program is developed and tested in Ubuntu 18.04 and expected to work in
Ubuntu 16+. Following method is described for these OS only.


In order to execute the program Tkinter modules of python is required.

run ApplicationS.py and ApplicationC.py using following commands

$ python3 applicationC.py
$ python3 applicationC.py

This starts GUI application of Chat application as Server and Client.

In server GUI, enter a port number greater than 1024 (say 1026) as ports below them are reserved and press "Connect".

In Client GUI, enter the IP address of server (127.0.0.1 if server and client are on same computer) and port number. Then press Connect.

On successful connection. It will display log message on Server GUI.

Now after successful connection between both system, message can be entered in either server's or client's text box and press send. 

Messages will be displayed on the message box.

OBJECTIVE
Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while other socket reaches out to the other to form a connection. Server forms the listener socket while client reaches out to the server. They are the real backbones behind web browsing. In simpler terms there is a server and a client. 
Objective of this assignment is to build a duplex chat application using socket programming in python.
So we will design both server and client model so that each can communicate with them. The steps can be considered like this.

    Python socket server program executes at first and wait for any request
    Python socket client program will initiate the conversation at first.
    Then server program will response accordingly to client requests.
    Client program will terminate if user exits. 
    Server program will also terminate when client program terminates, this is optional and we can keep server program running indefinitely or terminate with some specific command in client request.


METHODOLOGY

A _thread module & threading module is used for multi-threading in python, these modules help in synchronization and provide a lock to a thread in use.

from _thread import *
import threading

A lock object is created by->

print_lock = threading.Lock()

A lock has two states, “locked” or “unlocked”. It has two basic methods acquire() and release(). When the state is unlocked print_lock.acquire() is used to change state to locked and print_lock.release() is used to change state to unlock.

The function thread.start_new_thread() is used to start a new thread and return its identifier. The first argument is the function to call and its second argument is a tuple containing the positional list of arguments.

Socket programming is started by importing the socket library and making a simple socket.

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Here we made a socket instance and passed it two parameters. The first parameter is AF_INET and the second one is SOCK_STREAM. AF_INET refers to the address family ipv4. The SOCK_STREAM means connection oriented TCP protocol.


IMAGES
https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fis0dvil.files.wordpress.com%2F2010%2F01%2Fsocket_2.png&f=1&nofb=1
