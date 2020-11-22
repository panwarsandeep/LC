from collections import defaultdict
class Solution:
    def singleNumber(self, nums):
        res = nums[0]
        for n in nums[1:]:
            res ^= n
        return res
        
        

if __name__ == '__main__':
    sol = Solution()
    
    nums = [2]
    print(nums)
    r = sol.singleNumber(nums)
    print(r)