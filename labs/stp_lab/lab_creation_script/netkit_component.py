
 
# common methods for netkit components
# 2 spaces indentation.
#
import os
import sys

class NetkitComponent:

  def __init__(self, name):
    
    self.attr = dict()
    self.attr['map_IF_zone'] = dict() # Map interface to netkit zone and its neighbor
    self.attr['map_IF_neighbor'] = dict()
    self.attr['name'] = name
    self.attr['map_weight'] = dict()
    self.attr['IF'] = []
  
  def set_interface(self, interface, zone, neighbor): 
    """interface is an int and zone something between A0 and Z99"""
    self.attr['map_IF_zone'][interface] = zone
    self.attr['map_IF_neighbor'][interface] = neighbor.attr['name']
    self.attr['IF'] += [interface]

  def get_next_interface(self, degree):
    if not self.attr['IF']:
      return 0
    else:
      L =  self.attr['IF'].sort(reverse=True)
      if L[0]+1 < degree:
        return L[0]+1
      else:
	return None
  
  def get_interface_used_between(self, neighbor):
    for key in self.attr['map_IF_neighbor'].keys():
      if self.attr['map_IF_neighbor'][key] == neighbor:
	return key
    return None

  def create_dir(self, path):
    if not os.path.isdir(path+"/+"+self.attr['name']):
      try:
	os.mkdir(path+""+self.attr['name'])
      except OSError:
	if not os.path.isdir(path+""+self.attr['name']) :
	  print "Error happened when mkdir of "+self.attr['name']
  def create_startup(self, path):
    file(path+""+self.attr['name']+".startup", "w")
