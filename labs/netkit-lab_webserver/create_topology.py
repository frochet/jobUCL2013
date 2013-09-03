
# This file is used to create topologies for the traceroute lab.
#
#

PREFIX="2001:db8:"

import os
import sys
import getopt

def configure(topo):
	    create_r1(topo)
	    create_r2(topo)
	    create_r3(topo)
	    create_r4(topo)

def create_r1(topo):
    os.makedirs(r1)
    f=open('r1.startup','w')
    f.write('ifconfig eth0 up \nifconfig eth0 add '+ global PREFIX + 'c001::1/48\nifconfig eth1 up\nifconfig eth1 add '+ global PREFIX + 'c001::2/48\nsysctl -w net.ipv6.conf.all.forwarding=1\nroute -A inet6 add default gw '+ global PREFIX + 'c001::3\necho "'+ global PREFIX + 'c001::3 r2" >> /etc/hosts\necho "'+ global PREFIX + 'cafe::2 r4" >> /etc/hosts\necho "'+ global PREFIX + '5afe::2 r3" >> /etc/hosts')
    f.close()

def create_r2(topo):
    os.makedirs(r2)
    f=open('r2.startup','w')
    f.write('ifconfig eth0 up \nifconfig eth0 add '+ global PREFIX + 'c001::3/48\nifconfig eth1 up\nifconfig eth1 add '+ global PREFIX + '5afe::1/48\nifconfig eth2 up\nifconfig eth2 add '+ global PREFIX + 'cafe::1/48\nsysctl -w net.ipv6.conf.all.forwarding=1\nroute -A inet6 add '+ global PREFIX + '5afe::/48 gw '+ global PREFIX + 'cafe::2\necho "'+ global PREFIX + 'c001::1 r1" >> /etc/hosts\necho "'+ global PREFIX + 'cafe::2 r4" >> /etc/hosts\necho "'+ global PREFIX + '5afe::2 r3" >> /etc/hosts')
    f.close()

def create_r3(topo):
    os.makedirs(r3)
    f=open('r3.startup','w')
    f.write('ifconfig eth0 up \nifconfig eth0 add '+ global PREFIX + '5afe::2/48\nsysctl -w net.ipv6.conf.all.forwarding=1\nroute -A inet6 add default gw '+ global PREFIX + '5afe::1\necho "'+ global PREFIX + 'c001::1 r1" >> /etc/hosts\necho "'+ global PREFIX + 'cafe::2 r4" >> /etc/hosts\necho "'+ global PREFIX + '5afe::1 r2" >> /etc/hosts')
    f.close()

def create_r4(topo):
    os.makedirs(r4)
    f=open('r4.startup','w')
    f.write('ifconfig eth0 up \nifconfig eth0 add '+ global PREFIX + 'cafe::2/48\nifconfig eth1 up\nifconfig eth1 add '+ global PREFIX + 'c001::4/48\nsysctl -w net.ipv6.conf.all.forwarding=1\nroute -A inet6 add '+ global PREFIX + '5afe::/48 gw '+ global PREFIX + 'cafe::1\necho "'+ global PREFIX + 'c001::1 r1" >> /etc/hosts\necho "'+ global PREFIX + 'cafe::1 r2" >> /etc/hosts\necho "'+ global PREFIX + '5afe::2 r3" >> /etc/hosts')
    f.close()

def create_conf(lab):
    f=open('lab.conf','w')
    f.write('LAB_DESCRIPTION="A lab where routers have bad route table. Use traceroute6 to correct them."\n LAB_VERSION=1\n LAB_AUTHOR="O. Bonaventure, J. Vellemans, F. Rochet"')
    if (lab<=19):
        f.write('r1[0]=A\nr1[1]=A\nr1[M]=64\nr2[0]=A\nr2[1]=C\nr2[2]=B\nr2[M]=64\nr3[0]=C\nr3[M]=64\nr4[0]=B\nr4[1]=A\nr4[M]=64')

    if (lab <=29):
        f.write('client1[0]=A\nClient2[0]=A\nr[0]=A\nr[1]=B\nserver[0]=B')
    f.close()

#main function
def main(argv):
    if argv[0] == "-A1" :
        create_conf(1)
        configure(1)
           
     
    elif argv[0] == "-B1":
        create_conf(2)
    
if __name__=="__main__":
    main(sys.argv[1:])
