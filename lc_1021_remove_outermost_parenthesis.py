class Solution:
    def removeOuterParentheses(self, S):
        stack = []
        ans = ""
        tstr = ""
        for s in S:
            tstr += s
            if s == '(':
                stack.append(s)
            else:
                stack.pop()
                if not stack:
                    ans += tstr[1:-1]
                    tstr = ""
        return ans
 
if __name__ == '__main__':
    sol = Solution()
    p = "(()())(())"
    p = "(()())(())(()(()))"
    p = "()()"
    
    print(p)
    r = sol.removeOuterParentheses(p)
    print(r)