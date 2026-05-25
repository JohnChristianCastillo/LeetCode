class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for l, v in enumerate(nums):
            if v <= first:
                # we found a smaller first boundary
                # we take it since it will give us more
                # chance of finding a larger second
                first = v
            elif v <= second:
                second = v
            else: # we found the third index
                return True
        
        return False