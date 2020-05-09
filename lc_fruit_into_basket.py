#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
from collections import defaultdict
class Solution:
    '''
    # Naive approach, doesn't scale
    
    def totalFruit(self, tree):
        tmp = []
        mlen = 0
        for t in tree:
            tmp.append(t)
            tll = len(tmp)
            tl = len(set(tmp))
            if tl <= 2 and mlen < tll:
                mlen = tll    
            else:
                while len(set(tmp)) > 2:
                    tmp.pop(0)
            
        return mlen
    '''
    def totalFruit(self, tree):
        mlen = 0
        f = tree[0]
        s = None
        tlen = 0
        fl = 0
        sl = 0
        for t in tree:
            if t == f:
                tlen += 1
                sl = 0
                fl += 1
            elif s == None or s == t:
                if s == None:
                    s = t
                fl = 0
                sl += 1
                tlen += 1
            else:
                if mlen < tlen:
                    mlen = tlen
                if fl:
                    tlen = fl
                else:
                    tlen = sl
                    f = s
                fl = 0
                sl = 1
                s = t
                tlen += 1
        if mlen < tlen:
            mlen = tlen
        return mlen

if __name__ == '__main__':
    sol = Solution()
    tree = [3,3,3,1,2,1,1,2,3,3,4]
    tree = [1,2,3,2,2]
    tree = [1,0,3,4,3]

    s = sol.totalFruit(tree)
    print(s)