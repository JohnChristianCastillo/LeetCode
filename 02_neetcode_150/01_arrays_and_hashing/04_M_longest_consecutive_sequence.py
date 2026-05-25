class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        idea:
        1. put all numbers in a set for O(1) lookup
        2. loop over nums and treat a number as a 'start' only if (num - 1) is NOT in the set
           → this guarantees we only start counting at the beginning of a sequence
        3. from each start, count how long the consecutive chain goes: num, num+1, num+2, ...
        4. track the maximum chain length
        5. return the maximum
        """

        if not nums:
            return 0

        numset = set(nums)  # step 1: fast lookup
        max_length = 0

        # step 2: iterate over nums
        for n in nums:
            # only start counting if n is the BEGINNING of a sequence
            if (n - 1) not in numset:
                curr = n
                curr_length = 1

                # step 3: count consecutive numbers
                while (curr + 1) in numset:
                    curr += 1
                    curr_length += 1

                # step 4: update global max
                max_length = max(max_length, curr_length)

        return max_length
