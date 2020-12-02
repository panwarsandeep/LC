from collections import defaultdict
from sortedcontainers import SortedList
import sys
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if not nums:
            return False
        sl = SortedList()
        for i, n in enumerate(nums):
            fl_it = sl.irange(maximum=n, reverse=True)
            ceil_it = sl.irange(minimum=n, reverse=False)
            try:
                floor = next(fl_it)
            except StopIteration:
                floor = sys.maxsize
            try:
                ceil = next(ceil_it)
            except StopIteration:
                ceil = sys.maxsize
            if abs(ceil - n) <= t or abs(n - floor) <= t:
                return True
            sl.add(n)
            if len(sl) > k:
                sl.discard(nums[i - k])
        return False
if __name__ == '__main__':
    sol = Solution()
    
    nums = [1,2,3,1]
    k = 3
    t = 0
    nums, k, t = ([1,5,9,1,5,9], 2, 3)
    nums, k, t = ([1,0,1,1], 1, 2)
    #nums, k, t = ([8,7,15,1,6,1,9,15], 1, 3)
    print(nums, k, t)
    r = sol.containsNearbyAlmostDuplicate(nums, k, t)
    print(r)