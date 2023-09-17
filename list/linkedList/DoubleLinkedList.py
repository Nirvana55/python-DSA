import gc

class Node:
  def __init__(self,data) -> None:
    self.data = data
    self.next = None
    self.prev = None

class DoubleLinkedList:
  def __init__(self, nodes = None) -> None:
    self.head = None
    if nodes is not None:
      node = Node(data=nodes.pop(0))
      self.head = node
      for elements in nodes:
        new_node = Node(data=elements)
        node.next = new_node
        new_node.prev = node
        node = node.next
        
  def __repr__(self) -> str:
    nodes = []
    node = self.head
    while node is not None:
      nodes.append(node.data)
      node = node.next
    nodes.append("None")
    return "<->".join(map(str,nodes))
  
  def __iter__(self):
    nodes = self.head
    while nodes is not None:
      yield nodes
      nodes = nodes.next
  
  def reusing_function(self,func,target_node):
    if self.head is None:
      raise Exception("No element in list")
  
    for node in self:
      loop_end_value = func(target_node,node)
      if loop_end_value == "end":
        return
    
    raise Exception("Not found")
  
  def find_prev(self, target_node, node):
    if target_node.data == node.data:
        print(f"The target element previous is {node.prev.data}")
        return "end"

  def remove_node(self,target_node):
    if target_node.data == None:
      return
     
    if target_node.data == self.head.data:
      self.head = target_node.next
      if self.head is not None:
        self.head.prev == None
        return
    
    if target_node.prev.data is not None:
      target_node.prev.next = target_node.next
    if target_node.next.data is not None:
      target_node.next.prev = target_node.prev
    return
  
        
s1 = DoubleLinkedList([1,2,3,4,5])
s1.reusing_function(s1.find_prev, target_node=Node(data=3))
s1.remove_node(target_node=s1.head.next)
print(s1)






      
    


