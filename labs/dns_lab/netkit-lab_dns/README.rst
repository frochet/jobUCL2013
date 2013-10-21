=================================
LABO 2: DNS, BIND and IPv6
=================================

1. Starting Netkit
------------------

In order to run the Netkit network emulator, launch the following commands:

 .. code:: console
    
    ssh -Y <ingilogin>@permeke.info.ucl.ac.be
    export PATH=$PATH:/etinfo/applications/netkit/bin

To launch a single host instance, use the command vstart:

 .. code:: console
   
    vstart hostname

To launch the DNS lab, use the following command:

 .. code:: console
 
    cp -r /etinfo/applications/netkit/dnslab/ $HOME/	# do not forget the trailing /'s
    lstart -d $HOME/dnslab

To stop the lab, please stop all the involved instances by using the command "halt".

Also, cleanup the virtual disks when you are finished:

 .. code:: console

    rm -f $HOME/dnslab/\*.disk

2. Exploring DNS
----------------

In this lab, you will experiment on Domain Name system. You will perform queries through DNS server.

Below, you can find a graph where the DNS topology we will use is depicted.

  .. figure:: ../../../png/labs/dns/topo.png
     :align: center
     :scale: 100

To begin experimentation, launch the lab by running the commands explained above.

The configuration of the DNS server are already done. For this lab we ask you to find the IP address of the following fully qualified domain names (FQDN):

-
	pc2.nanoinside.net
-
	dnsorg.org
-
	dnsroot

You should use the command dig.

 .. code:: console

    dig @server -t type FQDN

If no server is specified, dig uses the default one that you can find in /etc/resolv.conf.

While doing these requests, observe the packets that are exchanged between the differents DNS server. Is this what you expected? Sketch the Question/response order on the figure below.

  .. figure:: ../../../png/labs/dns/topo.png
     :align: center
     :scale: 100

You have learnt that DNS can work in two ways: Forward and Reverse. We will now resolve IPv6 addresses into their corresponding DNS names.

Find the FQDN domain name of the following IPv6 addresses by asking the root server:

-
	2001:db8:ba1:b0a::22

-
	2001:db8:ba1:b0a::2

Again, you should use the dig command but with the -x option.

 .. code:: console

    dig @server -x ipv6

with ipv6 the IPv6 address you want to resolve.

3. Using DNS to access a website
--------------------------------

Now that you have played a bit with DNS, we will now try to add a DNS entry that will point to some IP address and setup a website that can be joined through the added DNS entry.

We will create the website on pc2 and we will call it helloworld.nanoinside.net. You thus have to add a DNS entry so that helloworld.nanoinside.net points to the IP address of pc2. See https://help.ubuntu.com/community/BIND9ServerHowto for a tutorial on bind9 configuration.

Once the DNS entry is set up, it is time to configure the web server. Apache2 is installed. See http://tuxtweaks.com/2009/07/how-to-configure-apache-linux/ for a tutorial. The final goal is to see "Hello world !" when accessing the website:

 .. code:: console

    $ curl -s helloworld.nanoinside.net
    Hello world !

The configuration files of apache are located in /etc/apache2/

Enjoy !
