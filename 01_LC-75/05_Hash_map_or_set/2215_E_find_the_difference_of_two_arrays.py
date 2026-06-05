class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        nums1 = []  # we repurpose the original containers
        nums2 = []
        for v in s1:
            if v not in s2:
                nums1.append(v)
                s2.add(v) # avoid duplicates
        for v in s2:
            if v not in s1:
                nums2.append(v)
                s1.add(v)
        
        return [nums1, nums2]