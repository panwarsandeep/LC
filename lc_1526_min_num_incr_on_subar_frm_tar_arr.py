from collections import defaultdict
from sortedcontainers import SortedList
import sys
class Solution:
    def minNumberOperations(self, target):
        ans = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i-1]:
                ans += target[i] - target[i-1]
        return ans

if __name__ == '__main__':
    sol = Solution()
    
    nums = [1,2,3,2,1]
    print(nums)
    r = sol.minNumberOperations(nums)
    print(r)