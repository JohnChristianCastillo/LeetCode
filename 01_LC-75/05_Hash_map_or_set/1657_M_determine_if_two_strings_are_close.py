class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        limitations:
        1. position swapping
        2. transform all occurence of existing char into ANOTHER EXISTING char

        idea:
        multiple conditions we need to pass
        1. |word1| == |word2|
            - len()
        2. letters in word 1 is same in word 2
            - use set()
        3. the counts of each letters are the same
            - use Counter to count each letter (Counter())
            - accumulate the values of each key (2 lists)
            - check if the 2 lists are the same
            -- make sure to sort the unordered list
        """
        # 1.
        if not len(word1) == len(word2):
            return False
        # 2.
        if not set(word1) == set(word2):
            return False
        # 3. 
        c1 = Counter(word1)
        c2 = Counter(word2)
        l1, l2 = [], []
        for v in c1:
            l1.append(c1[v])
        for v in c2:
            l2.append(c2[v])
        l1.sort(), l2.sort()
        if not l1 == l2:
            return False
        return True