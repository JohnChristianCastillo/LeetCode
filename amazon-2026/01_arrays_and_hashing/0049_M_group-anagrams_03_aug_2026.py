class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for word in strs:
            sort = ''.join(sorted(word))
            if sort in hm:
                hm[sort].append(word)
            else:
                hm[sort] = [word]
        
        res = []
        for key in hm:
            res.append(hm[key])

        return res