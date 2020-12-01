from collections import defaultdict

class Solution:
    def cutting_bin_str(self, num):
        maxnum = 2 ** 50 -1
        tpow = 0
        map = {}
        tnum = 0
        while tnum <= maxnum:
            tnum = 5 ** tpow
            map[bin(tnum).replace("0b", "")] = True
            tpow += 1
        result = []
        ans = [maxnum]

        def solve(st, parts):
            if st == len(num):
                if len(parts) < ans[0]:
                    ans[0] = len(parts)
                result.append(parts)
                return
            
            for j in range(st+1, len(num) + 1):
                prefix = num[st:j]
                #print(prefix)
                if prefix in map:
                    solve(j, parts + [prefix])
                
               
        solve(0, [])
        return ans[0] if ans[0] != maxnum else -1
        

        

if __name__ == '__main__':
    sol = Solution()
    
    num = "101101101"
    num = "1111101"
    num = "00000"
    T = int(input())
    for _ in range(T):
        num = input()
        r = sol.cutting_bin_str(num)
        print(r)