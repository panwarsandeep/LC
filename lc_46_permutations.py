from collections import defaultdict
class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums):
        def calc_perm(l, r):
            if l == r:
                self.res.append(nums[:])
            for i in range(l, r):
                nums[l], nums[i] = nums[i], nums[l]
                calc_perm(l+1, r)
                nums[l], nums[i] = nums[i], nums[l]
        calc_perm(0, len(nums))
        return self.res
        
        

if __name__ == '__main__':
    sol = Solution()
    
    nums = [1,2,3]
    print(nums)
    r = sol.permute(nums)
    print(r)