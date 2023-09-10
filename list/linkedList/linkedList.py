#linked list:

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    # initializing the instance variable
    def __init__(self, nodes = None) -> None:
        self.head = None
        if nodes is not None:
            # instance of node class
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
    
    # to represent the value
    def __repr__(self) -> str:
        nodes =[]
        node = self.head
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    # iterating 
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # adding on first
    def add_first(self, node:Node):
        node.next = self.head
        self.head = node

    # add last
    def add_last(self,node:Node):
        if self.head is None:
            self.head = node
            return
        # doing nothing until the elem reaches last
        for elem in self:
            pass
        elem.next = node

    def add_middle(self,target_node,new_node:Node):
        if self.head is None:
            raise Exception("no element in the list")
        
        for node in self:
            if target_node == node.data:
                new_node.next = node.next
                node.next = new_node
                return
            
        raise Exception("target node not found")
    
    def remove_node(self,target_node):
        if self.head is None:
            raise Exception("no element in the list")
        
        if self.head.data == target_node:
            self.head = self.head.next
            return
        

        prev_node = self.head
        for node in self:
            if node.data == target_node:
                prev_node.next = node.next
                return
            prev_node = node

        raise Exception("Target not found")
        

list = LinkedList(["a","b","c"])
list.add_first(Node("d"))
list.add_last(Node("sad"))
list.add_middle("b",Node("f"))
list.remove_node("f")
print(list)
