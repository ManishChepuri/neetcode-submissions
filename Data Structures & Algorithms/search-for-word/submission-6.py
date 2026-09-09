class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_idx = 0
        board_rows = len(board)
        board_cols = len(board[0])
        visited: [Tuple] = []

        def _backtrack(row: int, col: int, word_idx: int):
            if word_idx >= len(word):
                return True

            found = False

            if row - 1 >= 0 and (row - 1, col) not in visited and board[row - 1][col] == word[word_idx]: # Top letter
                visited.append((row, col))
                if _backtrack(row - 1, col, word_idx + 1):
                    found = True
                else:
                    visited.pop()
            if row + 1 < board_rows and (row + 1, col) not in visited and board[row + 1][col] == word[word_idx]: # Bottom letter
                visited.append((row, col))
                if _backtrack(row + 1, col, word_idx + 1):
                    found = True
                else:
                    visited.pop()
            if col - 1 >= 0 and (row, col - 1) not in visited and board[row][col - 1] == word[word_idx]: # Left letter
                visited.append((row, col))
                if _backtrack(row, col - 1, word_idx + 1):
                    found = True
                else:
                    visited.pop()
            if col + 1 < board_cols and (row, col + 1) not in visited and board[row][col + 1] == word[word_idx]: # Right letter
                visited.append((row, col))
                if _backtrack(row, col + 1, word_idx + 1):
                    found = True
                else:
                    visited.pop()

            return found

        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == word[0]:
                    word_idx = 1
                    if _backtrack(i, j, word_idx):
                        return True

        return False