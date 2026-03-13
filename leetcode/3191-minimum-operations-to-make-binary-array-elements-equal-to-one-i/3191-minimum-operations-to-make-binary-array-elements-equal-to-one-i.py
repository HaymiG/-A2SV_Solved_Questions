class Solution:
    def minOperations(self, nums: List[int]) -> int:

        def flip(nums , i):
            if nums[i] == 0 :
                nums[i] = 1
            else : nums[i] = 0
        
        count = 0
        n = len(nums)
        for i in range(n - 2):
            if nums[i] == 0 :
                flip(nums , i )
                flip(nums , i + 1)
                flip(nums , i + 2)
                count += 1
             
        return count if (nums[n - 2] == 1 and nums[n - 1] == 1) else -1