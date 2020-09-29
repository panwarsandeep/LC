from collections import defaultdict
class Solution:
    '''
    The idea is if the string is at even index (assuming index starting from 0),
    in the final output it'll be reversed else not.
    keep this in mind while appending the string (i.e. reverse or regular order)
    once encounter ')', append this string to the below one (in the stack) but again keeping in mind
    if the index is even or odd.
    final string will be at the bottom of the stack
    '''
    def reverseParentheses(self, S):
        stack = defaultdict(str)
        stk_ptr = -1
        def ins_stack(sp, val):
            if sp % 2 == 0:
                stack[sp] = val + stack[sp]
            else:
                stack[sp] += val

        for s in S:
            if s == '(':
                stk_ptr += 1
            elif s == ')':
                stk_ptr -= 1
                ins_stack(stk_ptr, stack[stk_ptr + 1])
                stack[stk_ptr + 1] = ""
            else:
                ins_stack(stk_ptr, s)
    
        return stack[stk_ptr]
 
if __name__ == '__main__':
    sol = Solution()
    s = "(abcd)"
    s = "(ed(et(oc))el)"
    #s = "(u(love)i)"
    #s = "(abcd)"
    
    print(s)
    r = sol.reverseParentheses(s)
    print(r)