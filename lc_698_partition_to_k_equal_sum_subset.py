class Solution:
    def canPartitionKSubsets(self, nums, k):
        def partitioin_helper(st, nums, visited, k, sum_so_far, tsum):
            if k == 1:
                return True
            
            if sum_so_far == tsum:
                return partitioin_helper(0, nums, visited, k-1, 0, tsum)
            
            for i in range(st, len(nums)):
                if visited[i] == False and sum_so_far + nums[i] <= tsum:
                    visited[i] = True
                    if partitioin_helper(i+1, nums, visited, k, sum_so_far+nums[i], tsum):
                        return True
                    visited[i] = False
            return False

        if k == 0 or sum(nums) % k != 0:
            return False
        tsum = sum(nums) // k
        visited = [False]*len(nums)
        return partitioin_helper(0, nums, visited, k, 0, tsum)

if __name__ == '__main__':
    sol = Solution()

    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    r = sol.canPartitionKSubsets(nums, k)
    print(r)