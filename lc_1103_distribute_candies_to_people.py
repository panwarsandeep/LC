import math
class Solution:
    def distributeCandies(self, c, np):
        def series_sum(a, n, d):
            return (n * (2*a + (n-1)*d))/2

        def series_nth(a, n, d):
            return a + (n - 1)*d

        sq = int(math.sqrt(c))
        while True:
            ts = (sq*(sq+1))/2
            if ts < c:
                sq += 1
            else:
                sq -= 1
                break
        ngrp = sq // np
        res = []
        tot = 0
        if ngrp:
            for i in range(1, np+1):
                ss = series_sum(i, ngrp, np)
                if tot + ss > c:
                    ss = c - tot
                res.append(ss)
                tot += ss
                if tot == c:
                    break
        else:
            res = [0]*np
        snth = series_nth(np, ngrp, np) + 1
        diff = c - tot
        for i in range(np):
            if snth  <= diff:
                res[i] += snth
            else:
                res[i] += diff
                break
            diff -= snth
            snth += 1
        res = map(int, res)
        return res

if __name__ == '__main__':
    sol = Solution()
    
    c = 60
    p = 4
    #c = 7
    #p = 4
    c = 10
    p = 3
    c = 600
    p = 40
    r = sol.distributeCandies(c, p)
    print(r)