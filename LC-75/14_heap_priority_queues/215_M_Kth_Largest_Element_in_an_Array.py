class Solution:
    # Operation           Function
    # ---------------------------------------------
    # Build Heap          heapq.heapify(x)          # 
    # Push                heapq.heappush(h, item)   # 
    # Pop                 heapq.heappop(h)          # 
    # Push + Pop          heapq.heappushpop(h, x)   # 
    # Pop + Push          heapq.heapreplace(h, x)   # 
    # Peek                h[0]                      # 
    # k Smallest          heapq.nsmallest(k, it)    # 
    # k Largest           heapq.nlargest(k, it)     # 

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # idea: construct heap from the list, pop until the kth element
        max_heap = []
        for v in nums:
            heapq.heappush(max_heap, -v)

        i = 1
        while i < k:
            i += 1
            heapq.heappop(max_heap)
        
        return -heapq.heappop(max_heap)
        
