class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        idea: two pointers, one on each end
        if their sum is too high we move the right pointer inwards
        else: left pointer inwards
        """

        l, r = 0, len(numbers)-1
        while l < r:
            tot = numbers[r] + numbers[l]
            if tot == target:
                return [l+1, r+1]
            elif tot < target:
                l += 1
            else:
                r -= 1
        
        return 