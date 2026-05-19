class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # idea: loop over a and b, each time taking their 1st bit, 
        # then comparing them to C's bit 
        # when c is 1 we only have to change (if none are 1) EITHER a or b's bit
        # BUT when c is 0, we have to check BOTH a and b's bit and set BOTH to 0 if necessary
        change = 0
        while b != 0 or a != 0 or c != 0:
            abit = 1 & a
            bbit = 1 & b
            cbit = 1 & c
            # cases: 
            """
            cbit = 1 --> abit or bbit should be set to 1. if both of them are 1 then it doesnt matter
            cbit == 0 --> abit AND bbit needs to be set to 0
            """
            if cbit:
                if not(abit or bbit): # abit and bbit are 0
                    change += 1
            else: # cbit = 0: make sure a and b are both 0
                if abit:
                    change += 1
                if bbit:
                    change += 1
            a = a // 2
            b = b // 2
            c = c // 2
        
        return change  