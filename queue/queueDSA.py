class Queue:
    def __init__(self) -> None:
        self.items = []

    def create_queue(self) -> list:
        return self.items
    
    def check_size_queue(self) -> int:
        return len(self.items)
    
    def append_queue(self,value) -> list:
        self.items.append(value)
        return self.items
    
    def pop_queue(self) -> list:
        size_of_queue = len(self.items)
        if size_of_queue == 0:
           return "No queue found"
        self.items.pop(0)
        return self.items

# Creating instance
queue1 = Queue()
print(queue1.create_queue())
print(queue1.append_queue(1))
print(queue1.check_size_queue())
print(queue1.pop_queue())
print(queue1.pop_queue())
print(queue1.check_size_queue())