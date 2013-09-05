============================
Labo X: Bad Routing Tables
============================

Situation
---------


In this lab, you'll work on a network that has some undefined problems. Using Traceroute :

 .. code:: console

    traceroute6 [IPv6]

where IPv6 is the address of the machine you want to know the route to.

Here is the topology of the network:

  .. figure:: ../../png/labs/traceroute/topology.png
     :align: center
     :scale: 100

Instructions
------------

The goal of this lab is to have a better understanding of  routing tables. You have to find the errors and correct them so all the routers can ping each others.

To launch the labs you have to execute the python scrypt "create-topology.py"

 .. code:: console

    python create-topology.py -option

There is three differents challenge. Use option -A1 , -A2, or -A3 to get one of them.
As usual launch the lab with netkit using lstart.

When you have finished with one, clean your directory by using :

 .. code:: console

    python create-topology.py -clean

and relaunch another.

Have fun!
