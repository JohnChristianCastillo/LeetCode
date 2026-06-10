class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for a in asteroids:
            # cases:
            # negative: check last added element sign
            #       equal size: both explodes
            # positive: checked by next look
            
            # if negative
            if a < 0:
                is_destroyed = False
                while res and res[-1] > 0:
                    last = res[-1]
                    # will only clash if they're opposite signs
                    # we're only interested if last <= a
                    # notice we check < and == 
                    # because then we have to change the list
                    # if last > a then we just ingore a anyways
                    # we keep clashing until we can't
                    if abs(last) < abs(a):
                        res.pop()
                    elif abs(last) == abs(a):
                        res.pop()
                        is_destroyed = True
                        break
                    else: # last > a
                        is_destroyed = True
                        break # destroy a --> not add
                if not is_destroyed:
                    res.append(a)
            else:
                res.append(a)

        return res                
            
                            
                    