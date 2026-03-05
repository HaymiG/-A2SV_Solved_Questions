class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:  
            return 0
        if needle not in haystack:
            return -1
        
        left = 0
        right = 0
        ans = -1
        
        while left < len(haystack):
            if haystack[left] == needle[right]:
                left += 1
                right += 1
                if right == len(needle):  
                    return left - len(needle)
            else:
                left = left - right + 1
                right = 0
        return -1