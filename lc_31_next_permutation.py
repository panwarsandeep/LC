class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        #print(nums)
        if l == 1:
            return
        li = l-1
        found = True
        while li and nums[li] <= nums[li-1]:
            li -= 1

        
        if l > 1 and nums[0] >= nums[1] and li == 0:
            found = False
        li -= 1
        print("li",li, found)
        if found:
            ti = self.binary_search(nums, li+1, l-1, nums[li])
            print("ti",ti)
            nums[li], nums[ti] = nums[ti], nums[li]
        
        print(nums, li+1, l-1)
        i = li+1
        j = l-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def binary_search(self, arr, low, high, x): 
        if high >= low: 
            mid = (high + low) // 2 
            if arr[mid] == x: 
                while arr[mid] == x and mid:
                    mid -= 1
                return mid
            elif arr[mid] < x: 
                return self.binary_search(arr, low, mid - 1, x) 
            else: 
                return self.binary_search(arr, mid + 1, high, x) 
        else: 
            return low-1

if __name__ == '__main__':
    
    sol = Solution()
    lst = [1,2,3]
    #lst = [1, 3, 2]
    #lst = [1, 1, 5]
    
    #lst = [1, 1, 1]
    #lst = [3]
    #lst = [2, 0, 1, 5, 4]
    lst = [2, 1, 1, 1]
    #lst = [3, 2, 1]
    lst = [2, 3, 1]
    print(lst)
    sol.nextPermutation(lst)
    print(lst)
    
    '''
    v = [2,6,5,4,1]
    r = binary_search(v, 1,4, 2)
    print(r)
    '''


