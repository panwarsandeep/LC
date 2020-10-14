from collections import defaultdict
class Solution:
    def heightChecker(self, h):
        t = sorted(h[:])
        ans = 0
        for i in range(len(h)):
            if h[i] != t[i]:
                ans += 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    
    h = [1,1,4,2,1,3]
    r = sol.heightChecker(h)
    print(r)
    

