class Solution:
    def resolves(self, a, b, operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        return int(a / b)

    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if len(token) == 1 and ord(token) < 48:
                num2 = stack.pop()
                num1 = stack.pop()
                cur_res = self.resolves(num1, num2, token)
                stack.append(cur_res)
            else:
                stack.append(int(token))
        return stack.pop()

