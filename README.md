This folder contains the simulation of a 6 dof robotic arm remote controller. The main idea of this project is to control a system in a remote way using networks. In this case I use the loopback IP (to simplify the problem), running in the 8891 port, to create the socket between the client and a server which is sopose to be running on the same place where the robot is. 

The main folder contains two subfolders:
* __Server_python:__ all the algorithms of this folder are made on python language. There are all the methods necesaries to run the server and also to control the robot on a local way if you want.
* __xmlrpc_client_c++:__ all the algorithms of this folder are made on c++ language. There are all the methods necesaries to control de robotic arm on the remote way. The clien must connect to the server previusly deployed on the port 8891 to make a succesful control.

This project could be done with the help of the teacher, Engeneer Specialist Cesar Aranda, who particularly helped with the development of the xmlrp_client.
