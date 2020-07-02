class Solution:
    def myAtoi(self, st) -> int:
        n = 0
        l = len(st)
        minus = 1
        int_max = 2 ** 31 -1
        int_min = -2**31
        if st == "":
            return 0
        for i in range(l):
            if st[i] != " ":
                break
        if st[i] == '-':
            minus = -1
            i += 1
        elif st[i] == '+':
            i += 1
        t = 10 ** (l-i-1)
        for j in range(i,l):
            if st[j].isnumeric():
                n += int(st[j])*t
                t //= 10
            else:
                n //= 10 ** (l-j)
                break
        n *= minus
        if n > int_max:
            n = int_max
        elif n < int_min:
            n = int_min
        return n

        


if __name__ == '__main__':
    sol = Solution()
    
    nums = "  -42"
    nums = "4193 with words"
    r = sol.myAtoi(nums)
    print(r)