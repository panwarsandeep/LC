from collections import defaultdict
class Solution:
    '''
    surprisingly the faster solution is as follows:
    nums.sort()
        return nums[len(nums)//2]
    
    Not sure how it is faster, maybe dictionary is slow
    '''
    def majorityElement(self, nums):
        dict = defaultdict(int)
        ans = None
        l = 0
        for n in nums:
            dict[n] += 1
            if dict[n] > l //2:
                ans = n
            l += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    
    nums = [3, 2, 3]
    nums = [2,2,1,1,1,2,2]
    nums = [0]
    nums = [3,3,4]
    
    r = sol.majorityElement(nums)
    print(r)