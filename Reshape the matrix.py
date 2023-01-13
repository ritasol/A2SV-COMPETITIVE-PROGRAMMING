class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]: 
        ans = []
        container = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                container.append(mat[i][j])
        
        if len(container) != r*c:
            return mat
        else:
            for i in range(r):
                ans.append(container[i*c:(i*c)+c])
            return ans