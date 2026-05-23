class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1. use hashmap s.t.: hask[key] = index
        - INITIALIZE AS YOU GO
        - pros: the values inside it are the ones you have currently seen
        - so if there's a duplicate, say tar = 6, curr = 3, diff = 3
        - then if there's already a 3 inside the map, you're guaranteed
        - that it's not the same 3 you currently have and thus found a sol
        2. loop over nums
        - calculate difference
        - check if difference in hashmap
        - yes: return curr index + diff index
        - no: SAVE that val +  index; move next
        """

        mp = {}  # num -> index
        for i, v in enumerate(nums):
            diff = target - v
            if diff in mp:
                return [mp[diff], i] # since i comes later
            mp[v] = i
       