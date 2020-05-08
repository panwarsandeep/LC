#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
from collections import defaultdict
def getPrevMatch(str, map):
    maxl = 0
    l = len(str)
    #iterate all the substr (with removing one char)
    for i in range(l):
        ts = str[:i]+str[i+1:l]
        if map[ts] > maxl:
            maxl = map[ts]
    return maxl

def longestStrChain(words):
    words = sorted(words, key=len)
    map = defaultdict(int)

    res = 0
    for i in range(len(words)):
        map[words[i]] = max(map[words[i]],getPrevMatch(words[i], map)+1)
        if map[words[i]] > res:
            res = map[words[i]]
    return res

if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    #s1 = input()

    #s2 = input()

    st = ["a","b","ba","bca","bda","bdca"]
    #st = ["sgtnz","sgtz","sgz","ikrcyoglz","ajelpkpx","ajelpkpxm","srqgtnz","srqgotnz","srgtnz","ijkrcyoglz"]
    st = ["czgxmxrpx","lgh","bj","cheheex","jnzlxgh","nzlgh","ltxdoxc","bju","srxoatl","bbadhiju","cmpx","xi","ntxbzdr","cheheevx","bdju","sra","getqgxi","geqxi","hheex","ltxdc","nzlxgh","pjnzlxgh","e","bbadhju","cmxrpx","gh","pjnzlxghe","oqlt","x","sarxoatl","ee","bbadju","lxdc","geqgxi","oqltu","heex","oql","eex","bbdju","ntxubzdr","sroa","cxmxrpx","cmrpx","ltxdoc","g","cgxmxrpx","nlgh","sroat","sroatl","fcheheevx","gxi","gqxi","heheex"]
    result = longestStrChain(st)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()