from collections import defaultdict
import sys
class Solution:
    def maximumSum(self, arr):
        def msum(arr):
        
            if not arr:
                return 0
            sum = arr[0]
            max_so_far = arr[0]

            for i in range(1, len(arr)):
                if sum + arr[i] >= 0:
                    sum += arr[i]
                    if max_so_far < sum:
                        max_so_far = sum
                else:
                    sum = arr[i] if arr[i] > 0 else 0

            return max_so_far
        totsum = msum(arr)
        max_so_far = totsum
        print(max_so_far)
        for i in range(1, len(arr)):
            tsum = msum(arr[:i])+ msum(arr[i+1:])
            print(tsum, arr[:i], arr[i+1:])
            if tsum > max_so_far:
                max_so_far = tsum

        return max_so_far
        


if __name__ == '__main__':
    sol = Solution()
    
    arr = [3, -2, 2, 3]
    arr = [-1, -1, -1, -1]
    #arr = [1,-2,-2,3]
    arr = [-7,6,1,2,1,4,-1]
    arr = [0,-5,-6,5,0,-5]
    #arr = [1,-2,0,3]
    arr = [-5,8,-7,12,7,2,-11,6,-1,2,-1,8,-1,0,1]
    r = sol.maximumSum(arr)
    print(r)