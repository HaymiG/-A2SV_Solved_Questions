class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        cur_sum = 0
        min_length = float("inf")
        left = 0 
        for right in range(n):
            cur_sum += nums[right]
            while cur_sum >= target :
                min_length = min(min_length , right - left + 1)
                cur_sum -= nums[left]
                left += 1
        return 0 if min_length == float("inf") else min_length