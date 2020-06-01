class Solution:
    def getNeighbours(self, x, y, r, c, grid, visited):
        nb = []
        poss = [(x-1,y), (x+1, y), (x, y-1), (x, y+1)]
        for i,j in poss:
            if (i >= 0 and i < r) and (j >=0 and j < c) and grid[i][j] == "1" and visited[i][j] == False:
                nb.append((i,j))
        return nb

    def numIslands(self, grid) -> int:
        if not grid:
            return 0
        r = len(grid)
        c = len(grid[0])
        visited = [[False]*c for _ in range(r)]
        connected = 0
        for i in range(r):
            for j in range(c):
                if visited[i][j] == True or grid[i][j] == "0":
                    continue
                queue = [(i,j)]
                connected += 1
                #print(i,j, grid[i][j])
                while queue:
                    x,y = queue.pop()
                    visited[x][y] = True
                    queue.extend(self.getNeighbours(x, y, r, c, grid, visited))
                
        return connected

if __name__ == '__main__':
    sol = Solution()

    gd = [ 
        [1,1,1,1,0],
        [1,1,0,1,0],
        [1,1,0,0,0],
        [0,0,0,0,0]
    ]
    r = sol.numIslands(gd)
    print(r)
    