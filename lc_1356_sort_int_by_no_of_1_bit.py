from functools import cmp_to_key
class Solution:
    def sortByBits(self, arr):
        def count_bits(n):
            c = 0
            while n:
                n = n & (n - 1)
                c += 1
            return c
        '''
        def bit_cmp(x, y):
            cb_x = count_bits(x)
            cb_y = count_bits(y)
            if cb_x == cb_y:
                return x - y
            else:
                return cb_x - cb_y
        return sorted(arr, key=cmp_to_key(bit_cmp))
        '''
        '''
        more elegant solution:
        Python's sort works well for list of set i.e.
        [(1,3), (1,1), (1,2), (2,4), (2,1)], the sorted one would be as follows:
        [(1, 1), (1, 2), (1, 3), (2, 1), (2, 4)]
        keeping this in mind, following logic works well
        '''
        #return [j for (i, j) in sorted([(count_bits(i), i) for i in arr])]
        # Using bin is much faster then counting bits
        return [j for (i, j) in sorted([(bin(i).count('1'), i) for i in arr])]


if __name__ == '__main__':
    sol = Solution()

    nums = [0,1,2,3,4,5,6,7,8]
    print("init: ", nums)
    r = sol.sortByBits(nums)
    print("ans: ", r)