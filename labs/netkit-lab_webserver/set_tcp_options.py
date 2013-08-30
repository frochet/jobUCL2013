#!/usr/bin/env python
#coding=utf-8
#
#Script to modify tcp options in netkit
#Author: F.Rochet
#indentation in 4 space

import os
import sys
import getopt
import create_topology

tcp_options = dict()


def default(onHosts):
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

    write_options(onHosts)



def add_options(host, keys):
    global tcp_options
    if os.path.isfile(host+".startup"):
        for option in keys:
	    f = open(host+".startup","a")
	    f.write("sysctl -w net.ipv4."+option+"={value} \n".format(value=tcp_options[option]))
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
    create_topology.configure(onHosts) # TODO: in create_topology.py
    for host in onHosts :
        # add tcp options for host
	if os.path.isfile(host+".startup"):
	    f = open(host+".startup",'a')
	    for option in tcp_options.keys():
	        f.write("sysctl -w net.ipv4."+option+"={value} \n".format(value=tcp_options[option]))
	    f.close()
	else:
	    print "Host name %s incorrect, the corresponding .startup file doesn't exit" % (host)
	    sys.exit()

def modify_options(host, keys):
    global tcp_options
    if os.path.isfile(host+".startup"):
        for option in keys:
	    f = open(host+".startup","r")
	    modif = ""
	    for line in f:
	        if option not in line:
		    modif+=line
	    f.close()
	    f = open(host+".startup","w")
	    modif+= "sysctl -w net.ipv4."+option+"={value}\n".format(value=tcp_options[option])
	    f.write(modif)
	    f.close()
    else:
	print "Host name %s incorrect, the corresponding .startup file doesn't exit" % (host)
	sys.exit()

##
#Add to the dict the keys and the values and 
#return the list of options given by the user.
##

def get_keys(key_value_list):
    global tcp_options
    keys = []
    for key_value in key_value_list:
	elems = key_value.split("=")
	tcp_options[elems[0]] = elems[1]
	keys.append(elems[0])
    
    return keys 

def usage():
    print " for default configuration: python set_tcp_options.py -d "
    print " to give the same set of options to each host: python set_tcp_option.py --all [option1]=[value] [option2]=[value] "
    print " to add an option to a particular host: python set_tcp_options.py -a [hostname] [option1]=[value] [option2]=[value] ...  "
    print " to modify an option to a particular host: python set_tcp_option.py -m [hostname] [option1]=[value] [option2]=[value] ... "

#main function
def main(argv):
   if argv[0] == "-a" :
     add_options(argv[1], get_keys(argv[2:]))
   elif argv[0] == "--all":
     global tcp_options
     for key_value in argv[1:] :
       elems = key_value.split("=")
       tcp_options[elems[0]] = elems[1]
     write_options( ["r", "server", "client1", "client2"])
   elif argv[0] == "-m":
     modify_options(argv[1], get_keys(argv[2:]))
   elif argv[0] == "-d" :
       default(["r", "server", "client1", "client2"]) 
   elif argv[0] == "-h" :
       usage()
   else:
       usage()
    
if __name__=="__main__":
    main(sys.argv[1:])

