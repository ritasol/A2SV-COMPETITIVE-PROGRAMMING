class Solution:
    def shortestBridge(self, g: List[List[int]]) -> int:
        n,a,b = len(g),[],[]
        def f(i,j,p):
            if 0<=i<n and 0<=j<n and g[i][j]:
                g[i][j] = 0
                p.append((i,j))
                any(f(x,y,p) for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)))
        any(f(i,j,b if a else a) for i in range(n) for j in range(n))
        return min(abs(x-i)+abs(y-j)-1 for x,y in a for i,j in b)
