class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = {}
        col_set = {}
        square_set = {}

        row = len(board)
        col = len(board[0])

        for i in range(col): 
            col_set[i] = set()
        
        for j in range(row):
            row_set[j] = set()
        
        for i in range(row):
            for j in range(col):
                square = (i // 3) * 3 + (j // 3)

                if square not in square_set:
                    square_set[square] = set()

        for i in range(row):
            for j in range(col):
                if board[i][j] != ".":
                    if int(board[i][j]) < 10:
                        square = (i // 3) * 3 + (j // 3)
                        val = board[i][j]
                        if val in row_set[i] or val in col_set[j] or val in square_set[square]:
                            return False
                        row_set[i].add(val)
                        col_set[j].add(val)
                        square_set[square].add(val)
                    else:
                        return False
        return True
        