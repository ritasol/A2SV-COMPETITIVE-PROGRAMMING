class Solution:
    def hourglassSum(self, grid, top_i, top_right_j, row, col):
        # First, Third row
        count = 0
        hourglass_sum = 0
        
        j = top_right_j - 2
        while j <= top_right_j:
            hourglass_sum += grid[top_i][j]
            hourglass_sum += grid[top_i + 2][j]
            j += 1
            
       # Middle
        hourglass_sum += grid[top_i + 1][top_right_j - 1]
        
        return hourglass_sum
    
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = 0
        
        row = len(grid)
        col = len(grid[0])
        
        for i in range(row):
            for j in range(2, col):
                if i + 2 >= row:
                    break
                cur_sum = self.hourglassSum(grid, i, j, row, col)
                max_sum = max(max_sum, cur_sum)
				
        return max_sum