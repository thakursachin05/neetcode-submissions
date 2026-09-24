class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cordinates = [[1,0], [-1,0], [0,1], [0, -1]]
        n, m = len(board), len(board[0])

        def dfs(i,j, curr, visited, word):
            if i >= n or i < 0 or j < 0 or j >= m or (i,j) in visited:
                return False

            if board[i][j] != word[len(curr)]:
                return False
            
            curr.append(board[i][j])
            visited.add((i,j))

            if len(curr) == len(word):
                return True

            for (x,y) in cordinates:
                if dfs(i+x, j+y, curr, visited, word):
                    return True

            visited.remove((i, j))
            curr.pop()
            return False
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited = set()
                    if dfs(i, j, [], visited, word):
                        return True
        return False
            