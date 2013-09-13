import networkx as nx
import random
import os
class Create_lab():

  def __init__(self, pathToGraph):
    self.graph = nx.read_dot(pathToGraph)
   # self.graph = nx.to_agraph(self.graph)
    self.netkit_components = []
    self.zones_given = []
    self.zones_ip=dict() #____:____:XXXX:XXXX::____

  
  def create_conf(self, pathToDir, lab_descr=None, lab_ver=None, lab_auth="O.Bonaventure,F.Rochet, J.Vellemans", lab_email=None, lab_web=None):
    f = open(pathToDir+"/lab.conf", "w")
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
      f.write(""+str(component.attr['name'])+"[M]=64\n")
      for interface in component.attr['map_IF_zone']:
        f.write("%s[%d]=%s\n"%(component.attr['name'], interface, component.attr['map_IF_zone'][interface]))

    f.close()
    self._create_sniffer(pathToDir)
 
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
    L = self.netkit_components[:]
    L.sort(reverse=True)
    for s in L:
      for neighbor in self.graph.neighbors(s.attr['name']):
	if "zone" in self.graph.node[s.attr['name']] and "zone" in self.graph.node[neighbor]:
	  s_neighbor = self.get_component(neighbor)
	  IF_neighbor = s_neighbor.get_next_interface()
	  if self.graph.node[s.attr['name']]["zone"] == self.graph.node[neighbor]["zone"]:
	    if zone_id in s.attr['map_IF_zone'].values():
	      IF = None
	      if IF_neighbor != None: 
	        s_neighbor.set_interface(IF_neighbor, zone_id, s)
		self._add_zone_given(zone_id)
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
	  self._add_zone_given(zone)
    self._set_mapping_IF_neighbors()

  def _set_mapping_IF_neighbors(self):

    L = self.netkit_components[:]
    L.sort(reverse=True)
    for s in L:
      for neighbor in self.graph.neighbors(s.attr['name']):
	for IF, zone in s.attr['map_IF_zone'].items():
	  s_neighbor = self.get_component(neighbor)
	  if zone in s_neighbor.attr['map_IF_zone'].values():
	    s.attr['map_IF_neighbor'] += [(IF, s_neighbor)]

  def set_data_from_edges(self):
    for node_from, nbrs in self.graph.adjacency_iter():
      for node_to, edges in nbrs.items():
	for edge in edges.values():
	  if node_from!=node_to:
	    s = self.get_component(node_to)
	    IF = s.get_interface_used_between(node_from)
	    if "weight" in edge :
	      w = edge['weight']
	      if IF != None:
	        if s:
                  s.attr['map_weight'][IF] = w
	        else:
		  print "Error occured, no netkit_component called "+node_to
	      else:
                 print "Error occured, no interface has been matched from "+node_to+" to neighbor "+node_from
	    else:
	       print "no weight attribute to the "+node_from+ " -> "+node_to+" edge. Default value is taken"
            if "delay" in edge:
              delay = edge['delay']
	      if IF != None:
	        if s:
		  s.attr['map_IF_delay'][IF] = delay
		else:
		  print "Error occured, no netkit_component called "+node_to
	      else:
		print "Error occured, no interface has been matched from "+node_to+" to neighbor "+node_from
	    if "bandwidth" in edge: 
	      bandwidth = edge['bandwidth']
	      if IF != None:
		if s:
		  s.att['map_IF_bandwidth'][IF] = bandwidth
		else:
		  print "Error occured, no netkit_component called "+node_to
	      else:
		print "Error occured, no interface has been matched from "+node_to+" to neighbor "+node_from

  
  def set_bandwidth(self):
    pass
  
  def get_component(self, node):
    for elem in self.netkit_components :
      if node == elem.attr['name'] :
	return elem
    return None
 

  def usage():
    print "This script generate a netkit lab from a .dot file"

  def new_zone(self):
    """ create a random zone A0 ~ Z99  """
    cond = True
    while cond:
      zone = ""
      zone+=random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
      zone+=random.choice('01234566789')
      if zone not in self.zones_given :
	cond = False
    return zone
    
    
  def _create_sniffer(self, pathToDir):
    IF=0
    f = open(pathToDir+"/lab.conf", "a")
    f.write("sniffer[M]=64\n")
    for i in self.zones_given :
      f.write("sniffer["+str(IF)+"]="+i+"\n")
      IF+=1
    f.close()
  
    f = open(pathToDir+"/sniffer.startup", "w")
    j=0
    while j<IF:
      f.write("ifconfig eth"+str(j)+" up\n")
      j+=1
    f.close()
    try:
      os.makedirs(pathToDir+"/sniffer")
    except OSError:
      if not os.path.isdir(pathToDir+"/sniffer"):
	print "Bad things happened during directory set up. lab could not working properly"
  
  
  def _add_zone_given(self, zone):
    if zone not in self.zones_given:
      self.zones_given += [zone]
      
      
      
  def give_ipv6(self,Prefix):
    ipzone="0000:0001"
    for zone in self.zones_given:
      self.zones_ip[zone]=ipzone
      temp=ipzone.split(":")
      i=0
      while i<2:
        temp[i]=int("0x"+temp[i],0)
        i+=1
      if temp[0]>=65535:
        printf("too much subnetworks")
      if temp[1]>=65535:
        temp[0]+=10000  #to have more differents subnetworks, not only 0001,0002,...
        temp[1]=0
      else:
        temp[1]+=10000  #to have more differents subnetworks, not only 0001,0002,...
        
      temp[0]= "%0.4x" % temp[0]
      temp[1]= "%0.4x" % temp[1]
      ipzone=":".join(temp)
      
      
    for components in self.netkit_components:
      ipend="0000"
      for IF in components.attr['IF']:
      #  print self.zones_ip
       # print self.zones_given
        components.attr['map_IF_ipv6'][IF]=""+Prefix+""+self.zones_ip[components.attr['map_IF_zone'][IF]]+"::"+ipend
        ipend=int("0x"+ipend,0)
        ipend+=1
        ipend="%0.4x" % ipend
