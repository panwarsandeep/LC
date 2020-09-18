from collections import defaultdict
import sys
class Solution:
    def maximumSum(self, arr):
        maxs = -sys.maxsize
        for v in arr:
            if v > maxs:
                maxs = v
        if maxs < 0:
            return maxs

        fwd_path = []
        sum = 0
        full_max = -sys.maxsize
        for v in arr:
            sum = max(v, v + sum)
            fwd_path.append(sum)
            full_max = sum if sum > full_max else full_max

        rev_path = []
        sum = 0
        for v in arr[::-1]:
            sum = max(v, v + sum)
            rev_path.append(sum)

        rev_path.reverse()

        ans = -sys.maxsize
        for i in range(1, len(arr)-1):
            tmp = max(full_max, fwd_path[i-1] + rev_path[i+1])
            ans = tmp if tmp > ans else ans
        return ans
        


if __name__ == '__main__':
    sol = Solution()
    
    arr = [3, -2, 2, 3]
    arr = [-1, -1, -1, -1]
    #arr = [1,-2,-2,3]
    #arr = [-7,6,1,2,1,4,-1]
    #arr = [0,-5,-6,5,0,-5]
    #arr = [1,-2,0,3]
    #arr = [-5,8,-7,12,7,2,-11,6,-1,2,-1,8,-1,0,1]
    print(arr)
    r = sol.maximumSum(arr)
    print(r)