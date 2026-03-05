class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start = 0
        cur = 0
        prifix = []
        for i in range(len(nums)):
         
            cur += nums[i]
            prifix.append(cur)
            start = min(start , cur)
        return -start + 1
           


        # for i in range(len(prifix)):
        #     if prifix[i] <= 0:
        #         start += 1 
        #         continue
            
                
        
        