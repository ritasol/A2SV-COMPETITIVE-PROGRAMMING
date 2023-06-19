class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l=[0]
        for i in range(len(gain)):l.append(l[i]+gain[i])
        return max(l)
