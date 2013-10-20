=================================
LABO 2: DNS, BIND and IPV6
=================================

In this lab, you will experiment on Domain Name system. You will perform queries through DNS server.

Below, you can find a graph where the DNS topology we will use is depicted.

  .. figure:: ../../../png/labs/dns/topo.png
     :align: center
     :scale: 100

To begin experimentation. Go in the lab directory and launch the lab by using the command :

 .. code:: console

    lstart

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

If no server are specified, dig uses the default one that you can find in /etc/resolv.conf.
=======
If no server are specified, dig uses the default one that you can find in /etc/resolv.conf
>>>>>>> 9f6675a6a1a3fe7c32c18761ec845cd3a0292ebf

While doing these request, observe the packets that are exchanged between the differents DNS server. Is this what you expected? Sketch the Question/response order on the figure below.

  .. figure:: ../../../png/labs/dns/topo.png
     :align: center
     :scale: 100

You have learnt that DNS can work in two ways: Forward and Reverse. We will now resolve IPv6 addresses into their corresponding DNS names.
>>>>>>> 9f6675a6a1a3fe7c32c18761ec845cd3a0292ebf

<<<<<<< HEAD
Find the FQDN domain name of the following IPv6 addresses by asking the root server:
=======
Find the FQDN domain name of the following ipv6 addresses by asking to one name server:
>>>>>>> f2234aa9b2ab2e93ef9054c9541674a8421f3f81

-
	2001:db8:ba1:b0a::22

-
	2001:db8:ba1:b0a::2

Again, you should use the dig command but with the -x option.

 .. code:: console

    dig @server -x ipv6

with ipv6 the ipv6 address you want to resolve.


Enjoy !
