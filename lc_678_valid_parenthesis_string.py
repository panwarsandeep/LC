class Solution:
    def checkValidString(self, S):
        fstack = 0
        rstack = 0
        tstr = 0
        rstr = 0
        ln = len(S) - 1
        for i in range(len(S)):
            if S[ln - i] == ')':
                fstack += 1
            elif S[ln - i] == '*':
                tstr += 1
            else:
                if fstack:
                    fstack -= 1
                elif tstr > 0:
                    tstr -= 1
                    fstack = 0
                else:
                    return False
            
            if S[i] == '(':
                rstack += 1
            elif S[i] == '*':
                rstr += 1
            else:
                if rstack:
                    rstack -= 1
                elif rstr > 0:
                    rstr -= 1
                    rstack = 0
                else:
                    return False
        return True



if __name__ == '__main__':
    sol = Solution()
    p = "(((())))"
    #p = "()()"
    #p = "((()()))"
    p = "(()(()))"
    #p = "(())"
    p = "()*((*)"
    p = "(*))"
    #p = "(()(()))(()()()))))((((()*()*(())())(()))((*()(*((*(*()))()(())*()()))*)*()))()()(())()(()))())))"
    #p = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"

    print(p)
    r = sol.checkValidString(p)
    print(r)