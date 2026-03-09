class Solution:
    def simplifyPath(self, path: str) -> str:
        new = path.split('/')
        stack = []
        for char in new:
            if char == "" or char == ".":
                continue
            
            if char == "..":
                if stack: stack.pop()

            else :
                stack.append(char)
        return  "/" + "/".join(stack) 
        