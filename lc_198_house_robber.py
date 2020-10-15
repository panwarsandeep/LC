from collections import defaultdict
class Solution:
    def rob(self, nums):
        dp = [-1]*len(nums)
        def calc_max_amount(ind):
            if ind >= len(nums):
                return 0
            # we have two choices:
            # - include the number at this index
            # - exclude the number at this index
            # try both and take max
            if dp[ind] != -1:
                return dp[ind]
            take_it = nums[ind] + calc_max_amount(ind + 2)
            leave_it = calc_max_amount(ind + 1)
            dp[ind] = max(take_it, leave_it)
            return dp[ind]
        return calc_max_amount(0)

   

if __name__ == '__main__':
    sol = Solution()
    
    h = [1,2,3,4]
    h = [2,7,9,3,1]
    print(h)
    r = sol.rob(h)
    print(r)
    

