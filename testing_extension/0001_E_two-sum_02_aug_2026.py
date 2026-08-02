class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i,v in enumerate(nums):
            diff = target-v
            if diff in mp:
                return [mp[diff], i]
            else:
                mp[v] = i
        
        return 