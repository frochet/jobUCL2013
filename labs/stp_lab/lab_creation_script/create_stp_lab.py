#Non-generic file, specially written for this lab

import sys
from switch import Switch

class Create_stp_lab(Create_lab):


  def __init__(self, pathToGraph, pathToDir):
    Create_lab.__init__(self, pathToGrah)
    for node in self.graph.nodes():
      s = Switch(node['name'])
      s.create_dir()
      self.netkit_components += [s]
    set_interface_and_zone()
    for switch in self.netkit_components:
      switch.create_dir(pathToDir)
      switch.create_startup()
      switch.create_conf()


def usage():
  pass

def main(argv):
  if len(argv) == 0:
    usage()
  else:
    if argv[0] == "-d":
      pass # write actual defaults files
    elif argv[0] == "-f":
      pass
    elif argv[0] == "-h":
      usage()
    else:
      usage()


if __name__ = "__main__":
  main(sys.argv[1:])
