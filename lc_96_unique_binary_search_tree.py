from collections import defaultdict
class Solution:
    def numTrees(self, n):
        '''
        Need to basically calculate Catalan number for given n
        Cn = C0Cn-1 + C1Cn-1-1 + C2Cn-2 + ... + Cn-1C0
        C0 = 1
        C1 = 1
        C2 = C0C1 + C1C0 = 1*1 + 1*1 = 2
        C3 = C0C2 + C1C1 + C2C0 = 1*2 + 1*1 + 2*1 = 5
        '''
        C = [0]*(n+1)
        C[0] = C[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                C[i] += C[j]*C[i-1-j]
        return C[n]

   

if __name__ == '__main__':
    sol = Solution()
    
    n = 19
    print(n)
    r = sol.numTrees(n)
    print(r)
    

