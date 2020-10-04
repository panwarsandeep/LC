from collections import defaultdict
class Solution:
    def splitIntoFibonacci(self, S):
        upper_limit = 2 ** 31 - 1
        def split_fib(s, res):
            if s == ""  and len(res) > 2 and int(res[-1]) == int(res[-2]) + int(res[-3]):
                return True
            if len(res) > 2 and int(res[-1]) != int(res[-2]) + int(res[-3]):
                return False
            if int(res[-1]) >= upper_limit:
                return False

            for i in range(1, len(s)+1):
                if (i > 1 and s[:i][0] == '0'):
                    continue
                res.append(s[:i])
                if split_fib(s[i:], res):
                    return True
                res.pop()
            return False

        res = []
        for i in range(1, len(S)):
            if S[:i][0] == '0' and i > 1:
                continue
            res.append(S[:i])
            #print(res, S[i:])
            if split_fib(S[i:], res) and int(res[-1]) <= upper_limit:
                return res
            res.pop()
        return []

 
if __name__ == '__main__':
    sol = Solution()
    
    inp = "123246492"
    inp = "123456579"
    #inp = "0123"
    #inp = "1101111"
    inp = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
    inp = "3611537383985343591834441270352104793375145479938855071433500231900737525076071514982402115895535257195564161509167334647108949738176284385285234123461518508746752631120827113919550237703163294909"
    print(inp)
    r = sol.splitIntoFibonacci(inp)
    print(r)
    '''
    t = r[0]
    for i, v in enumerate(r[1:]):
        t += v
    print(t)
    print(t == inp)
    i = len(r)
    while r and i > 2:
        if int(r[-1]) != int(r[-2]) + int(r[-3]):
            print("Failed: ", r[-1], r[-2], r[-3])
        r.pop()
        i -= 1
    '''
    

