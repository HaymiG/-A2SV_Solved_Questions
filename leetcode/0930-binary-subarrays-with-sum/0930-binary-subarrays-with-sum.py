class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashmap = {0:1}
        cur_sum = 0
        count = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum - goal in hashmap:
                count += hashmap[cur_sum - goal]
            if cur_sum in hashmap:
                hashmap[cur_sum] += 1
            else:
                hashmap[cur_sum] = 1
        return count
