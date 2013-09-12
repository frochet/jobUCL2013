from netkit_component import NetkitComponent

class Switch(NetkitComponent):


  def __init__(self, name):
    NetkitComponent.__init__(self, name)  


  def fill_startup_file(self, path):
    f = open(path+"/"+self.attr['name']+".startup","w")
    for IF in self.attr['IF']:
      f.write("ifconfig eth"+str(IF)+" up\n")

    f.write("brctl addbr br0\n")
    for IF in self.attr['IF']:
      f.write("brctl addif br0 eth"+str(IF)+"\n")
    
    for key, value in self.attr['map_weight'].items():
      f.write("brctl setpathcost br0 eth%s %s" % (key, value))

    f.close()
