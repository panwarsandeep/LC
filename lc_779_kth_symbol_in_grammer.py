class Solution:
    '''
    Base case:
    N = 1, K = 1 val = 0
    N = 2, K = 1 val = 0
    N = 2, K = 1 val = 1

    visualise the following table:

    1: 0
    2: 0 1
    3: 0 1 1 0
    4: 0 1 1 0 1 0 0 1
    As we can see 3,1 and 3,2 are generated using 2,1 as follows:
    3, 1 = 2, 1
    3, 2 = inverse of 2, 1
    similarly 3, 3 and 3, 4 are generated using 2, 2as follows
    3, 3 = 2, 2
    3, 4 = inverse of 2,2

    Now lets see how to get previous step.
    N will be simply N - 1 since we want to move to previous row.
    calculation for K is as follows:
    if K is odd:

    add '1' to it to make it even and divide by 2
    else
    divide K by 2
    using this we get the previous row value which is used to generate this value i.e. previous N, previous K.
    if K is odd, use the previous value as it is, else
    use the inverse of the previous value.

    Example:
    calculate 3,3 and 3,4
    3,3 => N = 3, K = 3
    here K is odd so previous K = (3+1)/2 = 2
    previous N = 3 - 1 = 2
    previous value = 2,2 which is '1'
    hence 3,3 = 1 (use the previous value since 3 is odd)

    for 3,4 => N = 3, K = 4
    here K is even so previous K = K/2 = 4/2 = 2
    previous N = 3 - 1 = 2
    since K is even here, use the inverted value of 2,2 i.e. '0'
    so 3,4 = 0
    '''
    base = {1:[0, 0], 2:[0, 0, 1]}
    def kthGrammar(self, N, K):
        def iseven(num):
            if num % 2 == 0:
                return True
            return False

        if N <= 2:
            print(N, K)
            return Solution.base[N][K]

        if iseven(K):
            val = self.kthGrammar(N-1, K//2)
            return (val ^ 1)
        else:
            return self.kthGrammar(N-1, (K+1)//2)

if __name__ == '__main__':
    sol = Solution()

    n = 2
    k = 1
    r = sol.kthGrammar(n, k)
    print(r)