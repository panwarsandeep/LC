from collections import defaultdict
class Solution:
    def sequentialDigits(self, low, high):
        def gen_digits(num):
            if num > high:
                return
            if num >= low:
                res.append(num)
            tmp = int(str(num)[1:])
            if tmp%10 < 9:
                tmp = tmp * 10 + ((tmp % 10) + 1)
            else:
                tmp = 0
                for i in range(1, len(str(num))+2):
                    tmp = tmp * 10 + i
            gen_digits(tmp)

        tmp = str(low)
        first = int(tmp[0])
        print("first", first)
        for i in range(first+1, first + len(tmp)):
            if i > 9:
                first = 0
                for j in range(1, len(str(low))+2):
                    first = first * 10 + j
                break
            first = first * 10 + (i)

        res = []
        gen_digits(first)
        return res
            
        

if __name__ == '__main__':
    sol = Solution()
    
    low = 1000
    high = 13000
    
    low = 8511
    high = 23553

    print(low, high)
    r = sol.sequentialDigits(low, high)
    print(r)