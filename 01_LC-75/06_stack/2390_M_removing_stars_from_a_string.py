class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for v in s:
            if v == '*':
                if st:
                    st.pop()
            else:
                st.append(v)
        
        return "".join(st)