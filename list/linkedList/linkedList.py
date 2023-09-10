#linked list:

class Node:
    def __init__(self, data) -> None:
        self.data= data
        self.next = None
        
    def __repr__(self) -> str:
        return self.data

class LinkedList:
    def __init__(self, nodes = None) -> None:
        self.head = None
       
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

list = LinkedList()    
firstNode = Node("a")
secondNode = Node("b")
thirdNode = Node("c")

list.head = firstNode
firstNode.next = secondNode
secondNode.next = thirdNode
print(list)

