from collections import defaultdict
import sys
class Solution:
    def minCostClimbingStairs(self, cost):
        def calc_cost(i):
            if i > len(cost) -1:
                return 0
            if dp[i] != -1:
                return dp[i]

            tcost = cost[i]
            dp[i] =  min(calc_cost(i+1), calc_cost(i+2)) + tcost
            
            return dp[i]
    
        dp = [-1]*len(cost)
        return min(calc_cost(0), calc_cost(1))



 
if __name__ == '__main__':
    sol = Solution()
    
    cost = [10, 15, 20]
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    
    print(cost)
    r = sol.minCostClimbingStairs(cost)
    print(r)
    

