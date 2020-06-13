class Solution:
    def exist(self, board, word):
        row = len(board)
        col = len(board[0])
        #print(row, col)
        #visited = [[False]*col for _ in range(row)]
        nv = row*col
        gotit = False
        for i in range(row):
            for j in range(col):
                visited = [[False]*col for _ in range(row)]
                gotit = self.checkIfExist(visited, board, word, nv, i, j)
                if gotit:
                    break
            if gotit:
                break
        return gotit

        #return self.checkIfExist(visited, board, word, nv, 0, 0)
    
    def checkIfExist(self, visited, a, w, nv, r, c):
        #if w == "":
        #    return True
        if nv == 0:
            return False
        visited[r][c] = True
        nv -= 1
        if a[r][c] == w[0]:
            w = w[1:]
            if w == "":
                return True

            nb = self.getNeighbours(visited, r, c)
            for n in nb:
                if self.checkIfExist(visited, a, w, nv, n[0], n[1]):
                    return True
        
        visited[r][c] = False
        nv += 1
        return False
                

    def getNeighbours(self, visited, r,c):
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


if __name__ == '__main__':
    sol = Solution()

    board = [ 
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    word = "ABCCED"
    word = "SEEF"
    r = sol.exist(board, word)
    print(r)
    