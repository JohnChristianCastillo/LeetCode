class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        sol = []
        curr_letter = 0 # index of searchWord
        l, r = 0, len(products) # sliding window [l, r)
        prefix = ""
        for ch in searchWord:
            prefix += ch
            while l < r and not products[l].startswith(prefix):
                # go over all sorted products
                # eliminate LEFT products that are not matching current letter
                l += 1
            while l < r and not products[r-1].startswith(prefix):
                # filter out all not matching right productd
                r -= 1
            right_bound = min(r, l + 3)
            sol.append(products[l:right_bound])
        return sol