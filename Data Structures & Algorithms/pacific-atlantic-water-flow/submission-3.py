class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        
        def dfs(r, c, prev_height, ocean):
            if (not (0 <= r < ROWS)
                or not (0 <= c < COLS)
                or (heights[r][c] < prev_height)
                or (r, c) in ocean):
                return

            ocean.add((r, c))

            dfs(r - 1, c, heights[r][c], ocean)
            dfs(r + 1, c, heights[r][c], ocean)
            dfs(r, c - 1, heights[r][c], ocean)
            dfs(r, c + 1, heights[r][c], ocean)

        # DFS from left and top
        pacific = set()
        for r in range(0, ROWS):
            dfs(r, 0, 0, pacific)
        for c in range(1, COLS):
            dfs(0, c, 0, pacific)
        print(pacific)

        atlantic = set()
        for r in range(0, ROWS):
            dfs(r, COLS - 1, 0, atlantic)
        for c in range(0, COLS - 1):
            dfs(ROWS - 1, c, 0, atlantic)

        return [[r, c] for r, c in pacific & atlantic]
    


