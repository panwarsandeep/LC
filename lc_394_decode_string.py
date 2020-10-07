from collections import defaultdict
class Solution:
    def decodeString(self, s):
        stack = []
        tstr = []
        tnum = -1
        for c in s:
            if c == ']':
                tstr = []
                while stack[-1] != '[':
                    tstr.append(stack.pop())
                stack.pop()
                tnum = 0
                base = 1
                while stack and stack[-1].isdigit():
                    tnum += int(stack.pop()) * base
                    base *= 10
                tstr = tstr * tnum
                for ts in tstr[::-1]:
                    stack.append(ts)
            else:
                stack.append(c)
        
        ans = []
        while stack:
            ans = [stack.pop()] + ans
        ans = ''.join(ans)
        return ans





    
if __name__ == '__main__':
    sol = Solution()
    
    s = "3[a]2[bc]"
    s = "3[a2[c]]"
    s = "2[abc]3[cd]ef"
    s = "abc3[cd]xyz"
    s = "3[a]2[b4[F]c]"
    s = "2[ab3[cd]]4[xy]"
    s = "100[leetcode]"
    print(s)
    r = sol.decodeString(s)
    print(r)
    

