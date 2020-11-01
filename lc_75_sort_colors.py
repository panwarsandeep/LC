class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        Naive solution

        zeros = nums.count(1)
        ones = nums.count(2)
        for i in range(zeros):
            nums[i] = 0
        for j in range(zeros, (zeros + ones)):
            nums[j] = 1
        for k in range((zeros + ones), len(nums)):
            nums[k] = 2
        '''

        '''
        Solution with O(1) space and one pass
        '''
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                mid += 1
                low += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
            else:
                mid += 1

        

if __name__ == '__main__':
    sol = Solution()

    nums = [1,2,0,0,0,0,1,2,0,1,0]
    print("init: ", nums)
    sol.sortColors(nums)
    print("ans: ", nums)