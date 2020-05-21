class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {')':'(', '}':'{', ']':'['}
        fail = False
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if not stack or stack[-1] != map[c]:
                    fail = True
                    break
                stack.pop()
        if stack or fail:
            return False
        else:
            return True


if __name__ == '__main__':
    p = "()[]{}"
    #p = "({}[])"
    #p = "([{}})"
    sol = Solution()
    r = sol.isValid(p)
    print(r)

