from collections import defaultdict
import heapq
class Solution:
    def maxEvents(self, events):
        events.sort(key = lambda x: (-x[0], x[1]))
        pq = []
        st = events[-1][0]
        end = max([ev[1] for ev in events])
        day = st
        cnt = 0
        while day <= end:
            while events and events[-1][0] <= day:
                valid = events.pop()
                heapq.heappush(pq, valid[1])
            
            while pq and pq[0] < day:
                heapq.heappop(pq)
            
            if pq and pq[0] >= day:
                cnt += 1
                heapq.heappop(pq)
            day += 1
        
        return cnt

if __name__ == '__main__':
    sol = Solution()
    
    inp = [[1,4],[4,4],[2,2],[3,4],[1,1]]
    inp = [[1,10],[2,2],[2,2],[2,2],[2,2]]
    inp = [[1,2],[1,2],[3,3],[1,5],[1,5]]
    inp = [[1,2],[2,2],[3,3],[3,4],[3,4]]
    print(inp)
    r = sol.maxEvents(inp)
    print(r)