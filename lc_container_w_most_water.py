#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
from collections import defaultdict
class Solution:
    def maxArea(self, height) -> int:
        marea = 0
        i = 0
        j = len(height) -1
        #print(height)
        while i < j:
            ta = min(height[i], height[j]) * (j-i)
            if ta > marea:
                marea = ta
                #print(marea, i,j,height[i],height[j])
            
            if height[i] > height[j]:
                th = height[j]
                j -= 1
                while th >= height[j] and j > i:
                    j -= 1
            elif height[i] < height[j]:
                th = height[i]
                i += 1
                while th >= height[i] and i < j:
                    i += 1
            else:
                if i < j:
                    i += 1
                if j < i:
                    j -= 1
        return marea

if __name__ == '__main__':
    sol = Solution()
    
    h = [1,8,6,2,5,4,8,3,7]
    s = sol.maxArea(h)
    print(s)