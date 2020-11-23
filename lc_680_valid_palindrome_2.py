from collections import defaultdict
class Solution:
    def validPalindrome(self, s):
        def pal_helper(s, st, en, match):
            if st >= en:
                return True
            if s[st] == s[en]:
                return pal_helper(s, st+1, en -1, match)
            elif match == 0:
                return pal_helper(s, st+1, en, match+1) or pal_helper(s, st, en-1, match+1)
            
            return False
        return pal_helper(s, 0, len(s)-1, 0)

if __name__ == '__main__':
    sol = Solution()
    
    inp = "abbca"
    inp = "acbbad"
    inp = "aba"
    inp = "ebcbbececabbacecbbcbe"
    print(inp)
    r = sol.validPalindrome(inp)
    print(r)