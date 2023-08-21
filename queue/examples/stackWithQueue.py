#Leet Code Level: Easy

#Question: Implement stack using two Queues and need to do it with queue principle

#Algorithm:
#step1: initialize two queues
#step2: append element to queue2 and swap element of q2 to q1 until the append has finished
#step3: pop element and top the element.
#step4: need to check if queue is empty.
#step6: end

class MyStack:
    def __init__(self) -> None:
        self.queue1 = []
        self.queue2 = []
    
    def push(self, x: int) -> None:
        self.queue2.append(x)
        while self.queue1:
             self.queue2.append(self.queue1.pop(0))
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        return self.queue1.pop(0)

    def top(self) -> int:
        return self.queue1[0]
    
    def empty(self) ->int:
        return len(self.queue1) == 0
    
s1 = MyStack()

print(s1.push(1))
print(s1.push(2))
print(s1.push(3))
print(s1.pop())
print(s1.top())
print(s1.empty())







