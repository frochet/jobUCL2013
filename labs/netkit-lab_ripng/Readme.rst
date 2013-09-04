====================================
Labo X: Routing information protocol
====================================

Situation
---------


In this lab, you'll work on a network with routers that use RIPng to build their routing tables.

Here is the topology of the network:

  .. figure:: ../../png/labs/ripng/topology.png
     :align: center
     :scale: 100


To use RIP, these routers uses daemons called ``zebra`` and ``ripngd`` .

Instructions
------------

The goal of this lab is to have a better understanding of the rip protocol. You'll have the possibility to watch how this protocol work.

To launch the labs you have to execute the python scrypt "xx.py"

 .. code:: console

    python xx.py -option


Then, as usual, launch the lab with netkit using lstart.

Observations
------------
-
    When your lab is launched, try to ping the other routers. Did it works?

It's because the daemon is not launched yet. You can look at the routing table and see that there is not yet all the informations about the network.


Tests
-----
First of all launch the ripngd and zebra daemon. To do that, type on each router the command :

 .. code:: console

    /etc/.init.d/zebra start

After a while, all destinations are available. Why it's not instantaneous?

-
    Check routing tables. They should be all updated.

-
    sniff the rip packets using tcpdump and observe them. Is this consistent with your expectations?

 .. code:: console

    tcpdump -i any -v -s 1518

Note : -i option permits to choose an interface. -v permits to display all packet details -s permits to capture the entire ethernet packets (not only the first 68 bytes)


Now it's time to play with the topology.

-
    Try to make some links fail and observe what is happening. You can do that by stoping one interface on a router :

 .. code:: console

    ifconfig IF down

where IF is the name of your interface.

Obsere what's happening. Is the network recovering fast? Why?

The End
--------
When you have finished clean your directory by using :

 .. code:: console

    python xx.py -clean

Have fun!
