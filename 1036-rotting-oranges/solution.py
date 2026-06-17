class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh = set()
        rotten = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh.add((r, c))
                elif grid[r][c] == 2:
                    rotten.append((r, c))

        if not fresh:
            return 0

        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while rotten and fresh:
            next_rotten = []

            for r, c in rotten:
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (nr, nc) in fresh:
                        fresh.remove((nr, nc))
                        next_rotten.append((nr, nc))

            rotten = next_rotten
            minutes += 1

        if fresh:
            return -1

        return minutes
