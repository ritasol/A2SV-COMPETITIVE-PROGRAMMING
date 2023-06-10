class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in grid:
            begin = 0
            end = len(i) - 1
            ans = -1
            while begin <= end:
                mid = int(begin+ (end - begin)/2)
                if i[mid] < 0:
                    end = mid - 1
                    ans = mid
                else:
                    begin = mid + 1
            if ans != -1:
                count+= len(i) - ans
        return count
