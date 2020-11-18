from collections import defaultdict
import math
class Solution:
    def removeElement(self, nums, val):
        cnt = 0
        i = 0
        j = len(nums) - 1
        if i == j and nums[i] == val:
            nums.clear()
            return 0

        while i < j:
            while j >= 0 and nums[j] == val:
                cnt += 1
                j -= 1
            while i < len(nums) and nums[i] != val:
                i += 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        if len(nums) - cnt == 0 and cnt > 0:
            nums.clear()
            return 0
        return len(nums) - cnt


if __name__ == '__main__':
    sol = Solution()
    
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    nums = [3,2,2,3]
    val = 3
    #nums = [2]
    #val = 2
    #nums = [4, 5]
    #val = 4
    #nums = [1,1,1,1]
    #val = 1
    nums = [3,3]
    val = 5
    print(nums, val)
    r = sol.removeElement(nums, val)
    print(r, nums)