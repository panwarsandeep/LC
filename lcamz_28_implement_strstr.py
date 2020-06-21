class Solution:
    '''
    Boyer Moore algorithm
    '''
    def strStr(self, hs, nd):
        M = len(nd)
        N = len(hs)
        if M == 0:
            return 0
        right = {}
        for i in range(M):
            right[nd[i]] = i
        
        i = 0
        ind = -1
        
        while i <= N - M:
            skip = 0
            for j in range(M-1, -1, -1):
                if hs[i+j] != nd[j]:
                    skip = max(1, j - right.get(hs[i+j], -1))
                    break
            if skip == 0:
                return i
            i += skip
            
        return ind


if __name__ == '__main__':
    sol = Solution()

    haystack = "hello"
    needle = "ll"

    haystack = "aaaa"
    needle = ""
    
    haystack = "mississippi"
    needle  = "issi"
    print(haystack, needle)
    r = sol.strStr(haystack, needle)
    print(r)
    