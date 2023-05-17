class Solution:
    def representative(self,x):
        while x!=self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
        
    def union(self,x,y):
        parent_x,parent_y = self.representative(x),self.representative(y)
        if parent_x!=parent_y:
            if parent_x>parent_y:
                parent_x,parent_y = parent_y,parent_x
        self.parent[parent_x] = parent_y
        
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        self.parent = [i for i in range(n)]
        
        for a,b in edges:
            self.union(a,b)
            
        return self.representative(start)==self.representative(end)
