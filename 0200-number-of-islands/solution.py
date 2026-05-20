class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def search(r, c):
            stack = [[r,c]]
            grid[r][c] = "0"
            while(stack): 
                current = stack.pop()
                r = current[0]
                c = current[1]
                if r > 0 and grid[r-1][c] == "1": 
                    stack.append([r-1, c])
                    grid[r-1][c] = "0"
                if r < len(grid) - 1 and grid[r+1][c] == "1":
                    stack.append([r+1, c])
                    grid[r+1][c] = "0"
                if c > 0 and grid[r][c-1] == "1": 
                    stack.append([r, c-1])
                    grid[r][c-1] = "0"
                if c < len(grid[0]) - 1 and grid[r][c + 1] == "1":
                    stack.append([r, c+1])
                    grid[r][c+1] = "0"
        
        count = 0
        for row in range(len(grid)): 
            for col in range(len(grid[row])): 
                if grid[row][col] == "1": 
                    search(row, col)
                    count += 1
        return count


        
