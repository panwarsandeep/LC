from collections import defaultdict
class Solution:
    '''
    #brute-force solution
    def corpFlightBookings(self, bookings, n):
        map = defaultdict(int)
        for b in bookings:
            for i in range(b[0], b[1]+1):
                map[i] += b[2]
        return [map[i] for i in range(1, n+1)]
    '''
    def corpFlightBookings(self, bookings, n):
        ans = [0]*n
        for bk in bookings:
            ans[bk[0] - 1] += bk[2]
            if bk[1] < n: ans[bk[1]] -= bk[2]
        for i in range(1, n):
            ans[i] += ans[i-1]
        return ans 
    

if __name__ == '__main__':
    sol = Solution()
    
    bookings = [[1,2,10],[2,3,20],[2,5,25]]
    n = 5

    r = sol.corpFlightBookings(bookings, n)
    print(r)