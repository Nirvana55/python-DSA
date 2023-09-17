#leet code question:Easy

#there is a head and we need to reverse the list

#breakdown
#if head is not none
#we can iterate to last loop
#head = last node 
#head.next = last_node.prev
#linked list = head, next
#while self.head is not None

class Node:
  def __init__(self, data) -> None:
    self.data = data
    self.next = None
  
class LinkedList:
  def  __init__(self, nodes) -> None:
    self.head = None
    if nodes is not None:
      node = Node(data=nodes.pop(0))
      self.head = node
    for elements in nodes:
      node.next = Node(data=elements)
      node = node.next

  def __repr__(self) -> str:
    nodes = []
    current  = self.head
    prev = None
    while current is not None:
      next = current.next
      current.next = prev
      prev = current
      current = next
    self.head = prev
    
    while prev is not None:
      nodes.append(prev.data)
      prev = prev.next
    nodes.append("None")
    return "->".join(map(str,nodes))

s1 = LinkedList([1,2,3,4])
print(s1)
