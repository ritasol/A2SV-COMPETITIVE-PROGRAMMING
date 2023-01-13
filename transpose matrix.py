class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        ans = ([] * len(matrix) for i in range(len(matrix[0])))
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                ans.append(matrix[j][i])
        return ans