from string import ascii_lowercase
class Solution:
    def findWords(self, board, words):
        row = len(board)
        col = len(board[0])

        res = set()
        wdb = {}
        visited = None
        for c in ascii_lowercase:
            t = {w for w in words if w[0] == c}
            if len(t) > 0:
                wdb[c] = t

        def getNeighbours(r,c):
            n = []
            if r > 0 and not visited[r-1][c]:
                n.append([r-1, c])
            if c > 0 and not visited[r][c-1]:
                n.append([r, c-1])
            if r < len(visited) - 1 and not visited[r+1][c]:
                n.append([r+1, c])
            if c < len(visited[0]) - 1 and not visited[r][c+1]:
                n.append([r,c+1])
            return n

        def findWords(r, c, cw):
            lst = wdb[cw[0]]
            if cw in lst:
                res.add(cw)

            nb = getNeighbours(r, c)
            for n in nb:
                x,y = n
                nc = board[x][y]
                
                if any(w.startswith(cw+nc) for w in lst):
                    visited[x][y] = True
                    findWords(x,y, cw+nc)
                    visited[x][y] = False

        for i in range(row):
            for j in range(col):
                if board[i][j] in wdb:
                    visited = [[False]*col for _ in range(row)]
                    visited[i][j] = True
                    findWords(i, j, board[i][j])
        return res


if __name__ == '__main__':
    sol = Solution()

    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]
    r = sol.findWords(board, words)
    print(r)
    