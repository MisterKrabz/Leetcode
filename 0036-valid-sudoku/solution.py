class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = []
        columnSets = []
        squareSets = [[set(), set(), set()], [set(), set(), set()], [set(), set(), set()]]

        for i in range(9): 
            rowSets.append(set())
            columnSets.append(set())

        i = 0
        while i < len(board): 
            j = 0
            while j < len(board[i]): 
                if board[i][j] == ".": 
                    j += 1
                    continue
                if board[i][j] in rowSets[i]: 
                    return False
                if board[i][j] in columnSets[j]: 
                    return False
                if board[i][j] in squareSets[i // 3][j // 3]: 
                    return False
                
                rowSets[i].add(board[i][j])
                columnSets[j].add(board[i][j])
                squareSets[i // 3][j // 3].add(board[i][j])

                j += 1
            i += 1

        return True
