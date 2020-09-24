class Solution:
    def scoreOfParentheses(self, S):
        '''
        #Using Stack

        stack = [0]
        for s in S:
            if s == '(':
                stack.append(0)
            else:
                t = stack.pop()
                if t == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += (2*t)
            #print(stack)
        return stack[0]
        '''

        ans = 0
        tmp = 0
        for i in range(len(S)):
            if S[i] == '(':
                tmp += 1
            else:
                tmp -= 1
                if S[i-1] == '(':
                    ans += 2 ** tmp
                    print(i, S[i], tmp, ans)
                    #tmp = 0
        return ans



if __name__ == '__main__':
    sol = Solution()
    p = "(((())))"
    #p = "()()"
    #p = "((()()))"
    p = "(()(()))"
    #p = "(())"

    print(p)
    r = sol.scoreOfParentheses(p)
    print(r)