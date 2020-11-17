from collections import defaultdict
import math
class Solution:
    def longestCommonPrefix(self, strs):
        no_words = len(strs)
        if no_words == 0:
            return ""
        prefix = [""]
        for i in range(len(strs[0])):
            tc = strs[0][i]
            for j in range(no_words):
                if i > len(strs[j]) - 1 or strs[j][i] != tc:
                    return ''.join(prefix)
            prefix.append(tc)
        return ''.join(prefix)
            


if __name__ == '__main__':
    sol = Solution()
    
    strs = ["flower","flow","flight"]
    strs = ["dog","racecar","car"]
    print(strs)
    r = sol.longestCommonPrefix(strs)
    print(r)