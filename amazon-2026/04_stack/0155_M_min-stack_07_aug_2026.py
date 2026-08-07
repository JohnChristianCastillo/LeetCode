class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MinStack:

    def __init__(self):
        self.head = None
        self.minheap = []
        self.removed = {}

    def push(self, value: int) -> None:
        # update heap
        heapq.heappush(self.minheap, value)
        node = Node(value)
        node.prev = self.head
        if self.head:
            self.head.next = node
        self.head = node
        # print(self.minheap)

    def pop(self) -> None:
        val = self.head.val
        self.removed[val] = self.removed.get(val, 0) + 1

        self.head = self.head.prev
        if self.head:
            self.head.next = None
        

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        while self.minheap and self.removed.get(self.minheap[0], 0):
            self.removed[self.minheap[0]] -= 1
            heapq.heappop(self.minheap)
        return self.minheap[0] if self.minheap else None
            
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()