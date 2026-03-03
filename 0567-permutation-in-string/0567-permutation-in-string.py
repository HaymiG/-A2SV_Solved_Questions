class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dict = Counter(s1)
        s2dict = defaultdict(int)
        left = 0
        if len(s2) < len(s1):
            return False
        for right in range(len(s2)):
            s2dict[s2[right]] += 1

            if right - left + 1 > len(s1):
                s2dict[s2[left]] -= 1
                if s2dict[s2[left]] == 0:
                    del s2dict[s2[left]] 
                left += 1
            
            if s2dict == s1dict:
                return True
        return False


        

        
        