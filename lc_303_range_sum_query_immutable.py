# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

class NumArray:

    def __init__(self, nums):
        self.len = len(nums)
        if self.len > 0:
            self.sums = [nums[0]]
            for i, n in enumerate(nums[1:], 1):
                self.sums.append(self.sums[i-1] + n)
        

    def sumRange(self, i: int, j: int) -> int:
        if i >= 0 and i < self.len and j >= i and j < self.len:
            if i > 0:
                return self.sums[j] - self.sums[i-1]
            else:
                return self.sums[j]
        else:
            return None


if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    i = 0
    j = 5
    r = obj.sumRange(i,j)
    print(r)