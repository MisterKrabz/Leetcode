class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def sortDiagonal(r, c): 
            row = r
            col = c
            diagonal = []
            while r < len(mat) and c < len(mat[0]): 
                diagonal.append(mat[r][c])
                r += 1
                c += 1
            
            diagonal.sort()

            for element in diagonal: 
                mat[row][col] = element
                row += 1
                col += 1
        
        r = len(mat) - 1
        while r >= 0: 
            sortDiagonal(r, 0)
            r -= 1

        c = 0
        while c < len(mat[0]): 
            sortDiagonal(0, c)
            c += 1

        return mat
