import networkx as nx

class Create_lab():

  def __init__(self, pathToGraph):
    self.graph = nx.read_dot(pathToGraph)
    self.netkit_components = []
    

  
  def create_conf(self):
    pass

  def set_interface_and_zone(self):
    for node in self.graph:
      node_degree = self.graph.degree(node)
      s = self.get_component(node)
      for neighbor in self.graph.all_neighbors(node):
	IF = s.get_next_interface(node_degree)
	s_neighbor = self.get_component(neighbor)
	IF_neighbor =  s_neighbor.get_next_interface(self.graph.degree(neighbor))
	if IF not None and IF_neihbor not None:
	  zone = new_zone()
	  s.set_interface(IF, zone)
	  s_neighbour.set_interface(IF_neighbor, zone)
 
  def set_weights(self):
    L = self.graph.nodes()


  def get_component(node):
    pass
  
  
  def new_zone():
    """ create a random zone A0 ~ Z99  """
    pass
