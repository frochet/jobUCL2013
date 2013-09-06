
=================================
LABO 1: IPV6 network Instructions
=================================


In this lab, you will discover netkit, an emulator of networks. Here is given a
network configuration where 2 routers and 2 hosts are interconnected as you can
see below:
  .. figure:: labo1.png
     :align: center
     :scale: 100

Basic configuration is already done, interface and IP on each host are set. 
First, you will have to understand how works the ifconfig command.

 .. code:: console

    man ifconfig

Then you will have to create routes inside the network. To help you do that. Make a new sketch with address of the routers/computers on each interface. You can find them using the ifconfig commands.

To manipulate routes inside the network, use the command route. You can use this command in each virtual machine to manipulate routing tables.
Dont forget you are working with ipv6:

 .. code:: console

    route -6


After have set correctly all routes, you must be able to ping any machine in the network (use ping6)

Enjoy !
