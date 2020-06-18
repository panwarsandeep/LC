from collections import defaultdict
import copy
class Solution:
    def floodFill(self, image, sr, sc, nc):
        queue = []
        ir = len(image)
        ic = len(image[0])
        visited = [[False]*ic for _ in range(ir)]
        cc = image[sr][sc]
        queue.append([sr, sc])
        def getNb(r,c):
            nb = []
            if r > 0:
                nb.append([r-1, c])
            if r < len(image) - 1:
                nb.append([r+1, c])
            if c > 0:
                nb.append([r, c-1])
            if c < len(image[0])-1:
                nb.append([r,c+1])
            return nb
        
        while queue:
            r,c = queue.pop()
            visited[r][c] = True
            image[r][c] = nc
            nb = getNb(r,c)
            for n in nb:
                if not visited[n[0]][n[1]] and image[n[0]][n[1]] == cc:
                    queue.append(n)

        return image

if __name__ == '__main__':
    sol = Solution()


    img = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2    
    print(img, sr, sc)
    r = sol.floodFill(img, sr, sc, newColor)
    print(r)
    