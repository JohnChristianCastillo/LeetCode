class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1. make a Counter object
        2. sort using min heap
        - add new item
        - if heap length exceeds k: heap pop
        """
        
        c = Counter(nums)
        heap = []

        for num, freq in c.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for freq, num in heap]


        
