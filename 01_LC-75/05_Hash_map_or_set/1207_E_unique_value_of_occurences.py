class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # use Counter() == dict that has 
        # key each element in list and 
        # val = amount of that element present in the list
        # then use a set to check whether the value of each keys
        # are unique
        count = Counter(arr)
        seen = set()
        for v in count:
            if count[v] in seen:
                return False
            else:
                seen.add(count[v])
        return True