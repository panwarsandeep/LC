class Solution:
    def removeOuterParentheses(self, S):
        stack = 0
        ans = ""
        tstr = ""
        for s in S:
            tstr += s
            if s == '(':
                stack += 1
            else:
                stack -= 1
                if not stack:
                    ans += tstr[1:-1]
                    tstr = ""
        return ans
 
if __name__ == '__main__':
    sol = Solution()
    p = "(()())(())"
    p = "(()())(())(()(()))"
    #p = "()()"
    
    print(p)
    r = sol.removeOuterParentheses(p)
    print(r)