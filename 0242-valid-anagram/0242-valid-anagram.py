class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        my_dict = defaultdict(int)

        for i in s:
            my_dict[i] += 1

        for j in t :
            if j not in my_dict or my_dict[j] == 0 :
                return False
            my_dict[j] -= 1
        return True
        
            
