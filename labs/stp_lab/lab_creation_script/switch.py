from netkit_component import NetkitComponent

class Switch(NetkitComponent):


  def __init__(self, name):
    NetkitComponent.__init__(self, name)  


  def fill_startup_file(path):

    f = open(path+"/"+self.attr['name']+".startup","w")
    for IF in self.attr['IF'].keys():
      f.write("ifconfig eth0 "+IF+" up\n")
