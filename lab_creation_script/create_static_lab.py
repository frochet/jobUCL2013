import sys
from router import Router
from create_lab import Create_lab

class Create_static_lab(Create_lab):

    def __init__(self,pathToGraph,pathToDir):
        Create_lab.__init__(self,pathToGraph)
        for node in self.graph.nodes():
	  if node[0] == 'r' or node[0] == 'R':
            r = Router(node)
            self.netkit_components += [r]
	  elif node[0] == 'p' or node[0] == 'P':
	    p = Pc(node)
	    self.netkit_components += [p]
	  else:
	    print "malmorfed dot file, elem should be routers and/or pc in this lab. Please start the name of the components by r[...] for router and by p[...] for pc"
	    sys.exit()
        self.set_interface_and_zone()
        self.set_data_from_edges()
        self.give_ipv6("2001:db8:")
        for component in self.netkit_components:
            component.create_dir(pathToDir)
            component.create_startup(pathToDir)
            component.fill_startup_file(pathToDir)

        self.create_conf(pathToDir)
def usage():
    print "python create_static_lab -f [pathToDotFile] [pathToNetkitDirectory]"
    
def main(argv):
    if len(argv)==0:
        usage()
    else:
        if argv[0] == "-d":
            pass # write default labs file
        elif argv[0] =="-f":
            lab = Create_static_lab(argv[1], argv[2])
        elif argv[0] == "-h":
            usage()
        else:
            usage()
            


if __name__ == "__main__":
    main(sys.argv[1:])
