import heapq

'''
Flattens all the values into one array and heapify that.
since this is min heap, hence keep removing k-1 elements from heap (from top)
after that the top of heap element would be Kth smallest number 
'''

class Solution:
    def solve(self, board):
        if not board:
            return
        m = len(board)
        n = len(board[0])
        visited = [ [False]*n for _ in range(m)]
        queue = []
        def getNbrs(x, y):
            return [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and visited[i][j] == False:
                    queue.append((i, j))
                    visited[i][j] = True
                    flip = []
                    flag = True
                    while queue:
                        x, y = queue.pop()
                        
                        if (0 < x < m-1) and \
                            (0 < y < n-1):
                            flip.append((x, y))
                        else:
                            flip = []
                            flag = False
                        for tx, ty in getNbrs(x, y):
                                if (0 <= tx < m) and (0 <= ty < n):
                                    if board[tx][ty] == 'O' and not visited[tx][ty]:
                                        queue.append((tx, ty))
                                        visited[tx][ty] = True
                    while flip and flag:
                        x, y = flip.pop()
                        board[x][y] = 'X'

                





if __name__ == '__main__':
    sol = Solution()
    
    X = 'X'
    O = 'O'
    board = [
        [X, X, X, X],
        [X, O, O, X],
        [X, X, O, X],
        [X, O, X, X]
    ]
   
    board = [["X","O","X"],["X","O","X"],["X","O","X"]]
    board = [["O","X","X","O","X"],
             ["X","O","O","X","O"],
             ["X","O","X","O","X"],
             ["O","X","O","O","O"],
             ["X","X","O","X","O"]]
    sol.solve(board)
    print(board)