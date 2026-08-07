class Solution:
    def isValid(self, s: str) -> bool:
        closer = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        closing_brackets = (')', ']', '}')

        st = []
        for ch in s:
            if ch in closing_brackets:
                if not st or st[-1] != closer[ch]:
                    return False
                st.pop()
            else:
                st.append(ch)
        return True if not st else False