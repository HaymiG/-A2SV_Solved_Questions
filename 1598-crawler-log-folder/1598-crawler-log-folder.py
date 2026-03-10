class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for char in logs:
            if char != "../" :
                if char != "./": 
                    stack.append(char)
            elif char == "./":
                continue
            else:
                if stack:
                    stack.pop
        n = len(stack)
        return n - 1 if n > 0 else 0



        