class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles=sorted(piles,reverse=True)
    
        l,r=0,len(piles)-1
        ans=0
    
    
        while l<r:
        
            ans+=piles[l+1]
            l+=2
            r-=1
        
        return ans