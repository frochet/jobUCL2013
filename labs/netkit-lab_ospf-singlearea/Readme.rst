===================================
Labo X: Open Shortest Path First v3
===================================

Situation
---------


In this lab, you'll work on a network with routers that use OSPFv3 to build their routing tables.

Here is the topology of the network:

  .. figure:: ../../png/labs/ospf/topology.png
     :align: center
     :scale: 100


To use OSPF, theses routers uses daemons called ``zebra`` and ``ospf6d`` .

Instructions
------------

The goal of this lab is to have a better understanding of OSPF. You'll have the possibility to watch how this protocol work.

To launch the labs you have to execute the python scrypt "xx.py"

 .. code:: console

    python xx.py -option


Then, as usual, launch the lab with netkit using lstart.

Observations
------------

-
    When your lab is launched, try to ping the other routers. Did it works immediately? Why?

-
    Perform traceroutes from/to different interfaces. 
    Think about the path the traceroute is expected to take, and the path ICMP replies are expected to take.
    Does the traceroute confirm your expetations?

Now we will access the ospf6d daemon. This will help us to see the ospf database, neighbor and route.

In netkit, type :

 .. code:: console

    telnet ::1 ospf6d

Reminder: "::1" is ipv6 address for localhost. ospf6d is the daemon our router use for ofps.

A password is asked, "zebra" should work.

Now you can ask some cool stuff at the ospf daemon:

 .. code:: console

    show ipv6 ospf6 database
    show ipv6 ospf6 neighbor
    show ipv6 ospf6 route
    show ipv6 ospf6 interface
    exit

-
    Is the lsdb the same for all routers? should it be?

-
    Observe the neighbor, you can find information about the Designated Router.


Tests
-----
Now it's time to play with the topology.

-
    Try to make some links fail and observe what is happening. You can do that by stoping one interface on a router :

 .. code:: console

    ifconfig IF down

where IF is the name of your interface.

-
    When you are in the daemon, change link cost and try some traceroute.

 .. code:: console

    interface IF
    ospf6 cost X

where IF is the interface and X the new cost.

The End
--------
When you have finished clean your directory by using :

 .. code:: console

    python xx.py -clean

Have fun!
