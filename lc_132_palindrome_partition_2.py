from collections import defaultdict

class Solution:
    '''
    def minCut(self, s):
        res = [len(s)]
        tres = 0
        def isPalindrom(strng, s, e):
            while s < e:
                if strng[s] != strng[e]:
                    return False
                s += 1
                e -= 1
            return True
    
        def helper(strng, st, res, tres):
            if st == len(strng):
                print("len: ", tres)
                if res[0] > tres - 1 and tres > 1:
                    res[0] = tres - 1
            for i in range(st, len(strng)):
                #print(strng[st:i+1])
                if tres + 1 < res[0] and isPalindrom(strng, st, i):
                    tres += 1
                    helper(strng, i+1, res, tres)
                    tres -= 1
                else:
                    return
        helper(s, 0, res, tres)
        return res[0]
    '''
    def minCut(self, s):
        def isPalindrom(strng, s, e):
            while s < e:
                if strng[s] != strng[e]:
                    return False
                s += 1
                e -= 1
            return True

        slen = len(s)
        dp = [[2001]*slen for _ in range(slen)]

        for l in range(1, slen + 1):
            for i in range(slen-l+1):
                j = l + i - 1
                print(l, i, s[i:l+i])
                if isPalindrom(s, i, j):
                    dp[i][j] = 0
                else:
                    for k in range(i, j):
                        #print(l, i, i+l, k)
                        tval = 1 + dp[i][k]+dp[k+1][j]
                        if dp[i][j] > tval:
                            dp[i][j] = tval
                        if tval == 1:
                            break
        print(dp)
        return dp[0][slen-1]



if __name__ == '__main__':
    sol = Solution()
    
    inp = "aabac"
    #inp = "aaa"
    #inp = ""
    inp = "abaqwerfadfoiuqweorpiquweropquewproqweurpoasdifupaodsfupaosdfuapsdfiasdpoqwerqwerqwerqerqewerwerwerrabaqwerfadfoiuqweorpiquweropquewproqweurpoasdifupaodsfupaosdfuapsdfiasdpoqwerqwerqwerqerqewerwerwerrabaqwerfadfoiuqweorpiquweropquewproqweurpoasdifupaodsfupaosdfuapsdfiasdpoqwerqwerqwerqerqewerwerwerrabaqwerfadfoiuqweorpiquweropquewproqweurpoasdifupaodsfupaosdfuapsdfiasdpoqwerqwerqwerqerqewerwerwerrabaqwerfadfoiuqweorpiquweropquewproqweurpoasdifupaodsfupaosdfuapsdfiasdpoqwerqwerqwerqerqewerwerwerrabaqwerfadfoiuqweorpiquweropquewproqweurpoasdifupaodsfupaosdfuapsdfiasdpoqwerqwerqwerqerqewerwerwerrabaqwerfadfoiuqweorpiquweropquewproqweurpoasdifupaodsfupaosdfuapsdfiasdpoqwerqwerqwerqerqewerwerwerrabaqwerfadfoiuqweorpiquweropquewproqweurpoasdifupaodsfupaosdfuapsdfiasdpoqwerqwerqwerqerqewerwerwerrabaqwerfadfoiuqweorpiquweropquewproqweurpoasdifupaodsfupaosdfuapsdfiasdpoqwerqwerqwerqerqewerwerwerrabaqwerfadfoiuqweorpiquweropquewproqweurpoasdifupaodsfupaosdfuapsdfiasdpoqwerqwerqwerqerqewerwerwerrabaqwerfadfoiuqweorpiquweropquewproqweurpoasdifupaodsfupaosdfuapsdfiasdpoqwerqwerqwerqerqewerwerwerrabaqwerfadfoiuqweorpiquweropquewproqweurpoasdifupaodsfupaosdfuapsdfiasdpoqwerqwerqwerqerqewerwerwerrabaqwerfadfoiuqweorpiquweropquewproqweurpoasdifupaodsfupaosdfuapsdfiasdpoqwerqwerqwerqerqewerwerwerrabaqwerfadfoiuqweorpiquweropquewproqweurpoasdifupaodsfupaosdfuapsdfiasdpoqwerqwerqwerqerqewerwerwerrabaqwerfadfoiuqweorpiquweropquewproqweurpoasdifupaodsfupaosdfuapsdfiasdpoqwerqwerqwerqerqewerwerwerrabaqwerfadfoiuqweorpiquweropquewproqweurpoasdifupaodsfupaosdfuapsdfiasdpoqwerqwerqwerqerqewerwerwerrabaqwerfadfoiuqweorpiquweropquewproqweurpoasdifupaodsfupaosdfuapsdfiasdpoqwerqwerqwerqerqewerwerwerrabaqwerfadfoiuqweorpiquweropquewproqweurpoasdifupaodsfupaosdfuapsdfiasdpoqwerqwerqwerqerqewerwerwerrabaqwerfadfoiuqweorpiquweropquewproqweurpoasdifupaodsfupaosdfuapsdfiasdpoqwerqwerqwerqerqewerwerwerrabaqwerfadfoiuqweorpiquweropquewproqweurpoasdifupaodsfupaosdfuapsdfiasdpoqwerqwerqwerqerqewerwerwerr"
    r = sol.minCut(inp)
    print(r)