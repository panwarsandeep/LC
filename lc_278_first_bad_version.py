from collections import defaultdict
class Solution:
    def setBadVer(self, ver):
        self.bver = ver
    def isBadVersion(self, ver):
        if ver == self.bver:
            return True
        return False

    def firstBadVersion(self, n):
        lo = 1
        hi = n
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.isBadVersion(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

if __name__ == '__main__':
    sol = Solution()
    n = 5
    bad = 4
    n = 1
    bad = 1
    sol.setBadVer(bad)
    r = sol.firstBadVersion(n)
    print(r)