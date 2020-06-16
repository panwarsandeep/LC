from collections import defaultdict
import copy
class Solution:
    def canFinish(self, num, preq):
        visited = [False for _ in range(num)]
        track = copy.deepcopy(visited)
        dpreq = defaultdict(list)
        for p in preq:
            dpreq[p[0]].append(p[1])

        def isCycle(i):
            visited[i] = True
            track[i] = True
            if dpreq.get(i, None):
                for nb in dpreq.get(i):
                    if track[nb] == True:
                        return True
                    elif not visited[nb]:
                        if isCycle(nb) == True:
                            return True

            track[i] = False
            return False

        for i in range(num):
            if not visited[i] and isCycle(i) == True:
                return False

        return True


if __name__ == '__main__':
    sol = Solution()

    n = 2
    p = [[1,0]]
    p = [[1,0],[0,1]]
    
    n = 6
    p = [[0,5], [0, 4], [2, 5], [1, 4], [3, 2], [1, 3]]
    
    print(n, p)
    r = sol.canFinish(n, p)
    print(r)
    