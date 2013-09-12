===================================
Labo X: Open Shortest Path First v3
===================================

Situation
---------


In this lab, you'll work on a network with routers that use OSPFv3 to build their routing tables.

Here is the topology of the network:

  .. figure:: ../../../png/labs/ospfnord/topology.png
     :align: center
     :scale: 100


To use OSPF, these routers uses daemons called ``zebra`` and ``ospf6d`` .

Instructions
------------

The goal of this lab is to have a better understanding of OSPF. You'll have the possibility to watch how this protocol works.

To launch the lab you have to go in the directory of the lab and launch it with netkit using lstart. 
You can see that the 5 machines are launched. For the moment, if you try to ping6 from a router to a non adjacent one, you'll see a destination unreachable. It's because the ospf deamon is not launched yet.

For this lab, you will use the "Wireshark" tool. It's a packet sniffer (like tcpdump) but it is more convenient to use.

To install it (under debian):

 .. code:: console

    sudo apt-get install wireshark

To use it with netkit :

    When you have launched a lab, you can access to your home directory or the lab directory from a netkit machine. These directories are located in ``/hosthome`` and ``/hostlab`` in netkit. Go in that directory :

 .. code:: console

    cd /hostlab

Now we will launch a tcpdump capture that we will save on a file in our hostlab(or hosthome) directory (option -w). This will permits us to start a capture from this file with wireshark.

 .. code:: console

    tcpdump -n -i IF -w aaa.pcap &

where aaa.out is our output file, IF the interface we want to listen on (any for all interfaces) and we add the "&" symbol so we can continue to work in the netkit shell.

Now we can launch wireshark on our computer with the input file aaa.out. You can do that with :

 .. code:: console

    wireshark -k -i<(tail -f aaa.pcap)&


Launching the daemon
--------------------

We will launch the daemon on each router one by one. This will permits us to carefully look at the exchanged packets between the different routers. (It's the good moment to launch wireshark)

Launch first the daemon on bb1. To do that enter the following command line in the bb1 terminal :

 .. code:: console

    /etc/init.d/zebra start

Then launch the daemon on bb2. 
-
	What packets are exchanged? 

-
    Have the routing tables changed?

Launch now the deamon on the others routers while looking on the exchanged packet.

-
    Perform traceroutes from/to different interfaces. 
    Think about the path the traceroute is expected to take, and the path ICMP replies are expected to take.
    Does the traceroute confirm your expetations?

Now we will access the ospf6d daemon. This will help us to see the ospf database, neighbor and route.

In netkit, type :

 .. code:: console

    telnet ::1 ospf6d

Reminder: "::1" is ipv6 address for localhost. ospf6d is the daemon our router use for ospf.

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


Tests
-----
Now it's time to play with the topology.

-
    Try to make some links fail and observe what is happening. You can do that by stoping one interface on a router :

 .. code:: console

    ifconfig IF down

where IF is the name of your interface.

-
    When you are in the daemon (telnet ::1 ospf6d) , change link cost and try some traceroute. Below, the line you should enter in your console:

 .. code:: console

    telnet ::1 ospf6d
    zebra
    enable
    configure terminal
    router ospf6
    interface IF
    ipv6 ospf6 cost X

where IF is the interface and X the new cost.


Have fun!
