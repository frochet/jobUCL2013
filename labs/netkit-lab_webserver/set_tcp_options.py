#!/usr/bin/env python
#coding=utf-8
#
#Script to modify tcp options in netkit
#
#indentation in 4 espace

import os
import sys
import getopt
import create_topology

tcp_options = dict()


def parse_option():
    pass

def default():
    global tcp_options
    tcp_options['tcp_abc'] = 0
    tcp_options['tcp_abort_on_overflow']= False
    tcp_options['tcp_adv_win_scale'] = 2
    #tcp_options['tcp_allowed_congestion_control']="reno"
    #tcp_options['tcp_available_congestion_control']
    tcp_options['tcp_app_win'] = 31
    tcp_options['tcp_base_mss'] = 512
    tcp_options['tcp_bic']=False
    tcp_options['tcp_bic_low_window']=14



def add_options(host, keys)
    global tcp_options
    if os.path.isfile(host+".startup"):
        for option in keys:
	    f = opent(host+".startup","a")
	    f.write("sysctl -w
		net.ipv4."+option+"={value}".format(value=tcp_options[option]))
	    f.close()
    else:
        print "Host name %s incorrect, the corresponding .startup file doesn't exit" % (host)
	sys.exit()


###
# onHosts must be a list of names without .startup
#
###

def write_options(onHosts):
    global tcp_options
    configure(onHosts) # TODO: in create_topology.py
    for host in onHosts :
        # add tcp options for host
	if os.path.isfile(host+".startup"):
	    f = open(host+".startup",'w')
	    for option in tcp_options.keys():
	        f.write("sysctl -w
		    net.ipv4."+option+"={value}".format(value=tcp_options[option]))
	    f.close()
	else:
	    print "Host name %s incorrect, the corresponding .startup file
		doesn't exit" % (host)
	    sys.exit()

def modify_options(host, keys):
    global tcp_options
    if os.path.isfile(host+".startup"):
        for option in keys:
	    f = open(host+".startup","r")
	    modif = ""
	    for line in f :
		if option not in line
		    modif+=line
	    f.close()
	    f = open(host+".startup","w")
	    modif+= "sysctl -w
	    net.ipv4."+option+"={value}".format(value=tcp_options[option])
	    f.write(modif)
	    f.close()
    else:
	print "Host name %s incorrect, the corresponding .startup file
	doesn't exit" % (host)
	sys.exit()

def usage():
    print " for default configuration: python set_tcp_options.py "
    print " to give the same set of options to each host: python
    set_tcp_option.py --all [option1]=[value] [option2]=[value] "
    print " to add an option to a particular host: python set_tcp_options.py -a
    host=[hostname] [option1]=[value] [option2]=[value] ...  "
    print " to modify an option to a particular host: python set_tcp_option.py
    -m host=[hostname] [option1]=[value] [option2]=[value] ... "

#main function
def main(argv):
    parse_option(argv)
    
if __name__=="__main__":
    main(sys.argv[1:])

