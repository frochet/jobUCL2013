
# This file is used to create topologies for the webserver lab.
#
#


import os
import sys
import getopt

def create_router():
    pass

def create_webserver():
    pass

def create_hosts(hostnames):
    pass

def create_basic_topology():
    f=open('client1.startup','w')
    f.write('ifconfig eth0 2001:db8:0b0:15:da:b055::2/96 up\nroute -A inet6 add default gw 2001:DB8:0b0:15:da:b055::1')
    f.close()
    f=open('client2.startup','w')
    f.write('ifconfig eth0 2001:db8:0b0:15:da:b055::3/96 up\nroute -A inet6 add default gw 2001:DB8:0b0:15:da:b055::1')
    f.close()
    f=open('server.startup','w')
    f.write('ifconfig eth0 2001:db8:be:600d::2\n/etc/init.d/apache2 start\nroute -A inet6 add default gw 2001:DB8:be:600d::1')
    f.close()
    f=open('r.startup','w')
    f.write('ifconfig eth0 2001:db8:0b0:15:da:b055::1/96 up\nifconfig eth1 2001:db8:be:600d::1/64 up\nsysctl -w net.ipv6.conf.all.forwarding=1\n')
    f.close()
    f=open('lab.conf','w')
    f.write('LAB_DESCRIPTION="A lab showing problems that can occurs when using tcp protocol to download files on a webserver"\n LAB_VERSION=1\n LAB_AUTHOR="O. Bonaventure, J. Vellemans, F. Rochet"')
    f.write('client1[0]=A\nClient2[0]=A\nr[0]=A\nr[1]=B\nserver[0]=B')
    f.close()

#main function
def main(argv):
    create_basic_topology()
    
if __name__=="__main__":
    main(sys.argv[1:])
