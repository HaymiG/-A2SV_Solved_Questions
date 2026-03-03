class NumArray:

    def __init__(self, nums: List[int]):
        self.prifix=[]
        sum_cur = 0
        
        for i in range(len(nums)):
            sum_cur += nums[i]
            self.prifix.append(sum_cur)
            
            

    def sumRange(self, left: int, right: int) -> int:
        leftsum = self.prifix[left-1]if left > 0 else 0
        rightsum= self.prifix[right]
        return rightsum-leftsum
        
            


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)