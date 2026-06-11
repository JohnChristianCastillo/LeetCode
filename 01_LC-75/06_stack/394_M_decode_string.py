class Solution:
    def decodeString(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        stack = []

        # idea:
        """
        encounter first ']'
        construct the string that matches it '['
        use the multipler after the closing brace
        """
        ret = ""
        for c in s:
            # print("curr_stack: ", ''.join(stack))
            if c != ']':
                stack.append(c)
            else:
                new_substr = ""
                while stack[-1] != '[':
                    new_substr = stack.pop() + new_substr
                # print("new: ", new_substr)
                # print("got out:", stack)
                # now we know stack[-1] == [
                stack.pop()
                # now we are at the multiplier
                multiplier = ""
                while stack and stack[-1].isdigit():
                    # print("multiplier: ", stack )
                    multiplier = stack.pop() + multiplier
                new_substr = new_substr * int(multiplier) 
                for v in new_substr:
                    stack.append(v)
        return ''.join(stack)