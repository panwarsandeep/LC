class Solution:
    def maxProfit(self, prices):
        l = len(prices)
        i = 0
        min = 0
        max = 0
        pft = 0
        while i < l-1:
            min = prices[i]
            max = min
            i += 1
            while i < l and prices[i] > prices[i-1]:
                if max < prices[i]:
                    max = prices[i]
                i += 1
            if min != max:
                pft += max - min
        return pft
    '''
    Another variant 

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0 
        max_so_far = prices[0]
        min_so_far = prices[0]
        tot_profit = 0
        for p in prices[1:]:
            if p > max_so_far:
                tot_profit += p - max_so_far
                max_so_far = p
            else:
                min_so_far = max_so_far = p
        return tot_profit
        '''

if __name__ == '__main__':
    sol = Solution()
    
    nums = [7,1,5,3,6,4]
    nums = [1,2,3,4,5]
    nums = [7,6,4,3,1]

    r = sol.maxProfit(nums)
    print(r)