'''Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]
 
Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.'''
from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        '''we can use the dynamic programing:
        give a two dimention'''
        n = len(nums)
        nums = sorted(nums)
        max_index = 0
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j]+1)
            if dp[max_index]< dp[i]:
                max_index = i
        # max_index is the longest 
        m = max_index
        count = dp[max_index]
        result = []
        while count:
            if nums[max_index] % nums[m] == 0:
                result.append(nums[m])
                count-=1
            m -= 1
                
        return result


nums = [1,2,3]
solution = Solution()
result = solution.largestDivisibleSubset(nums)
print(result)