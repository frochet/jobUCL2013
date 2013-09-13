
import sys
from router import Router
from create_lab import Create_lab

class Create_ospf_lab(Create_lab):

  def __init__(self,pathToGraph,pathToDir):
    Create_lab.__init__(self,pathToGraph)
    for node in self.graph.nodes():
      r = Router(node)
      self.netkit_components += [r]
    self.set_interface_and_zone()
    self.set_data_from_edges()
    self.give_ipv6("2001:db8:")
    for router in self.netkit_components:
      router.create_dir(pathToDir)
      router.create_startup(pathToDir)
      router.fill_startup_file(pathToDir)
      router.create_ospf_dir(pathToDir)

    self.create_conf(pathToDir)   
def usage():
<<<<<<< HEAD
  super(Create_ospf_lab, self).usage()
=======
>>>>>>> c10ce85b97f656b7d19a1132d60424a97611803b
  print "python create_ospf_lab -f [pathToDotFile] [pathToNetkitDirectory]"
  
def main(argv):
  if len(argv)==0:
    usage()
  else:
<<<<<<< HEAD
    if argv[0] == "-d":
      pass # write default labs file
    elif argv[0] =="-f":
=======
    if argv[0] =="-f":
>>>>>>> c10ce85b97f656b7d19a1132d60424a97611803b
      lab = Create_ospf_lab(argv[1], argv[2])
    elif argv[0] == "-h":
      usage()
    else:
      usage()
      


if __name__ == "__main__":
  main(sys.argv[1:])
