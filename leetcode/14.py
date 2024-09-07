from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        result = 0
        nums.sort()
        min_sum = 100000
        for i in range(n-1):

            if i>0 and nums[i-1]==nums[i]:
                continue
            left = i+1
            right = n-1
            while left<right:
                sum_ = nums[i]+nums[left]+nums[right]
                if abs(sum_-target)<min_sum:
                    min_sum = abs(sum_-target)
                    result = sum_
                if sum_>target:
                    right -= 1
                elif sum_<target:
                    left += 1
                else:
                    while left<right and nums[left]==nums[left+1]:
                        left +=1
                    while left<right and nums[right] == nums[right-1]:
                        rigtht -= 1
                    left+=1
                    right-=1
        return result

solution  = Solution()
print(solution.threeSumClosest([1,1,1,1],-100))