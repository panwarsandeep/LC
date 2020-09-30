from collections import defaultdict
class Solution:
    def minRemoveToMakeValid(self, S):
        ind = []
        res = ""
        for i in range(len(S)):
            if S[i] == '(':
                ind.append((i, '('))
            elif S[i] == ')':
                if ind and ind[-1][1] == '(':
                    ind.pop()
                    continue
                ind.append((i, ')'))
            else:
                pass

        for i in range(len(S)):
            if not ind:
                res += S[i:]
                break
            elif i == ind[0][0]:
                ind.pop(0)
                continue
            res += S[i]

        return res

 
if __name__ == '__main__':
    sol = Solution()
    s = "(ab((cd)"
    s = "lee(t(c)o)de)"
    s = "))(("
    s = "a)b(c)d"
    
    print(s)
    r = sol.minRemoveToMakeValid(s)
    print(r)