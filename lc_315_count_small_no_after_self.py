from collections import defaultdict
from sortedcontainers import SortedList
import sys

class BIT:
    def __init__(self, size):
        self.bit = [0]* (size+1)
        self.size = size
    def update(self, pos):
        pos += 1
        while pos <= self.size:
            self.bit[pos] += 1
            pos = pos + (pos & ~(pos - 1))
    def query(self, rng):
        sum = 0
        rng += 1
        while rng > 0:
            sum += self.bit[rng]
            rng = rng & (rng - 1)

        return sum

class Solution:
    def countSmaller(self, nums):
        if not nums:
            return []
        snums = sorted(nums)
        map = {}
        rank = 0
        map[snums[0]] = rank
        for i in range(1, len(snums)):
            if snums[i] > snums[i-1]:
                rank += 1
                map[snums[i]] = rank
        
        res = [0]*len(nums)
        bit = BIT(len(nums))
        for i in range(len(nums)-1, -1, -1):
            res[i] = bit.query(map[nums[i]] - 1)
            bit.update(map[nums[i]])
        return res


        
if __name__ == '__main__':
    sol = Solution()
    
    nums = [5,2,6,1]
    print(nums)
    r = sol.countSmaller(nums)
    print(r)