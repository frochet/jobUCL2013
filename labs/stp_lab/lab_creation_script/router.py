from netkit_component import NetkitComponent
import os
import sys


As=1
Rid='0.0.0.1'
class Router(NetkitComponent):

  def __init__(self,name):
    NetkitComponent.__init__(self, name)
    self.attr['as']=None
    self.attr['router-id']=''
    
  def define_router_id(self):
    global Rid
    self.attr['router-id']=Rid
    temp=map(int,Rid.split("."))
    if temp[0]>= 255 :
      printf("you made way too much router!")
      exit()
    if temp[1] >= 255 :
      temp[1]=0
      temp[0]+=1
    if temp[2] >= 255:
      temp[2] = 0
      temp[1]+=1
    if temp[3]>= 255:
      temp[3]=0
      temp[2]+=1
    Rid=".".join(temp)

  def define_as(self):
    global As
    self.attr['as']=As
    As+=1

  def fill_ospf_startup_file(self,path):
    f = open(path+"/"+self.attr['name']+".startup","w")
    for IF in self.attr['IF']:
      f.write("ifconfig eth"+IF+" up\n")
      #f.write("ifconfig eth"+IF+" add ::) adresse ip 

    f.write("# Active ipv6 forwarding\n") 
    f.write("sysctl -w net.ipv6.conf.all.forwarding=1\n")
    f.close()

  def create_ospf_dir(self, path):
    try:
      os.makedirs(path+"/"+self.attr['name']+"/etc/quagga")
    except: OSError
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
    f.write("router-id "+self.attr['router-id']+"\n")

    for IF in self.attr['IF']:
      f.write("interface eth"+IF+" area 0.0.0.0")

    f.write("log file /var/log/zebra/ospf6d.log")
    f.close()

  def create_ripng_dir(self,path):
    try:
      os.makedirs(path+"/"+self.attr['name']+"/etc/quagga")
    except:OSError

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

  def create_bgp_dir(self,path):
    global As
    try:
      os.makedirs(path+"/"+self.attr['name']+"/etc/quagga")
    except:OSError  

    #fichier daemons
    f = open(path+"/"+self.attr['name']+"/etc/quagga/daemons","w")
    f.write("zebra=yes\nbgpd=yes\nospfd=no\nospf6d=no\nripd=no\nripngd=no")
    f.close()

    #fichier zebra.conf
    f = open(path+"/"+self.attr['name']+"/etc/quagga/zebra.conf","w")
    f.write("hostname Router\npassword zebra\nlog file /var/log/quagga/zebra.log")
    f.close()

    #fichier bgpd.conf
    f = open(path+"/"+self.attr['name']+"/etc/quagga/bgpd.conf","w")
    f.write("hostname bgpd\npassword zebra\n")
    f.write("router bgp "+As+"\n")
    f.write("bgp router-id "+self.attr['router-id']+"\n")
    for i in self.attr['neighbors']
      f.write("neighbor "+i.attr['ipv6']+" remote-as "+i.attr['as']\n")
      f.write("!add routemap if it's needed.")
    for i in self.attr['neighbors']
      f.write("no neighbor "+i.attr['ipv6']+" activate\n")
    f.write("address-family ipv6\n")
    f.write("!add the network that the router must share below\n")
    for i in self.attr['neighbors']
      f.write("neighbor "+i.attr['ipv6']+" activate\n")
    f.write("exit-address-family\n")
    f.write("!make your community list and route map below\n")
      
