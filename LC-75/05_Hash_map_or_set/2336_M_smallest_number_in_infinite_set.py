class SmallestInfiniteSet:
    """
    idea:
    1. when popping: 
        save current smallest
        add smallest to the removed set
        increment the smallest until we find a value not in the removed set
        return saved smallest
    2. when adding back: look if the number is in the removed set
        if so: check if it's smaller than our current smallest
    """
    def __init__(self):
        self.smallest = 1
        self.removed = set()
    def popSmallest(self) -> int:
        # return the current smallest +  remove it from inf list
        prev = self.smallest
        self.removed.add(self.smallest)
        while self.smallest in self.removed:
            self.smallest += 1
        
        return prev

    def addBack(self, num: int) -> None:
        if num in self.removed:
            self.removed.remove(num)
        if num < self.smallest:
            self.smallest = num
