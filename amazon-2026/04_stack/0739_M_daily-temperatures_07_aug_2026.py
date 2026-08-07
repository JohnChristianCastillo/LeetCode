class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        stack holds currently unsolved temperatures
        each element: (temp, index)
        index cause we need to overwrite the temperatures list
        """
        st = []
        for i, temp in enumerate(temperatures):
            # check if we can "solve" items in our stack
            while st and st[-1][0] < temp:
                old_temp, old_index = st[-1]
                st.pop()
                temperatures[old_index] = i - old_index
            
            # add new temp on stack
            st.append([temp, i])
        # some might be unsolved
        while st:
            temp, index = st[-1]
            st.pop()
            temperatures[index] = 0
        return temperatures
