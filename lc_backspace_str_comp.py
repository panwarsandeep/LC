# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    '''
    O(1) space and O(N) complexity.
    With O(N) space it is quite easy i.e. keep one additional stack
    '''
    def backspaceCompare(self, S: str, T: str) -> bool:
        S = list(S)
        T = list(T)
        ls = len(S)
        lt = len(T)
        lptr = 0
        for i in range(ls):
            if S[i] == '#':
                if lptr:
                    lptr -= 1
            else:
                S[lptr] = S[i]
                lptr += 1
        rptr = 0
        for i in range(lt):
            if T[i] == '#':
                if rptr:
                    rptr -= 1
            else:
                T[rptr] = T[i]
                rptr += 1

        if lptr != rptr:
            return False
        else:
            for i in range(lptr):
                if S[i] != T[i]:
                    return False
        return True

if __name__ == '__main__':
    S = "ab#c"
    T = "ad#c"

    sol = Solution()
    r = sol.backspaceCompare(S, T)
    print(r)

