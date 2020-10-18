from collections import defaultdict
class Solution:
    '''
    using DP
              h   o   r   s   e
          0   1   2   3   4   5
        -----------------------
      0 | 1   1   1   1   1   1
    r 1 | 1
    o 2 | 1
    s 3 | 1

    row represents word1 and col represents word2
    initialize first column and first row with 1,2,3.... this means if either of the string is empty, the operation required will the the insert
    hence keep adding 1 to previous result.
    run a loop for the len1 x len2 and check each corresponding character
    if the char matches, there is no operation required so the total operation (till now) will be the operation till
    previous state i.e. dp[i-1][j-1]
    if the current char doesn't match the we need to apply one of the three operation i.e. insert, delete or replace and take the minimum of that.
    dp[i][j-1] represents prev state before deleting the char from word1, then add 1 to it for operation cost
    dp[i-1][j] represents prev state before insertion of char in word2 hence keeping the index at i-1, add 1 to it for operation (insert) cost.
    dp[i-1][j-1] represents prev state, before replacing of character from word1 to word2. add cost of operation(replace) 1 to it. 
    finally take minimum of all the three cost.
    '''
    def minDistance(self, word1, word2):
        len1 = len(word1)
        len2 = len(word2)
        dp = [[0]* (len1 + 1) for _ in range(len2+1)]
        for i in range(len1+1):
            dp[0][i] = i
        for j in range(len2 + 1):
            dp[j][0] = j
    
        for i in range(1, len2+1):
            for j in range(1, len1+1):
                if word2[i-1] == word1[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min([dp[i-1][j], dp[i][j-1], dp[i-1][j-1]])
        return dp[len2][len1]

   

if __name__ == '__main__':
    sol = Solution()
    
    w1 = "intention"
    w2 = "execution"
    print(w1, w2)
    r = sol.minDistance(w1, w2)
    print(r)
    

