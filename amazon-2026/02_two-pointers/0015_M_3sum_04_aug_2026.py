class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        idea:
        1. it is easy because we dont need to return the indices
            -> sort the list
        2. loop over each element until 3 elements left so until len(nums)-3
            perform two sum II (two pointer)
        NOTE: DO NOT FORGET TO CHECK FOR DUPLICATES
        - once before while loop starts to check if new anchor is good
        - another when new elements in two sum are being chosen
        """
        nums = sorted(nums)
        
        sols = []
        for i, v in enumerate(nums):
            # !!!to avoid duplicate triplets, avoid duplicate anchors
            if i > 0 and v == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                curr = v + nums[l] + nums[r]
                if curr == 0:
                    sols.append([v, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # !!!make sure new indexes are not duplicates
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

                elif curr < 0:
                    l += 1
                else:
                    r -= 1
        return sols