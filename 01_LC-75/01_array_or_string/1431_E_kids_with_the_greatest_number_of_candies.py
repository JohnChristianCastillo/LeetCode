class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        greatest: greater than OR EQUAL to
        idea:
        1. find the maximum element -> this will be the metric to compare with
        2. loop over the list again and check 1 by 1 if list[i] >= max element
            -> update the ORIGINAL list to True or False (O(1) space, O(2n) time)
        """
        max_element = max(candies)  # O(1) space
        for i in range(len(candies)): # O(1) space
            candies[i] = candies[i] + extraCandies >= max_element # O(1) time
        
        return candies