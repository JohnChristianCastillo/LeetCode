class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        use map<value, count>
        calculate difference, and see if it's in map

        OR you could sort the array, then use 2 pointers 
        where if the sum is smaller than target, you move left pointer
        otherwise move right pointer
        """
        mp = Counter(nums)
        matches = 0
        for v in nums:
            # !!! first verify if v is actually still available
            if mp[v] <= 0:
                continue
            diff = k - v
            # special case where diff == v
            # we need to have atleast 2 copies of v
            if v == diff:
                if mp[v] >= 2:
                    mp[v] -= 2
                    matches += 1
            else:
                if diff in mp and mp[diff] > 0: # !!! 
                # can go less than 0 but that still exists so check it
                    matches += 1
                    # remove both v and diff's instances from map
                    mp[diff] -= 1
                    mp[v] -= 1
        
        return matches