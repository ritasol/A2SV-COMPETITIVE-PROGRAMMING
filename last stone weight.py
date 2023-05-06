import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in stones:
            if len(stones) < 2:
                return i
        for i in range(len(stones)):
            stones[i] = int(stones[i] * -1)
        heapq.heapify(stones)
        while len(stones) >= 2:
            st1 = heapq.heappop(stones)
            st2 = heapq.heappop(stones)
            new_st = st1-st2
            heapq.heappush(stones,new_st)
        return -1 * new_st
