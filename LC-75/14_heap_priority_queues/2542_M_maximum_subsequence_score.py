class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        idea:
        0. sort nums1 and nums2 according to: nums2 descending order while also keeping the indexes synced with nums1
        1. nums2 is most important since it's the multiplier, we want this to be maximized
        2. when extending the window to K, nums1 should be prioritized for discardment 
        because we know we can't do anything about the new minimum we add (since nums2 will be sorted in descending order) 
        """
        curr_max_sum = -float("inf")
        n1_sum = 0

        max_heap = []
        for n1, n2 in zip(nums1, nums2):
            heapq.heappush(max_heap, (-n2,n1))

        min_heap = [] # used to be able to easily remove the minimum n1
        while max_heap:
            n2, n1 = heapq.heappop(max_heap)
            n2 = -n2  # make it have its original sign

            if len(min_heap) == k:
                mn1 = heapq.heappop(min_heap)
                n1_sum -= mn1
            # min heap will be of length k
            # we use min heap so we can pop the min element (n1) before adding to it the new combination
            # this is because n1 will affect more since the new element will have a smaller n2(multiplier) anyways
            heapq.heappush(min_heap, n1) 
            
            n1_sum += n1
            if len(min_heap) == k: # we can only update curr_max from the point where we actually have a window of size k
                curr_max_sum = max(curr_max_sum, n1_sum*n2)
            
        return curr_max_sum