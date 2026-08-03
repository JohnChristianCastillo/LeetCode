class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i, v in enumerate(nums):
            need = target - v
            if need in mp:
                return [mp[need], i]
            else:
                mp[v] = i
                # notice we dont check if there's a duplicate
                # 1. if solution was 2x of same number then 1st if find this
                # 2. if sol was not duplicate then we can return any indice
                #  -- say sol = 2+3 and input was 2,2,3 -> can be either index 0 or 1 pair with 2
        return 