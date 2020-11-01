from functools import lru_cache
class Solution:
    ''' 
    DP solution
    
    def canPartition(self, nums):
        tot = sum(nums)
        tsum = tot // 2
        if tot % 2 != 0:
            return False
        
        dp = [[False]*(tsum+1) for _ in range(len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][0] = True
        for i in range(1, tsum+1):
            dp[0][i] = False
        
        for i in range(1, len(nums)+1):
            for j in range(1, tsum+1):
                if nums[i-1] > i:
                    dp[i][j] = dp[i-1][j]
                dp[i][j] = dp[i-1][j] or dp[i-1][i - nums[i-1]]
        for i in range(1, len(nums)+1):
            print(dp[i])
        return dp[-1][-1]
    '''
    # Backtracking and memoization (using LRU cache)
    
    def canPartition(self, nums):
        @lru_cache(None)
        def partition_helper(st, cur_sum, tsum):
            if cur_sum == tsum:
                return True
            if cur_sum > tsum or st >= len(nums):
                return False
    
            found = partition_helper(st+1, cur_sum, tsum) or partition_helper(st+1, cur_sum+nums[st], tsum)
            return found
        tot = sum(nums)
        tsum = tot // 2
        if tot % 2 != 0:
            return False
        return partition_helper(0, 0, tsum)
    
    # Backtracking and memoization (without LRU cache)
    '''
    def canPartition(self, nums):
        def partition_helper(st, nums, cur_sum, tsum):
            if cur_sum == tsum:
                return True
            if cur_sum > tsum or st >= len(nums):
                return False

            if dp[st][cur_sum] != -1:
                #print("dp")
                return dp[st][cur_sum]
            
            found = partition_helper(st+1, nums, cur_sum, tsum) or partition_helper(st+1, nums, cur_sum+nums[st], tsum)
            #print(key, found)
            dp[st][cur_sum] = found
            return found
        tot = sum(nums)
        tsum = tot // 2
        if tot % 2 != 0:
            return False
        dp = [[-1]*(tsum+1) for _ in range(len(nums)+1)]
        return partition_helper(0, nums, 0, tsum)
    '''
    

if __name__ == '__main__':
    sol = Solution()

    nums = [1, 5, 11, 5]
    nums = [1,2,3,5]
    nums = [5,3,2,1]
    nums = [1, 1]
    nums = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]
    r = sol.canPartition(nums)
    print(r)