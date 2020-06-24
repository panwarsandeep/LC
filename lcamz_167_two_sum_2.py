class Solution:
    def twoSum(self, num, tar):
        i1 = 0
        i2 = len(num)-1
        while i2 > i1:
            while i2 > i1 and num[i2] + num[i1] > tar:
                i2 -= 1
            if num[i1] + num[i2] == tar:
                break
            i1 += 1
        return i1+1, i2+1

if __name__ == '__main__':
    sol = Solution()
    
    nums = [2,7,11,15]
    tar = 9
    r,s = sol.twoSum(nums, tar)
    print(r,s)