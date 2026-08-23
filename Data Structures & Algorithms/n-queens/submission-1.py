class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        

        def queen(r,board):
            if n == r:
                copy= ["".join(row) for row in board ]   
                res.append(copy)
                return  

            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                queen(r+1, board)

                #backtrack
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."

        
        queen(0,board = [["."] * n for i in range(n)])
        return res