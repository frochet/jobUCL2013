from netkit_component import NetkitComponent
import os
import sys

class Router(NetkitComponent):

    def __init__(self,name):
        NetkitComponent.__init__(self, name)
        
    def fill_ospf_startup_file(self,path):
        f = open(path+"/"+self.attr['name']+".startup","w")
        for IF in self.attr['IF']:
            f.write("ifconfig eth"+IF+" up\n")
            #f.write adresse ip 
            
        f.write("# Active ipv6 forwarding\n") 
        f.write("sysctl -w net.ipv6.conf.all.forwarding=1\n")
        f.close()
        
    def create_ospf_dir(self, path):
        os.makedirs(path+"/"+self.attr['name']+"/etc/quagga")
        #fichier daemons
        f = open(path+"/"+self.attr['name']+"/etc/quagga/daemons","w")
        f.write("zebra=yes\nbgpd=no\nospfd=no\nospf6d=yes\nripd=no\nripngd=no")
        f.close()
        
        #fichier zebra.conf
        f = open(path+"/"+self.attr['name']+"/etc/quagga/zebra.conf","w")
        f.write("hostname Router\npassword zebra\nlog file /var/log/quagga/zebra.log")
        f.close()
        
        #fichier ospf6d.conf
        f = open(path+"/"+self.attr['name']+"/etc/quagga/ospf6d.conf","w")
        f.write("hostname ospf6d\npassword zebra\n")
        for IF in self.attr['map_weight']:
            f.write("interface eth"+IF+"\n")
            f.write("ipv6 ospf6 cost"+self.attr['map_weight'][IF]+"\n")
        f.write("router ospf6\n")
        #todo router id   f.write("router-id 255.0.0.X")
        for IF in self.attr['IF']:
            f.write("interface eth"+IF+" area 0.0.0.0")
        
        f.write("log file /var/log/zebra/ospf6d.log")
        f.close()
        
    def create_ripng_dir(self,path):
        os.makedirs(path+"/"+self.attr['name']+"/etc/quagga")
        
        #fichier daemons
        f = open(path+"/"+self.attr['name']+"/etc/quagga/daemons","w")
        f.write("zebra=yes\nbgpd=no\nospfd=no\nospf6d=no\nripd=no\nripngd=yes")
        f.close()
    
        #fichier zebra.conf
        f = open(path+"/"+self.attr['name']+"/etc/quagga/zebra.conf","w")
        f.write("hostname Router\npassword zebra\nlog file /var/log/quagga/zebra.log")
        f.close()
        
        #fichier ripngd.conf
        f = open(path+"/"+self.attr['name']+"/etc/quagga/ripngd.conf","w")
        f.write("router ripng\nnetwork ::/0")
        f.close()
            
