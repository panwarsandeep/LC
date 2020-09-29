class Solution:
    def minAddToMakeValid(self, S):
        stack = 0
        req = 0
        for s in S:
            if s == '(':
                stack += 1
            elif stack:
                stack -= 1
            else:
                req += 1
        req += stack
        return req

if __name__ == '__main__':
    sol = Solution()
    p = "(()"
    p = "((()))"
    p = "()))(("
    #p = "((()((())"
    
    print(p)
    r = sol.minAddToMakeValid(p)
    print(r)