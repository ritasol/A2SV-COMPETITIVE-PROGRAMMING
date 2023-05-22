from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        cnt=sorted(cnt,key=lambda x : cnt[x],reverse =True)
        return cnt[:k]
        
        
