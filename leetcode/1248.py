class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        result = []
        self.func(nums,0,[],result,k,0,0)
        return result
    
    def func(self, nums, startindex, path, result, k,count,index):
        if count == k:
            result.append(path[:])
        if startindex == len(nums):
            return
        for i in range(startindex,len(nums)):
            # print('i: ',i)
            if i == index+1 or i==0:
                print('index: ',index,'i: ',i)
                print('path: ',path)
                # print(f'result{i}:',result)
                if nums[i]%2 != 0:
                    count+=1
                path.append(nums[i])
                self.func(nums,i+1, path,result,k,count,i)
                if nums[i]%2 != 0:
                    count-=1
                path.pop()

sample =[2,2,2,1,2,2,1,2,2,2]
k=2
# sample = [1,1,2,1,1]
# k=3
solution = Solution()
result = solution.numberOfSubarrays(sample,k=k)
print(result)
print(len(result))