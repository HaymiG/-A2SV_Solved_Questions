class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashmap = {0 : 1}
        sum_s = 0 
        count = 0
        remainder = 0
        for i in range(len(nums)):
            sum_s += nums[i]
            remainder = sum_s % k
            if remainder in hashmap :
                count += hashmap[remainder]
                hashmap[remainder] += 1
            else:
                hashmap[remainder] = 1
            
                
            
            
               
        return count

        