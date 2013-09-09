===============================================
Labo X: The Dynamic Host Configuration Protocol
===============================================

Situation
---------


In this lab, you'll work on a network with one routers that use dhcpv6-server and 3 pcs that use dhcpv6 client.

Here is the topology of the network:

  .. figure:: ../../png/labs/dhcp/topology.png
     :align: center
     :scale: 100


To use dhcpv6, these machines uses daemons called ``dibbler``.

Instructions
------------

The goal of this lab is to have a better understanding of dhcp. You'll have the possibility to watch how this protocol works.

To launch the lab you have to go in the directory of the lab and launch it with netkit using "lstart -f". 
You can see that the 4 machines are launched. 

For this lab, you can use wireshark to see the packets exchanged between the clients and the server.

When the lab is launched, run the server daemon on the router, then run the client daemon on the pc's.

 .. code:: console

    /etc/init.d/dibbler-server start
    /etc/init.d/dibbler-client start


Observations
------------
-
    Why the server sends periodically multicast messages?

-
    What kinds of messages are exchanged between the server and the clients? (You should identify 4 different type)

Have fun!
