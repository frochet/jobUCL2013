
import sys
from router import Router
from create_lab import Create_lab

class Create_ospf_lab(Create_lab):

    def __init__(self,pathToGraph,pathToDir):
        create_lab.__init__(self,pathToGraph)
        for node in self.graph.nodes():
            r = Router(node)
            self.netkit_components += [r]
        self.set_interface_and_zone()
        self.set_weights()
        for router in self.netkit_components:
            router.create_dir(pathToDir)
            router.create_startup(pathToDir)
            
            #Prints

            print router.attr['IF']
            print router.attr['map_IF_neighbor']
            print router.attr['map_IF_zone']
            print router.attr['map_weight']

def usage():
    pass
    
def main(argv):
    if len(argv)==0:
        usage()
    else:
        if argv[0] == "-d":
            pass # write default labs file
        elif argv[0] =="-f":
            lab = create_ospf_lab(argv[1], argv[2])
        elif argv[0] == "-h":
            usage()
        else:
            usage()
            


if __name__ == "__main__":
    main(sys.argv[1:])
