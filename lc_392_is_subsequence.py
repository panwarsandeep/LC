from functools import cmp_to_key
class Solution:
    def isSubsequence(self, s, t):
        if len(s) == 0:
            return True
        i = 0
        for ch in t:
            if ch == s[i]:
                i += 1
            if i == len(s):
                return True
        return False


if __name__ == '__main__':
    sol = Solution()

    s = "abc"
    t = "ahbgdc"
    print(s, t)
    r = sol.isSubsequence(s, t)
    print(r)