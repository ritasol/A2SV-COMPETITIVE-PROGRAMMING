import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap=[]
        count={}
        for i in words:
            if i in count:
                count[i] += 1
            else:
                count[i]= 1
        for key,val in count.items():
            heapq.heappush(heap,(-1 * val,key))
        ans = []
        while k > 0:
            val = heapq.heappop(heap)[1]
            ans.append(val)
            k-=1
        return ans
