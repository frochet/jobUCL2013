====================================
Labo X: Routing information protocol
====================================

Situation
---------


In this lab, you'll work on a network with routers that use RIPng to build their routing tables.

Here is the topology of the network:

  .. figure:: ../../../png/labs/rip/topology.png
     :align: center
     :scale: 100


To use RIP, these routers use daemons called ``zebra`` and ``ripngd`` .

Instructions
------------

The goal of this lab is to have a better understanding of the rip protocol. You'll have the possibility to watch how this protocol works.

As usual, launch the lab with netkit using lstart, and use wireshark with the "sniffer"


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


Observations
------------
-
    When your lab is launched, try to ping the other routers (using ping6). Did it works?

It's because the daemon is not launched yet. You can look at the routing table and see that there is not yet all the informations about the network.


Tests
-----
First of all launch the ripngd and zebra daemon. To do that, type on each router the command :

 .. code:: console

    /etc/init.d/zebra start

After a while, all destinations are available. Why it's not instantaneous?

-
    Check routing tables. They should be all updated.

-
    sniff the rip packets using tcpdump & wireshark and observe them. Is this consistent with your expectations?


Note : -i option permits to choose an interface. -v permits to display all packet details -s permits to capture the entire ethernet packets (not only the first 68 bytes)


Now it's time to play with the topology.

-
    Try to make some links fail and observe what is happening. You can do that by stoping one interface on a router :

 .. code:: console

    ifconfig IF down

where IF is the name of your interface.

Obsere what's happening. Is the network recovering fast? Why?


Have fun!
