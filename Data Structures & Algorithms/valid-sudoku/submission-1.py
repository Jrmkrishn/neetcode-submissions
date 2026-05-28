class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = defaultdict(set)
        c = defaultdict(set)
        box = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in r[row] or
                   board[row][col] in c[col] or
                   board[row][col] in box[(row//3, col//3)]):
                   return False
                r[row].add(board[row][col])
                c[col].add(board[row][col])
                box[(row//3, col//3)].add(board[row][col])
        return True