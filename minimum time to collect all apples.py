class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        
        def dfs(node,par):
            ans = 0
            for nei in graph[node]:
               
                if nei != par:
                    ans += dfs(nei,node)
            if ans or hasApple[node]:
                ans += 2
                return ans
            return ans
        return max(dfs(0,-1)-2, 0)
