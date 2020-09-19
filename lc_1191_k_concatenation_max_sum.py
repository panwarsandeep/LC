from collections import defaultdict
import sys
class Solution:
    def MODified(func):
        def inner(*args, **kwargs):
            mod = 10**9 + 7
            return func(*args, **kwargs) % mod
        return inner

    @MODified
    def kConcatenationMaxSum(self, arr, k):
        arr_sum = 0
        max_sum = 0
        arr_total = 0
        ans = 0
        for v in arr:
            arr_sum = max(v, v + arr_sum)
            max_sum = max(arr_sum, max_sum)

            arr_total += v
    
    
        print(arr_total, arr_sum, max_sum)
        print("max sum:", max_sum)
        if k == 1:
            return max_sum
        else:
            if arr_total <= 0:
                for v in arr:
                    arr_sum = max(v, v + arr_sum)
                    max_sum = max(arr_sum, max_sum)
                return max_sum
            else:
                return max_sum + (k - 1) * arr_total 

        if arr_total > 0 and k >= 2:
            if k == 2:
                ans = max_sum * 2
            else:
                ans = max_sum * 2 + (k - 2) * arr_total

        return ans
        


if __name__ == '__main__':
    sol = Solution()
    
    arr = [1, -2, 1]
    k = 5
    arr = [-5,-2,0,0,3,9,-2,-5,4]
    k = 5

    print(arr)
    r = sol.kConcatenationMaxSum(arr, k)
    print(r)