from netkit_component import NetkitComponent


Mac="00:01"
class Switch(NetkitComponent):


  def __init__(self, name):
    NetkitComponent.__init__(self, name)  
    self.attr['mac-addr']=""

  def define_hw_addr(self):
    global Mac
    self.attr['mac-addr']="00:00:00:00:"+Mac
    temp=Mac.split(":")
    temp2=[]
    i=0
    while i<2:
      temp2[i]=int("0x"+temp[i])
    if temp2[0]>=255:
      printf("you made way too much switch!")
      exit()
    if temp2[1]>=255:
      temp2[0]+=1
      temp2[1]=0
    else:
      temp2[1]+=1
    Mac=":".join(hex(temp2))
          
    
    
    

  def fill_startup_file(self, path):
    f = open(path+"/"+self.attr['name']+".startup","w")
    for IF in self.attr['IF']:
      f.write("ifconfig eth"+str(IF)+" hw ether "+self.attr['mac-addr']+"up\n")

    f.write("brctl addbr br0\n")
    for IF in self.attr['IF']:
      f.write("brctl addif br0 eth"+str(IF)+"\n")
    
    for key, value in self.attr['map_weight'].items():
      f.write("brctl setpathcost br0 eth%s %s" % (key, value))

    f.close()
