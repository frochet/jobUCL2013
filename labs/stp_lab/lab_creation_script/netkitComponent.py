
 
# common methods for netkit components
# 2 spaces indentation.
#
import os
import sys

class NetkitComponent:

  def __init__(self):
    
    self.attr = dict()
    self.attr['IF'] = dict() # Map interface to netkit zone
    self.attr['name'] = ""

  
  def set_interface(interface, zone): 
    """interface is an int and zone something between A0 and Z99"""
    self.attr['IF'][interface] = zone


  def get_next_interface(degree):
    if not self.attr['IF'].keys():
      return 0
    else:
      L =  self.attr['IF'].keys().sort(reverse=True)
      if L[0]+1 < degree
        return L[0]+1
      else:
	return None

  def create_dir(path):
    if not os.path.isdir(path+"/+"+self.attr['name']):
      try:
	os.mkdir(path+"/+"+self.attr['name'])
      except OSError:
	print "Error happened when mkdir of "+self.attr['name']
	sys.exit()

  def create_startup():
    pass
