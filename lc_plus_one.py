class Solution:
    def plusOne(self, digits):
        l = len(digits)
        carry = 1
        for i in range(l-1, -1, -1):
            digits[i] += carry
            carry = 0
            if digits[i]//10 == 1:
                carry = 1
            digits[i] %= 10
            if not carry:
                break
        if carry == 1:
            digits.insert(0,1)
        return digits

if __name__ == '__main__':
    sol = Solution()

    l = [4,3,9,9]
    l = [9]
    print(l)
    o = sol.plusOne(l)
    print(o)