class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        result = []

        def isValid(i,j,board):
            for row in range(i):
                if board[row][j] == 'Q':
                    return False
            row, col = i-1, j-1

            while row >= 0 and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row, col = row - 1, col - 1
            
            row, col = i-1,j+1

            while row >= 0 and col < n:
                if board[row][col] == 'Q':
                    return False
                row, col = row - 1, col + 1
            return True



        def dfs(i):
            if i == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            for j in range(n):
                if isValid(i,j,board):
                    board[i][j] = 'Q'
                    dfs(i+1)
                    board[i][j] = '.'
        
        dfs(0)

        return result
            
        
        

        
        