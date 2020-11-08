from collections import defaultdict
class Solution:
    def isBipartite(self, graph):
        def bipartite_helper(src):
            colors[src] = 1
            queue = [src]
            while queue:
                ver = queue.pop()
                for nb in adj[ver]:
                    if colors[nb] == -1:
                        colors[nb] = 1 - colors[ver]
                        queue.append(nb)
                    elif colors[nb] == colors[ver]:
                        return False
            return True
        adj = defaultdict(list)
        no_edges = 0
        for s, d in enumerate(graph):
            adj[s].extend(d)
            # check for self loop
            if s in d:
                return False
            no_edges += len(d)
        # graph with 0 edges is bipartite
        if no_edges == 0:
            return True
        colors = [-1]*len(graph)
        for v in range(len(graph)):
            if colors[v] == -1 and not bipartite_helper(v):
                return False
        return True
            


if __name__ == '__main__':
    sol = Solution()

    graph = [[1,3],[0,2],[1,3],[0,2]]
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    graph = [[1],[0,3],[3],[1,2]]
    graph = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
    r = sol.isBipartite(graph)
    print(r)