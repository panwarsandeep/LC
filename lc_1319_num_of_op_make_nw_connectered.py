from collections import defaultdict
class Solution:
    def makeConnected(self, n, conn):
        no_edges = len(conn)
        if no_edges < n - 1:
            # min spanning trea must have n-1 edges
            return -1
        adj_list = defaultdict(list)
        for c in conn:
            adj_list[c[0]].append(c[1])
            adj_list[c[1]].append(c[0])

        #print(adj_list)

        visited = [False]*n
        
        def dfs(i):
            stack = [i]
            while stack:
                e = stack.pop(0)
                for nb in adj_list[e]:
                    if visited[nb] == False:
                        visited[nb] = True
                        # append at the beginning
                        stack[:0] = [nb]


        def get_cc(visited):
            cc = 0
            for i in range(n):
                if visited[i] == False:
                    cc += 1
                    dfs(i)
            return cc

        cc = get_cc(visited)
        extra_edges = no_edges - ((n - 1) - (cc - 1))
        #print(no_edges, extra_edges, cc)
        if extra_edges >= cc - 1:
            return cc -1
        else:
            return -1


 
if __name__ == '__main__':
    sol = Solution()
    
    conn = [[0,1],[0,2],[1,2]]
    n = 4

    n = 11
    conn = [[1,4],[0,3],[1,3],[3,7],[2,7],[0,1],[2,4],[3,6],[5,6],[6,7],[4,7],[0,7],[5,7]]

    n = 6
    conn = [[0,1],[0,2],[0,3],[1,2],[1,3]]

    print(conn, n)
    r = sol.makeConnected(n, conn)
    print(r)