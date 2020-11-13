from collections import defaultdict
class Solution:
    def searchInsert(self, nums, target):
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                hi = mid -1
            else:
                lo = mid + 1
        return lo

if __name__ == '__main__':
    sol = Solution()

    nums = [1,3,5,6]
    tar = 0

    nums = [1]
    tar = 0
    r = sol.searchInsert(nums, tar)
    print(r)