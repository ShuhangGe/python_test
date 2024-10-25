from typing import *
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> int:
        results = []
        self.helper(nums,target,[],results)
        return results
    def helper(self,nums,target,path,results):
        print(path)
        print(target)
        if target==0:
            results.append(path[:])
            return
        elif target<0:
            return
        for i in nums:
            path.append(i)
            self.helper(nums,target-i,path,results)
            path.pop()

class Solution2:
    def combinationSum(self, nums: List[int], target: int) -> int:
        results = []
        self.helper(nums,target,[],results)
        return results
    def helper(self,nums,target,path,results):
        print(path)
        print(target)
        if sum(path)==target:
            results.append(path[:])
            return
        elif sum(path)>target:
            return
        for i in nums:
            path.append(i)
            self.helper(nums,target,path,results)
            path.pop()

solution = Solution2()
result = solution.combinationSum([1,2,3],4)
print(result)
