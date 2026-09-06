class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        cols = len(board[0])

        visited = set()

        def dfs(i, j):
            stack = [(i, j)]
            region = []
            touches_border = False

            while stack:
                r, c = stack.pop()

                if (r, c) in visited:
                    continue

                visited.add((r, c))
                region.append((r, c))

                # Does this region touch the outer border?
                if (
                    r == 0
                    or r == rows - 1
                    or c == 0
                    or c == cols - 1
                ):
                    touches_border = True

                # Up
                if r - 1 >= 0 and board[r - 1][c] == "O":
                    stack.append((r - 1, c))

                # Down
                if r + 1 < rows and board[r + 1][c] == "O":
                    stack.append((r + 1, c))

                # Left
                if c - 1 >= 0 and board[r][c - 1] == "O":
                    stack.append((r, c - 1))

                # Right
                if c + 1 < cols and board[r][c + 1] == "O":
                    stack.append((r, c + 1))

            # Only capture region if it never touched border
            if not touches_border:
                for r, c in region:
                    board[r][c] = "X"

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i, j) not in visited:
                    dfs(i, j)
