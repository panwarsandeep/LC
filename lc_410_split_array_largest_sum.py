from functools import cmp_to_key
class Solution:
    def splitArray(self, nums, m):
        def get_pieces(nums, val):
            no_pcs = 1 # by default entire array can be considered as single piece
            cur_sum = 0
            for n in nums:
                if cur_sum + n > val:
                    cur_sum = n
                    no_pcs += 1
                else:
                    cur_sum += n
            return no_pcs

        lo = max(nums)
        hi = sum(nums)
        # The max sum can be between total and largest value
        # Need to check if the min between this range can be done using m pieces
        # perform binary search
        while lo < hi:
            mid = lo + (hi - lo) // 2
            no_pieces = get_pieces(nums, mid)
            if no_pieces > m:
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == '__main__':
    sol = Solution()

    nums = [7, 2, 5, 10, 8]
    m = 2
    r = sol.splitArray(nums, m)
    print(r)