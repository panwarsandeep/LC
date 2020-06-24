class Solution:
    def missingNumber(self, nums):
        l = len(nums)
        asum = sum(nums)
        ps = (l * (l + 1))//2
        return ps - asum
if __name__ == '__main__':
    sol = Solution()
    
    nums = [9,6,4,2,3,5,7,0,1]
    r = sol.missingNumber(nums)
    print(r)