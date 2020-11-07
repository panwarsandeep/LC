from collections import defaultdict
class Solution:
    def gardenNoAdj(self, n, paths):
        adj = defaultdict(list)
        for p in paths:
            adj[p[0]].append(p[1])
            adj[p[1]].append(p[0])
        
        flowers = [0]*(n + 1)
        for v in range(1, n+1):
            avl_flw = [4,3,2,1]
            for nb in adj[v]:
                if flowers[nb] and flowers[nb] in avl_flw:
                    avl_flw.remove(flowers[nb])
            flowers[v] = avl_flw.pop()
        return flowers[1:]

if __name__ == '__main__':
    sol = Solution()

    paths = [[1,2],[2,3],[3,1]]
    n = 3
    paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
    n = 4
    n = 4
    paths = [[3,4],[4,2],[3,2],[1,3]]
    n = 5
    paths = [[3,4],[4,5],[3,2],[5,1],[1,3],[4,2]]
    r = sol.gardenNoAdj(n, paths)
    print(r)