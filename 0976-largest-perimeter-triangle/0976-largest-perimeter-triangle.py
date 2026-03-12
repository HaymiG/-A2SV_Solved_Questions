class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        # to form triangle let say we have a , b, c
        # a+b>c , a+c>b , b+c>a
        nums.sort(reverse = True)
        for i in range(len(nums) - 2):
            if nums[i+2] + nums[i+ 1] > nums [i]:
                return  nums[i+2] + nums[i+1] + nums [ i]
        return 0
            
         
    

        
       
        
       
        