class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        indicies = []
        for i in range(len(matrix)): 
            for j in range(len(matrix[i])): 
                if matrix[i][j] == 0: 
                    indicies.append([i, j])

        for index in indicies: 
            row = index[0]
            column = index[1]

            r = row
            while r >= 0: 
                matrix[r][column] = 0
                r -= 1
            
            r = row
            while r < len(matrix):
                matrix[r][column] = 0
                r += 1
            
            c = column
            while c >= 0: 
                matrix[row][c] = 0
                c -= 1
            
            c = column
            while c < len(matrix[0]): 
                matrix[row][c] = 0
                c += 1
