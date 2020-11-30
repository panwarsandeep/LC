from collections import defaultdict
import math
class Solution:
    def subsets(self, nums):
        subsets = []
        for n in range(len(nums)+1):
            ts = []
            while n:
                # Get the last bit set
                lbit = n & ~(n-1)
                # get the index for last bit set
                ind = int(math.log2(lbit))
                ts.append(nums[ind])
                n = n & (n - 1)
            subsets.append(ts)
        return subsets
        

if __name__ == '__main__':
    sol = Solution()
    
    nums = [1,2,3]
    print(nums)
    r = sol.subsets(nums)
    print(r)