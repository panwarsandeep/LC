from collections import defaultdict
class Solution:
    def allPathsSourceTarget(self, graph):
        def dfs(src, cur_path):
            if src == n - 1:
                res.append(cur_path)
                return
            for nb in graph[src]:
                dfs(nb, cur_path + [nb])

        res = []
        n = len(graph)
        dfs(0, [0])
        return res

        


if __name__ == '__main__':
    sol = Solution()

    graph = [[1,2],[3],[3],[]]
    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    r = sol.allPathsSourceTarget(graph)
    print(r)