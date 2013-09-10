import networkx as nx
import random
class Create_lab():

  def __init__(self, pathToGraph):
    self.graph = nx.read_dot(pathToGraph)
    #self.graph = nx.to_agraph(self.graph)
    self.netkit_components = []
    self.zones_given = []

  
  def create_conf(self):
    pass

  def set_interface_and_zone(self):
    for node in self.graph:
      node_degree = self.graph.degree(node)
      s = self.get_component(node)
      for neighbor in self.graph.neighbors(node):
	IF = s.get_next_interface(node_degree)
	s_neighbor = self.get_component(neighbor)
	IF_neighbor =  s_neighbor.get_next_interface(self.graph.degree(neighbor))
	zone = self.new_zone()
	if IF >= 0:
	  s.set_interface(IF, zone, s_neighbor)
	if IF_neighbor >= 0:
 	  s_neighbor.set_interface(IF_neighbor, zone, s)
 
  def set_weights(self):
    L = self.graph.nodes()
    for node_from, nbrs in self.graph.adjacency_iter():
      for node_to, eattr in nbrs.items():
	if node_from!=node_to:
	   if "weight" in eattr :
	     w = eattr['weight']
	     s = self.get_component(j)
	     IF = s.get_interface_between(i)
	     if IF:
	       if s:
                 s.attr['map_weight'][IF] = w
	       else:
		 print "Error occured, no netkit_component called "+j
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
    
