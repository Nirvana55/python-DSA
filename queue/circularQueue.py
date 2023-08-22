#circular queue 

class circularQueue:
    def __init__(self, k:int) -> None:
        self.queue = [None] * k
        self.k = k
        self.Front = -1
        self.Rare = -1 

    def enqueue(self,x:int):
        if (self.Rare + 1) % self.k == self.Front:
           print("the data is full")
        elif self.Front == -1:
            self.Front = 0
            self.Rare = 0
            self.queue[self.Rare] = x
        else:
            self.Rare = (self.Rare + 1) % self.k
            self.queue[self.Rare] = x

    def dequeue(self):
        if self.Front == -1:
            print("the data is empty")
        elif self.Front == self.Rare:
            temp = self.queue[self.Front]
            self.Front = -1
            self.Rare = -1
            return temp
        else:
            temp = self.queue[self.Front]
            self.Front = (self.Front + 1) % self.k
            return temp



circQueue = circularQueue(4)
circQueue.enqueue(1)
circQueue.enqueue(2)
circQueue.enqueue(3)
circQueue.enqueue(4)
circQueue.enqueue(5)
print(circQueue.queue)
circQueue.dequeue()
circQueue.enqueue(5)
print(circQueue.queue)








