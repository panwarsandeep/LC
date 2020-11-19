from collections import defaultdict
import math
class Solution:
    def firstUniqChar(self, s):
        w_dict = defaultdict(int)

        for i in range(len(s)):
            if w_dict[s[i]] > 0:
                w_dict[s[i]] *= -1
            elif w_dict[s[i]] == 0:
                w_dict[s[i]] = i + 1
        
        
        for _, v in w_dict.items():
            if v > 0:
                return v - 1
        '''
        for i, c in enumerate(s):
            if w_dict[c] > 0:
                return i
        '''
        return -1


if __name__ == '__main__':
    sol = Solution()
    
    s = "leetcode"
    #s = "loveleetcode"
    #s = ""
    #s = "aaaaaaaab"
    s = "aadadaad"
    print(s)
    r = sol.firstUniqChar(s)
    print(r)