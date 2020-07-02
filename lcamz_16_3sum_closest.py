class Solution:
    def threeSumClosest(self, nums, tar):
        l = len(nums)

        ans = 30001
        nums = sorted(nums)
        for i in range(l-1):
            j = i+1
            k = l-1
            while j < k:
                ts = nums[i] + nums[j] + nums[k]
                if abs(tar - ans) > abs(tar - ts):
                    ans = ts
                if ts < tar:
                    j += 1
                elif ts > tar:
                    k -= 1
                else:
                    j += 1
                    k -= 1
            if ans == tar:
                break
        return ans

if __name__ == '__main__':
    sol = Solution()
    
    nums = [-1, 2, 1, -4]
    tar = 1
    r = sol.threeSumClosest(nums, tar)
    print(r)