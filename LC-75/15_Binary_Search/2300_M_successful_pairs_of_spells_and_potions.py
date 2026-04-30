class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # spell[i] == strength of spell
        # potions[j] == strength of potion
        # success: if product of spell[i]*potion[j] is successful (prod >= success)

        # idea: 
        # 1. sort potions (not the spells since they are our anchor)
        # 2. Binary search through list (remember 1st solution isn't necessarily the earliest)!!!
        potions.sort()
        
        for i in range(len(spells)):
            # we just initialize our "solution" to 0 and at the end of the potions loop
            # it doesnt matter if we find one or not, we just assign spells[i] = sol
            l,r = 0, len(potions)-1
            sol = 0
            while l <= r:
                mid = l + (r-l)//2
                prod = spells[i]*potions[mid]
                if prod >= success:
                    sol = len(potions) - mid
                    r = mid - 1 # we don't break since it's possible an earlier solutione xists
                else: # we know l is too low
                    l = mid+1
            spells[i] = sol
        return spells

