from collections import defaultdict

class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        prv = nums[0]
        swp = 1
        dup = 0
        for i, n in enumerate(nums[1:]):
            if n == prv:
                dup += 1
                continue
            prv = n
            nums[i+1], nums[swp] = nums[swp], nums[i+1]
            swp += 1
        return len(nums) - dup

if __name__ == '__main__':
    sol = Solution()
    
    nums = [1,1,2]
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(nums)
    r = sol.removeDuplicates(nums)
    print(r, nums)