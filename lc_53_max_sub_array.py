class Solution:
    def maxSubArray(self, nums) -> int:
        maxs = nums[0]
        cur_max = nums[0]

        for n in nums[1:]:
            if n > cur_max and cur_max < 0:
                cur_max = n
            else:
                cur_max += n
            maxs = max(maxs, cur_max)
        return maxs


if __name__ == '__main__':
    sol = Solution()

    n = [-2,1,-3,4,-1,2,1,-5,4]
    
    n = [1, 2]
    r = sol.maxSubArray(n)
    print(r)
