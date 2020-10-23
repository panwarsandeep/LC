from collections import defaultdict
class Solution:
    def reverse(self, x):
        two_pow_31 = 2 ** 31
        max_num = two_pow_31 - 1
        min_num = -1 * two_pow_31
        sign = -1 if x < 0 else 1
        x *= sign
        rev_num = 0
        while x:
            rev_num = rev_num * 10 + x % 10
            x = x // 10
            if (sign == 1 and rev_num > max_num) or \
                (sign == -1 and rev_num > max_num-1):
                rev_num = 0
                break
        return rev_num * sign


   

if __name__ == '__main__':
    sol = Solution()
    
    x = 123
    x = -2147483648
    r = sol.reverse(x)
    print(r)
    

