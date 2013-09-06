===============================
Labo X: Border Gateway Protocol
===============================

Situation
---------


In this lab, you'll work on a network with routers that use border gateway protocol.

Here is the topology of the network:

  .. figure:: ../../png/labs/bgp/topology.png
     :align: center
     :scale: 100


To use bgp, these routers uses daemons called ``zebra`` and ``bgpd`` .

Instructions
------------

The goal of this lab is to have a better understanding of bgp. You'll have the possibility to watch how this protocol works.

To launch the lab you have to go in the directory of the lab and launch it with netkit using lstart. 
You can see that the 8 machines are launched. 

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

    tcpdump -n -i IF -w aaa.out &

where aaa.out is our output file, IF the interface we want to listen on (any for all interfaces) and we add the "&" symbol so we can continue to work in the netkit shell.

Now we can launch wireshark on our computer with the input file aaa.out. You can do that with :

 .. code:: console

    wireshark -k -i<(tail -f aaa.out)&


Observations
------------

If you look at the routing table of the routers, you can see that they all have an entry for their subnetworks and for the network shared by r9 with the nexthop defined. But they have no knowledge of the others subnetworks and routers.

You can have more advanced informations about how bgp runs on the routers by connecting the daemon.

 .. code:: console

    telnet localhost bgpd

password is zebra as usual.

In this terminal you can use:

 .. code:: console

    show ip bgp neighbors
    show ip community-list
    show ip bgp summary

to get more infos.


Analyzing the configuration
---------------------------

If you look in the folders of the routers in the lab, you can find the configurations files of the differents daemons. For example, take a look at r1 configuration. You can find 3 files in ``lab/r1/etc/quagga``. 
The first one is ``daemons``:
This file contains informations about wich daemon should be started on our router.

The second one is ``zebra.conf``
This file contains the password that we use to connect to the zebra daemon when we are on the router. (the password asked when we type ``telnet localhost zebra``)

The third one is ``bgpd.conf``:
This is the configuration file of our bgpd daemon. Let's see what all these lines means.

  .. figure:: ../../png/labs/bgp/bgpdconf.png
     :align: center
     :scale: 100

Knowing that, you should be able to play with the topology and even create new routers that use bgp. Try some different configurations, try to change how the filters work and observe what's happening.

Tests
-----
Now it's time to play with the topology.

-
    Try to make some links fail and observe what is happening. You can do that by stoping one interface on a router :

 .. code:: console

    ifconfig IF down

where IF is the name of your interface.

-
    When you are in the daemon (telnet localhost bgpd).

 .. code:: console

    interface IF
    ospf6 cost X

where IF is the interface and X the new cost.


Have fun!
