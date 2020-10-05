from collections import defaultdict
import sys
class Solution:
    def minCostClimbingStairs(self, cost):
        first, second = cost[0], cost[1]
        for i in range(2, len(cost)):
            tmp = second
            second = min(first, second) + cost[i]
            first = tmp
        
        return min(first, second)

 
if __name__ == '__main__':
    sol = Solution()
    
    cost = [10, 15, 20]
    #cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    
    print(cost)
    r = sol.minCostClimbingStairs(cost)
    print(r)
    

