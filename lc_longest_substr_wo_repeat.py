#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mlen = 0
        map = {}
        i = 0
        tlen = 0
        print(s)
        thr = 0
        for ts in s:
            idx = map.get(ts,-1)
            if idx >= 0:
                if idx >= thr:
                    tlen = i - idx
                    thr = idx
                else:
                    tlen += 1
            else:
                tlen += 1
            map[ts] = i
            if tlen > mlen:
                mlen = tlen
            print(ts,idx,i,tlen,mlen, thr)
            i += 1

        return mlen

if __name__ == '__main__':
    sol = Solution()
    
    st = "abcabcbb"
    st = "bbbbb"
    st = "pwwkew"
    #st = "abba"
    #st = "tmmzuxt"
    #st = "abcabcbb"
    s = sol.lengthOfLongestSubstring(st)
    print(s)