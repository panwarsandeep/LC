class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        res = 0
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] > s[j]:
                j += 1
                continue
            res += 1
            i += 1
            j += 1
        return res

if __name__ == '__main__':
    sol = Solution()
    
    g = [1, 2]
    s = [1, 2, 3]
    r = sol.findContentChildren(g, s)
    print(r)