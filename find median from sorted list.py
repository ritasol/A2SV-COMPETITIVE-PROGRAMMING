from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.data = SortedList()

    def addNum(self, num: int) -> None:
        self.data.add(num)

    def findMedian(self) -> float:
        length = len(self.data)
        return self.data[length//2] if length%2 else (self.data[length//2] + self.data[length//2 - 1])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
