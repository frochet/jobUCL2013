===================================
Labo X: Spanning Tree Protocol
===================================

Situation
---------


In this lab, you'll work on a network with switchs that uses the spanning tree protocol.This protocol allows switches to automatically disable ports on Ethernet switches to ensure that the network does not contain any cycle that could cause frames to loop forever.

Here is the topology of the network:

  .. figure:: ../../../png/labs/stp/topology.png
     :align: center
     :scale: 100


To use STP, these switches uses ``brctl``. A tool that allows to make bridges and build spanning tree.

Instructions
------------

The goal of this lab is to have a better understanding of STP. You'll have the possibility to watch how this protocol works.

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

To launch the lab you have to go in the directory of the lab and launch it with netkit using command ``lstart`` (you can add the option -f for a quick launch). 
You can see that the 6 machines are launched. For the moment, no one of them runs the stp. You will begin by run it on two routers and activate wireshark on one of them as explained above. To activate the STP on one switch type in his terminal:

 .. code:: console

    brctl stp br0 on
    ifconfig br0 up

With these two routers you can see what messages are exchanged for the root bridge election.
You can see the state of a bridge by typing :

 .. code:: console

    brctl showstp br0

this command give you information about the designated root of the tree, the root port of the switch and the cost to the root switch.


Launching the other switches
----------------------------

Now, we will launch some other switches. By doing that we change the topology. With wireshark you can observe the packets of the spanning tree protocol that are exchanged. The switches already launched will generate a "topology change notification", then others switches will acknowlegdes theses changes.


When all the switches are launched, you can look at the bridge state of each switches: 

 .. code:: console

    brctl showstp br0

You can see wich ports are in blocking state, wich are in forwarding state.
You can also look at the port-station table by entering :

 .. code:: console

    brctl showmacs br0

Tests
-----
Now it's time to play with the topology.

-
    Try to make some links fail and observe what is happening. You can do that by stoping one interface on a switch or the entire bridge (if=br0) :

 .. code:: console

    ifconfig IF down

where IF is the name of your interface.


Have fun!
