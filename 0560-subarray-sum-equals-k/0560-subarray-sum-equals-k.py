class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        sum_n = 0
        count = 0
        hashmap = {0:1}
        for r in range(n):
            sum_n += nums[r]
            if sum_n - k in hashmap:
               count += hashmap[sum_n-k]
            if sum_n in hashmap:
                hashmap[sum_n]+= 1
            else:
                hashmap[sum_n]= 1
        return count

            