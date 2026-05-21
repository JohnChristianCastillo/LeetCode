class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        1. flowers can't be adjacent
        2. return: True if you can place n extra flowers
        """
        prev = 0
        for i in range(len(flowerbed)-1): 
        # we do the last bed outside to avoid extra conditional per loop
            nxt = flowerbed[i+1]
            # prev = 0 AND next = 0 AND curr = 0 
            if not prev and not nxt and not flowerbed[i]: 
                n -= 1
                flowerbed[i] = 1  # MAKE SURE TO UPDATE THE FLOWERBED
            prev = flowerbed[i]
            
        if not prev and not flowerbed[-1]:
            n -= 1
        
        return n <= 0
                