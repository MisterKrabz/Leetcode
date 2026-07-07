class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i = 0
        while i < len(matrix) // 2: 
            temp = matrix[i]
            matrix[i] = matrix[len(matrix) - i - 1]
            matrix[len(matrix) - i- 1] = temp
            i += 1

        for r in range(len(matrix)): 
            c = r
            while c < len(matrix[r]): 
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp
                c += 1

        return matrix

