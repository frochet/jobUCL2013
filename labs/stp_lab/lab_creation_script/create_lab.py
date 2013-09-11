import networkx as nx
import random
class Create_lab():

  def __init__(self, pathToGraph):
    self.graph = nx.read_dot(pathToGraph)
   # self.graph = nx.to_agraph(self.graph)
    self.netkit_components = []
    self.zones_given = []

  
  def create_conf(self, pathToDir, lab_descr=None, lab_ver=None, lab_auth=None, lab_email=None, lab_web=None):
    f = open(pathToDir+"lab.conf", "w")
    if lab_descr:
      f.write("LAB_DESCRIPTION=\""+lab_descr+"\"\n")
    if lab_ver:
      f.write("LAB_VERSION="+lab_ver+"\n")
    if lab_auth :
      f.write("LAB_AUTHOR=\""+lab_auth+"\"\n")
    if lab_email:
      f.write("LAB_EMAIL="+lab_email+"\n")
    if lab_web:
      f.write("LAB_WEB="+lab_web+"\n")


    for component in self.netkit_compenents:
      for interface in component.attr['map_IF_zone']:
	f.write("%s[%d]=%s\n"%(component.attr['name'], interface,
	  component.attr['map_IF_zone'][interface]))

    f.close()
    

  def set_interface_and_zone(self):
    for node in self.graph:
      node_degree = self.graph.degree(node)
      s = self.get_component(node)
      zone = self.new_zone()
      for neighbor in self.graph.neighbors(node):
	IF = s.get_next_interface(node_degree)
	s_neighbor = self.get_component(neighbor)
	IF_neighbor =  s_neighbor.get_next_interface(self.graph.degree(neighbor))
	if IF >= 0:
	  s.set_interface(IF, zone, s_neighbor)
	if IF_neighbor >= 0:
 	  s_neighbor.set_interface(IF_neighbor, zone, s)
 
  def set_weights(self):
    L = self.graph.nodes()
    for node_from, nbrs in self.graph.adjacency_iter():
      for node_to, edges in nbrs.items():
	for edge in edges.items():
	  if node_from!=node_to:
	    if "weight" in edge[1] :
	      w = edge[1]['weight']
	      s = self.get_component(node_to)
	      IF = s.get_interface_used_between(node_from)
	      if IF != None:
	        if s:
                  s.attr['map_weight'][IF] = w
	        else:
		  print "Error occured, no netkit_component called "+node_to
	      else:
                 print "Error occured, no interface has been matched from "+node_to+" to neighbor "+node_from
	    else:
	       print "no weight attribute to the "+node_from+ " -> "+node_to+" edge. Default value is taken"
  def get_component(self, node):
    for elem in self.netkit_components :
      if node == elem.attr['name'] :
	return elem
    return None
  
  
  


  def new_zone(self):
    """ create a random zone A0 ~ Z99  """
    cond = True
    while cond:
      zone = ""
      zone+=random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
      zone+=random.choice('01234566789')
      if zone not in self.zones_given :
	cond = False
	self.zones_given += [zone]
    return zone
    
