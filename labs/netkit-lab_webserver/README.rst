============================
Labo 2: Hack on tcp behavior
============================


Situation
---------


In this lab, you will find 2 hosts connected to a router. Behind this router
there is a webserver on a different collision domain than the hosts.
On the webserver, you have files you can download. The router has a fixed
maximum  bandwidth of 1 Mb/s, do not change it.

TODO: Image here


Instructions
------------


The goal of this lab is to have a better understanding of TCP by modifiyng its
options. You will have to analyse tcpdump traces of your download (man tcpdump) with tcptrace (http://www.tcptrace.org/manual.html)
and makes some conclusion about the value given to some particular options.
tcp is highly modifiable, and as you will see, some change can improve network
performance or lose network performance.

To modify tcp options, use the python script set_tcp_options.py. You can print
the help with the command python set_tcp_options.py -h

After that the tcp options have been set as you want, you can start netkit.
Each hosts will be configured as you requested.
