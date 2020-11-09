from collections import defaultdict
import sys
import heapq
class Solution:
    ''' dijkstra with min-heap
    '''
    def maxProbability(self, n, edges, succProb, start, end):
        adj = defaultdict(list)
        for i, d in enumerate(edges):
            adj[d[0]].append([d[1], succProb[i]])
            adj[d[1]].append([d[0], succProb[i]])
        #print(adj)

        dist = [0]*n
        visited = set()
        minheap = [(-1, start)]
        while minheap:
            prob, v = heapq.heappop(minheap)
            prob *= -1
            if v == end:
                return prob
            if v in visited:
                continue
            visited.add(v)
            for nb in adj[v]:
                weight = prob * nb[1]
                if weight > dist[nb[0]]:
                    dist[nb[0]] = weight
                    weight *= -1
                    heapq.heappush(minheap, (weight, nb[0]))
        return dist[end]
        
        ''' dijkstra without min-heap TLE
        def maxProbability(self, n, edges, succProb, start, end):
        def sel_max_ind(dist, visited):
            max_val = -sys.maxsize
            max_ind = -1
            for i, d in enumerate(dist):
                if d > max_val and not visited[i]:
                    max_val = d
                    max_ind = i
            return max_ind

        adj = defaultdict(list)
        for i, d in enumerate(edges):
            adj[d[0]].append([d[1], succProb[i]])
            adj[d[1]].append([d[0], succProb[i]])
        #print(adj)

        dist = [-sys.maxsize]*n
        visited = [False]*n
        dist[start] = 1
        for i in range(n):
            it = sel_max_ind(dist, visited)
            for nb in adj[it]:
                if dist[nb[0]] < dist[it] * nb[1]:
                    dist[nb[0]] = dist[it] * nb[1]
            visited[it] = True
        if dist[end] == -sys.maxsize:
            return 0
        return dist[end]
        '''


if __name__ == '__main__':
    sol = Solution()

    n = 3
    edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.2]
    start = 0
    end = 2

    n = 3
    edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.3]
    start = 0
    end = 2

    '''
    n = 3
    edges = [[0,1]]
    succProb = [0.5]
    start = 0
    end = 2
    '''

    n = 5
    edges = [[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]]
    succProb = [0.37,0.17,0.93,0.23,0.39,0.04]
    start = 3
    end = 4

    
    n = 3
    edges = [[0,1]]
    succProb = [0.5]
    start = 0
    end = 2
    
    r = sol.maxProbability(n, edges, succProb, start, end)
    print(r)