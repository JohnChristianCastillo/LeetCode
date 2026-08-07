class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ('+', '-', '*', '/')
        params = []

        for i, token in enumerate(tokens):
            if token in ops:
                a, b = params[-2], params[-1]
                params.pop()
                params.pop()
                res = 0
                if token == '*':
                    res = a*b
                elif token == '+':
                    res = a+b
                elif token == '/':
                    res = int(a/b)
                else:
                    res = a-b
                # print(a, token, b, "=", res)
                
                params.append(res)
            else:
                params.append(int(token))
        return params[-1]
