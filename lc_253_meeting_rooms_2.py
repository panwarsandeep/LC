from collections import defaultdict
import heapq
from queue import PriorityQueue

class Solution:
    '''
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x: x[0])
        pq = []
        heapq.heappush(pq, intervals[0][1])
        for intrv in intervals[1:]:
            if pq[0] <= intrv[0]:
                heapq.heappop(pq)
            
            heapq.heappush(pq, intrv[1])
        return len(pq)
    '''
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        end = 0
        stime = sorted([x[0] for x in intervals])
        etime = sorted([x[1] for x in intervals])
        cnt = 0
        for s in stime:
            if s >= etime[end]:
                cnt -= 1
                end += 1
            
            cnt += 1
        return cnt
            
        
        

if __name__ == '__main__':
    sol = Solution()
    
    inp = [[0, 30],[5, 10],[15, 20]]
    print(inp)
    r = sol.minMeetingRooms(inp)
    print(r)