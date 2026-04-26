class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        Idea:
        Stack: To keep track of rooms you can and still need to visit 
        (dynamically adjusts depending on newly explored rooms and keys within it)
        
        Set: To keep track of already visited rooms (avoids endless loop)
        """

        stk = [0] # since room 0 is unlocked
        visit = set()

        while stk:
            room_id = stk.pop()
            
            visit.add(room_id)
            # add keys in this room to the stack only if they havent been visited yet
            for key in rooms[room_id]:
                if key not in visit:
                    stk.append(key)
        
        return len(visit) == len(rooms)
