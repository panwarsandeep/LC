class Solution:
    def peakIndexInMountainArray(self, arr):
        l = len(arr)
        low = 0
        high = l - 1
        mid = (low + high) // 2
        while low <= high:
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                break
            elif arr[mid+1] < arr[mid]:
                high = mid
            else:
                low = mid
            mid = (low + high) // 2
        return mid

if __name__ == '__main__':
    sol = Solution()
    
    h = [0, 1, 0]
    h = [3,4,5,1]
    h = [0,10,5,2]
    #h = [24,69,100,99,79,78,67,36,26,19]
    r = sol.peakIndexInMountainArray(h)
    print(r)
    

