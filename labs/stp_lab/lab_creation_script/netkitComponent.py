
 
# common methods for netkit components
# 2 spaces indentation.
#

class NetkitComponent:

  def __init__(self):
    
    self.attr = dict()
    self.attr['IF'] = dict() # Map interface to netkit zone
    self.attr['name'] = ""

  
  def assign_interface(interface, zone): 
    self.attr['IF'][interface] = zone


  def get_next_interface():
    if not self.attr['IF'].keys():
      return 0
    else:
      L =  self.attr['IF'].keys().sort(reverse=True)
      return L[0]+1

  def create_dir():
    pass

  def create_startup():
    pass
