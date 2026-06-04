class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        use prefix and postfix lists
        """
        pre = [0]
        post = [0]
        i = 0
        j = len(nums) - 1
        while i < len(nums):
            pre.append(pre[i]+nums[i])
            post.append(post[i]+nums[j])
            i += 1
            j -= 1
        
        post.reverse()
        for i in range(len(nums)):
            if pre[i] == post[i+1]:
                return i
        return -1