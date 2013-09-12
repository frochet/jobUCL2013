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


    for component in self.netkit_components:
      for interface in component.attr['map_IF_zone']:
        f.write("%s[%d]=%s\n"%(component.attr['name'], interface, component.attr['map_IF_zone'][interface]))

    f.close()
 
  def _set_nbr_interface(self):
    for node in self.graph:
      count = -1;
      for neighbor in self.graph.neighbors(node):
        if "zone" in self.graph.node[node] and "zone" in self.graph.node[neighbor]:
	  if self.graph.node[node]['zone'] == self.graph.node[neighbor]['zone']:
	    count+=1
      s = self.get_component(node)
      if count >= 0:
	s.attr['nbr_IF'] = self.graph.degree(node) - count
      else:
	s.attr['nbr_IF'] = self.graph.degree(node)
      
  def set_interface_and_zone(self):
    self._set_nbr_interface()
    zone_id = self.new_zone()
    zone = ""
    IF = -1
    IF_neighbor = -1
    L = self.netkit_components
    L.sort(reverse=True)
    for s in L:
      for neighbor in self.graph.neighbors(s.attr['name']):
	if "zone" in self.graph.node[s.attr['name']] and "zone" in self.graph.node[neighbor]:
	  s_neighbor = self.get_component(neighbor)
	  IF_neighbor = s_neighbor.get_next_interface()
	  if self.graph.node[s.attr['name']]["zone"] == self.graph.node[neighbor]["zone"]:
	    if zone_id in s.attr['map_IF_zone'].values():
	      #print "should see %s with IF=%d"% (neighbor, IF_neighbor)
	      IF = None
	      if IF_neighbor != None: 
	        s_neighbor.set_interface(IF_neighbor, zone_id, s)
	    else:
	      zone_id = self.new_zone()
              IF = s.get_next_interface()
	      zone = zone_id
	  else:
	    zone_id = self.new_zone()
	    IF = s.get_next_inteface(node_degree)
	    zone = zone_id
        else:
	  zone = self.new_zone()
	  IF = s.get_next_interface()
	  s_neighbor = self.get_component(neighbor)
          IF_neighbor = s_neighbor.get_next_interface()
	if IF != None and IF_neighbor != None:
	  s.set_interface(IF, zone, s_neighbor)
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
    
