from typing import *
class Solution:
    def __init__(self) -> None:
        self.result = 1000000000
    def splitArray(self, nums: List[int], k: int) -> int:
        min_ = 1000000000
        self.dp(nums, min_,0)
        return self.result
    def dp(self, nums, min_, start_indx):
        print('start_indx: ',start_indx)
        print('min_: ',min_)
        cur_num = max(sum(nums[start_indx:]), sum(nums[:start_indx]))
        print('cur_num: ',cur_num)
        if cur_num < self.result:
            min_ = cur_num
            self.result = min_
        print('self.result: ',self.result)
        if start_indx>=len(nums):
            return
        for i in range(start_indx, len(nums)):
            self.dp(nums, min_, i+1)

solution = Solution()
result = solution.splitArray([7,2,5,10,8],2)
print(result)