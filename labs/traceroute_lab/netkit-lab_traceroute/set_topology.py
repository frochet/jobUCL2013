
# This file is used to create topologies for the traceroute lab.
#
#

PREFIX="2001:db8:"

import os
import sys
import getopt

def clean():
    filelist= [f for f in os.listdir(".") if f.startswith("r")]
    for f in filelist:
        if os.path.isdir(f):
            os.removedirs(f)
        else:
            os.remove(f)
    
    os.remove('lab.conf')

def configure(topo):
	    create_r1(topo)
	    create_r2(topo)
	    create_r3(topo)
	    create_r4(topo)

def create_r1(topo):
    global PREFIX
    os.makedirs('r1')
    f=open('r1.startup','w')
    f.write('ifconfig eth0 up \nifconfig eth0 add ' + PREFIX + 'c001::1/48\nifconfig eth1 up\nifconfig eth1 add ' + PREFIX + 'c001::2/48\nsysctl -w net.ipv6.conf.all.forwarding=1\nroute -A inet6 add default gw '+ PREFIX + 'c001::3\necho "' + PREFIX + 'c001::3 r2" >> /etc/hosts\necho "' + PREFIX + 'cafe::2 r4" >> /etc/hosts\necho "' + PREFIX + '5afe::2 r3" >> /etc/hosts')
    f.close()

def create_r2(topo):
    global PREFIX
    os.makedirs('r2')
    f=open('r2.startup','w')
    if topo == 1 or topo == 13:
        f.write('ifconfig eth0 up \nifconfig eth0 add '+ PREFIX + 'c001::3/48\nifconfig eth1 up\nifconfig eth1 add '+ PREFIX + '5afe::1/48\nifconfig eth2 up\nifconfig eth2 add '+ PREFIX + 'cafe::1/48\nsysctl -w net.ipv6.conf.all.forwarding=1\nroute -A inet6 add '+ PREFIX + '5afe::/48 gw '+ PREFIX + 'cafe::2\necho "'+ PREFIX + 'c001::1 r1" >> /etc/hosts\necho "'+ PREFIX + 'cafe::2 r4" >> /etc/hosts\necho "'+ PREFIX + '5afe::2 r3" >> /etc/hosts')
    if topo == 12:
        f.write('ifconfig eth0 up \nifconfig eth0 add '+ PREFIX + 'c001::3/48\nifconfig eth1 up\nifconfig eth1 add '+ PREFIX + '5afe::1/48\nsysctl -w net.ipv6.conf.all.forwarding=1\nroute -A inet6 add '+ PREFIX + '5afe::/48 gw '+ PREFIX + 'cafe::2\necho "'+ PREFIX + 'c001::1 r1" >> /etc/hosts\necho "'+ PREFIX + 'cafe::2 r4" >> /etc/hosts\necho "'+ PREFIX + '5afe::2 r3" >> /etc/hosts')
    f.close()

def create_r3(topo):
    global PREFIX
    os.makedirs('r3')
    f=open('r3.startup','w')
    f.write('ifconfig eth0 up \nifconfig eth0 add '+ PREFIX + '5afe::2/48\nsysctl -w net.ipv6.conf.all.forwarding=1\nroute -A inet6 add default gw '+ PREFIX + '5afe::1\necho "'+ PREFIX + 'c001::1 r1" >> /etc/hosts\necho "'+ PREFIX + 'cafe::2 r4" >> /etc/hosts\necho "'+ PREFIX + '5afe::1 r2" >> /etc/hosts')
    f.close()

def create_r4(topo):
    global PREFIX
    os.makedirs('r4')
    f=open('r4.startup','w')
    if topo==1:
        f.write('ifconfig eth0 up \nifconfig eth0 add '+ PREFIX + 'cafe::2/48\nifconfig eth1 up\nifconfig eth1 add '+ PREFIX + 'c001::4/48\nsysctl -w net.ipv6.conf.all.forwarding=1\nroute -A inet6 add '+ PREFIX + '5afe::/48 gw '+ PREFIX + 'c001::2\necho "'+ PREFIX + 'c001::1 r1" >> /etc/hosts\necho "'+ PREFIX + 'cafe::1 r2" >> /etc/hosts\necho "'+ PREFIX + '5afe::2 r3" >> /etc/hosts')
    elif topo == 13:
        f.write('ifconfig eth0 up \nifconfig eth0 add '+ PREFIX + 'cafe::2/48\nifconfig eth1 up\nifconfig eth1 add '+ PREFIX + 'c001::4/48\nsysctl -w net.ipv6.conf.all.forwarding=1\nroute -A inet6 add '+ PREFIX + '5afe::/48 gw '+ PREFIX + 'cafe::1\necho "'+ PREFIX + 'c001::1 r1" >> /etc/hosts\necho "'+ PREFIX + 'cafe::1 r2" >> /etc/hosts\necho "'+ PREFIX + '5afe::2 r3" >> /etc/hosts')
    f.close()

def create_conf(lab):
    f=open('lab.conf','w')
    f.write('LAB_DESCRIPTION="A lab where routers have bad route table. Use traceroute6 to correct them."\n LAB_VERSION=1\n LAB_AUTHOR="O. Bonaventure, J. Vellemans, F. Rochet"')
    if (lab<=19):
        f.write('r1[0]=A\nr1[1]=A\nr1[M]=64\nr2[0]=A\nr2[1]=C\nr2[2]=B\nr2[M]=64\nr3[0]=C\nr3[M]=64\nr4[0]=B\nr4[1]=A\nr4[M]=64')

    elif (lab <=29):
        f.write('client1[0]=A\nClient2[0]=A\nr[0]=A\nr[1]=B\nserver[0]=B')
    f.close()

def usage():

  print "This script can set up 3 differents topologies. \n";
  print "Try python set_topology.py [option] where option can be -A1 or -A2 or -A3"


#main function
def main(argv):
    if argv[0] == "-A1" :
        create_conf(1)
        configure(1)
           
     
    elif argv[0] == "-A2":
        create_conf(12)
        configure(12)
    
    elif argv[0] == "-A3":
        create_conf(13)
        configure(13)

    elif argv[0] == "-clean":
        clean()
    
    elif argv[0] == "-h":
      usage()
    else:
      print "wrong usage \n"
      usage();

if __name__=="__main__":
    main(sys.argv[1:])
