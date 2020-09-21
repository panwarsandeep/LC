import bisect
class Solution:
    def eventualSafeNodes(self, graph):
        white, gray, black = range(3)
        colors = [white]*len(graph)
        safe_nodes = []
        def has_cycle(g):
            if colors[g] == gray:
                return True
            if colors[g] == black:
                return False
            colors[g] = gray
            for nb in graph[g]:
                if has_cycle(nb):
                    return True
            colors[g] = black
            return False
        
        for g in range(len(graph)):
            has_cycle(g)
        safe_nodes = [i for i in range(len(graph)) if colors[i] == black]

        return safe_nodes

            

        


if __name__ == '__main__':
    sol = Solution()
    
    graph = [[1,2],[2,3],[5],[0],[5],[],[]]

    print(graph)
    r = sol.eventualSafeNodes(graph)
    print(r)