import sys
from router import Router
from create_lab import Create_lab

class Create_bgp_lab(Create_lab):

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
            router.create_bgp_dir(pathToDir)
            
	self.create_conf(pathToDir)
def usage():
    super(Create_bgp_lab, self).usage()
    print "python create_bgp_lab -f [pathToDotFile] [pathToNetkitDirectory]"
    
def main(argv):
    if len(argv)==0:
        usage()
    else:
        if argv[0] == "-d":
            pass # write default labs file
        elif argv[0] =="-f":
            lab = Create_bgp_lab(argv[1], argv[2])
        elif argv[0] == "-h":
            usage()
        else:
            usage()
            


if __name__ == "__main__":
    main(sys.argv[1:])
