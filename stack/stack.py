class Stack:
    def __init__(self) -> None:
        self.items = []

    def create_stack(self) -> list:
        return self.items
    
    def check_stack_size(self) -> int:
        size_stack = len(self.items)
        return size_stack
    
    def append_value_stack(self,value) -> list:
        self.items.append(value)
        return self.items
    
    def pop_value_stack(self) -> list:
        size_of_stack = len(self.items)
        if size_of_stack == 0:
            return "Stack is empty"
        
        self.items.pop()
        return self.items
    
# Creating instance
stack1 = Stack()
print(stack1.create_stack())
print(stack1.append_value_stack(2))
print(stack1.check_stack_size())
print(stack1.pop_value_stack(2))
print(stack1.check_stack_size())


    

    
