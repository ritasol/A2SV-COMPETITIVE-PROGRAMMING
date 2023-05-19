class Solution:
    def representative(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.representative(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        parent_x,parent_y = self.representative(x),self.representative(y)
        if parent_x == parent_y:
            return 
        if self.rank[parent_x] == self.rank[parent_y]:
            self.parent[parent_x] = parent_y
            self.rank[parent_y] += 1
        if self.rank[parent_x] > self.rank[parent_y]:
            self.parent[parent_y] = parent_x
        else:
            self.parent[parent_x] = parent_y

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        self.parent = [i for i in range(n+1)]
        self.rank = [0 for _ in range(n+1)] 
        minn = inf
    
        for x,y,z in roads:
            self.union(x,y)

        rep_1 = self.representative(1)
        for x,y,z in roads:
            rep_2 = self.representative(x)
        
            if rep_1 == rep_2:
                minn = min(minn,z)

        return minn
