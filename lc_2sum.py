#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
from collections import defaultdict

class Solution:
    def twoSum(self, nums, target):
        map = defaultdict(list)
        for i,n in enumerate(nums):
            map[n].append(i)
        res = []

        for i in range(len(nums)):
            t = map[nums[i]].pop(0)
            found = map.get(target-nums[i], None)
            if found and len(found) > 0:
                res.extend([i, found[0]])
                return res
            map[nums[i]].appent(t)
        return res





if __name__ == '__main__':
    sol = Solution()
    
    num = [2, 7, 11, 15]
    t = 9

    num = [1,3,4,2]
    t = 6

    #num = [3,3]
    #t = 6

    s = sol.twoSum(num, t)
    print(s)