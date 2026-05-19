class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        return: list s.t. list[i] = #days to wait before day i get warmer temp
            --> use original list as answers

        idea: use stack s.t contents = (temp_i, index)
        1. place day 0 in stack
        2. loop over from day 1 to n
            while day 1's temp > top of stack:
                # NOTICE that the stack can't have multiple elements unless
                the new element is COLDER than the older element

                top_temp, top_index = stk.pop() # (temp, index)
                days_needed = curr_day_temp - top_temp
                temperatures[top_index]= days_needed # constant space
        3. check the stack if there are still elements, if so set them to 0
        """

        stk = [(temperatures[0], 0)]
        for i in range(1, len(temperatures)):
            curr_temp = temperatures[i]
            while stk and stk[-1][0] < curr_temp:
                top_temp, top_index = stk.pop()
                temperatures[top_index] = i - top_index # days to wait
            stk.append((temperatures[i], i))
        while stk: # no future days -> set to 0
            top_temp, top_index = stk.pop()
            temperatures[top_index] = 0
        return temperatures