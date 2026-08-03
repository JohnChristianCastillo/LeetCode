class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        first note: 1st idea was minheap + duplicate detection
        -> works but not O(n)
        
        edge cases: 
        1. duplicates -> use set()

        idea:
        make set from nums -> numset
        for each element in numset:
            if element-1 not in numset (means it has no predecessor) we pursue
                
        """

        numset = set(nums)

        longest = 0
        for n in numset:
            if n-1 not in numset:
                curr_length = 1
                curr = n
                while curr + 1 in numset:
                    curr = curr + 1
                    curr_length += 1
                longest = max(longest, curr_length)
        return longest

            
