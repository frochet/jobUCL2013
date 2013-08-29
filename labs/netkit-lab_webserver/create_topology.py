
# This file is used to create topologies for the webserver lab.
#
#


import os
import sys
import getopt

def configure(onHosts):
    for host in onHosts:
        if host == "r":
	    create_router()
	elif host == "client1":
	    create_client1()
	elif host == "client2":
	    create_client2()
	elif host == "server":
	    create_server()
	

def create_router():
    f=open('r.startup','w')
    f.write('ifconfig eth0 2001:db8:0b0:15:da:b055::1/96 up\nifconfig eth1 2001:db8:be:600d::1/64 up\nsysctl -w net.ipv6.conf.all.forwarding=1\n')
    f.close()

def create_webserver():
    f=open('server.startup','w')
    f.write('ifconfig eth0 2001:db8:be:600d::2\n/etc/init.d/apache2 start\nroute -A inet6 add default gw 2001:DB8:be:600d::1')
    f.close()

def create_client2():
    f=open('client2.startup','w')
    f.write('ifconfig eth0 2001:db8:0b0:15:da:b055::3/96 up\nroute -A inet6 add default gw 2001:DB8:0b0:15:da:b055::1')
    f.close()

def create_client1():
    f=open('client1.startup','w')
    f.write('ifconfig eth0 2001:db8:0b0:15:da:b055::2/96 up\nroute -A inet6 add default gw 2001:DB8:0b0:15:da:b055::1')
    f.close()

def create_conf():
    f=open('lab.conf','w')
    f.write('LAB_DESCRIPTION="A lab showing problems that can occurs when using tcp protocol to download files on a webserver"\n LAB_VERSION=1\n LAB_AUTHOR="O. Bonaventure, J. Vellemans, F. Rochet"')
    f.write('client1[0]=A\nClient2[0]=A\nr[0]=A\nr[1]=B\nserver[0]=B')
    f.close()

#main function
def main(argv):
    create_conf()
    configure(["r", "server", "client1", "client2"])
    
if __name__=="__main__":
    main(sys.argv[1:])
