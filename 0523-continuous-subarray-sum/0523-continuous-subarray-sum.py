class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prifix = 0
        count = {0 : -1}
        for right in range(n):
            prifix += nums[right]
            rem = prifix % k
            if rem in count:
                if right - count[rem] >= 2:
                    return True
            else:
                count[rem] = right
        return False
                    


        


            

                

                

        