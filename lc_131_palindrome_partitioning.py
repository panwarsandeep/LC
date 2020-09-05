from collections import defaultdict

class Solution:
    def partition(self, s):
        res = []
        tres = []
        def isPalindrom(strng, s, e):
            while s < e:
                if strng[s] != strng[e]:
                    return False
                s += 1
                e -= 1
            return True
    
        def helper(strng, st, res, tres):
            if st == len(strng):
                res.append(tres[:])
            for i in range(st, len(strng)):
                print(strng[st:i+1])
                if isPalindrom(strng, st, i):
                    tres.append(strng[st:i+1])
                    helper(strng, i+1, res, tres)
                    tres.pop()
        helper(s, 0, res, tres)
        return res



if __name__ == '__main__':
    sol = Solution()
    
    inp = "aac"
    #inp = "aaa"
    #inp = ""
    inp = "aba"
    r = sol.partition(inp)
    print(r)