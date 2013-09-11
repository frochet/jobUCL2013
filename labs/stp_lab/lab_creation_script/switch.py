from netkit_component import NetkitComponent

class Switch(NetkitComponent):


  def __init__(self, name):
    NetkitComponent.__init__(self, name)  


  def fill_startup_file(self, path):
    f = open(path+"/"+self.attr['name']+".startup","w")
    for IF in self.attr['IF']:
      f.write("ifconfig eth%d "+IF+" up\n")

    f.write("brctl addbr br0\n")
    for IF in self.attr['IF']:
      f.write("brctl addif br0 eth"+IF)
 
