from collections import defaultdict
class Solution:
    def findJudge(self, N, trust):
        deg = defaultdict(int)
        for t in trust:
            deg[t[0]] -= 1
            deg[t[1]] += 1
        for i in range(1, N+1):
            if deg[i] == N - 1:
                return i
        return -1

if __name__ == '__main__':
    sol = Solution()

    N = 3
    trust = [[1,3],[2,3],[3,1]]

    N = 2
    trust = [[1,2]]
    r = sol.findJudge(N, trust)
    print(r)