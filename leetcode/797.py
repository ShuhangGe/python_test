class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph)-1
        print(n)
        result = []
        def func(path, node):
            # print(node)
            if node == n:
                result.append(path.copy())
                return 
            for i in graph[node]:
                path.append(i)
                print('path2: ',path)
                func(path, i)
                path.pop()
        func([0],0)
        return result
solution = Solution()
print(solution.allPathsSourceTarget([[1,2],[3],[3],[]]))