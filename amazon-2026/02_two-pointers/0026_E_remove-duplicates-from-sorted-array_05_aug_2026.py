class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        insert_pos = 0
        for i, curr in enumerate(nums):
            if curr != prev:
                prev = curr
                nums[insert_pos] = curr
                insert_pos += 1

        return insert_pos

