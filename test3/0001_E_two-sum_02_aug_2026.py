class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        convert nums s.t. it also holds the index
        """
        for i, v in enumerate(nums):
            nums[i] = [v, i]
        nums.sort()
        l, r = 0, len(nums)-1

        while l < r:
            _sum = nums[l][0] + nums[r][0]
            if _sum < target:
                l += 1
            elif _sum > target:
                r -= 1
            else:
                return [nums[l][1], nums[r][1]]
        return []