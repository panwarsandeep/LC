class Solution:
    def solveNQueens(self, n):
        def is_safe(qpos, r, c):
            for qr, qc in qpos:
                if abs(qr - r) == abs(qc - c) or \
                    qr == r or qc == c:
                    return False
            return True

        def solve(board, n, res):
            if n >= len(board):
                res.append([''.join(x) for x in board])
            for i in range(len(board)):
                if is_safe(queens_pos, n, i):
                    board[n][i] = 'Q'
                    queens_pos.append((n, i))
                    solve(board, n+1, res)
                    board[n][i] = '.'
                    queens_pos.pop()

        board = [['.']*n for _ in range(n)]
        queens_pos = []
        res = []
        solve(board, 0, res)
        return res

   

if __name__ == '__main__':
    sol = Solution()
    
    n = 4
    print(n)
    r = sol.solveNQueens(n)
    print(r)
    

