from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr = []
        for token in tokens:
            if self.is_number(token):
                arr.append(int(token))
            else:
                e1,e2 = arr.pop(), arr.pop()
                e3=0
                if token =="+":
                    e3 = e1+e2
                elif token == "*":
                    e3 = e1*e2
                elif token == "-":
                    e3 = e2 - e1
                else:
                    e3 = int(e2/e1)
                arr.append(e3)
        
        return arr.pop()

    def is_number(self, str):
        try:
            int_value = int(str)
            return True
        except ValueError:
            return False

print(Solution().evalRPN(["2","1","+","3","*"]))