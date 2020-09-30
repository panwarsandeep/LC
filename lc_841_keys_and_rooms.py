from collections import defaultdict
class Solution:
    def canVisitAllRooms(self, rooms):
        visited = [False]*len(rooms)
        
        def dfs(room):
            for r in rooms[room]:
                if visited[r] == False:
                    visited[r] = True
                    dfs(r)
        
        visited[0] = True
        dfs(0)
        if False in visited:
            return False
        else:
            return True


 
if __name__ == '__main__':
    sol = Solution()
    
    room = [[1],[2],[3],[]]
    room = [[1,3],[3,0,1],[2],[0]]
    print(room)
    r = sol.canVisitAllRooms(room)
    print(r)