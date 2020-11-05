from functools import cmp_to_key
class Solution:
    def arrangeCoins(self, n):
        l, r = 0, n
        while l <= r:
            t = (l + r) // 2
            print(t)
            val = t * (t + 1) // 2
            if val == n:
                return t
            elif val < n:
                l = t + 1
            else:
                r = t - 1
        return r
        



if __name__ == '__main__':
    sol = Solution()

    n = 65535
    print(n)
    r = sol.arrangeCoins(n)
    print(r)