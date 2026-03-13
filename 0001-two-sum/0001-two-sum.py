class Solution(object):
    def twoSum(self, nums, target):
        hashmap = defaultdict(int)
        for i in range(len(nums)):
            reminder = target - nums[i]
            if reminder in hashmap:
                return [hashmap[reminder] , i]
            hashmap[nums[i]] = i
            

