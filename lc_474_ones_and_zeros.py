from collections import defaultdict
class Solution:
    def findMaxForm(self, strs, m, n):
        mat = [ [0]*(n+1) for i in range(m+1)]

        '''
        Iterate for entire list:
         - count zeros and ones in each string
         - matrix[m][n] represents max num of strings:
         - - the corresponding index i.e. mat[i][j] represents
         - - max number of possible string for 'i' zeros and 'j' ones
         - e.g. string is "1100" zeros = 2, ones = 2
         - need to run a loop from m to 'num of zeros present in given string'
         - an inner loop from n to 'num of ones present in given string'
         - e.g. m = 5, n = 3 and string = "1100"
         - mat[5][3] = 0 (initially)
         - the string "1100" can only be included if m > = "no of zeros in it" and n > = "no of ones in it"
         - which is true in this case as 5 > 2 and 3 > 2
         - now to check whether inclusion of this string will give any benefit (for the calculation done so far)
         - as per the matrix, mat[5-2][3-2] = mat[3][1] represents the max possible string with 3 zeros and 1 ones
         - now including this string at this stage will represent the mat[5][3].
         - inclusion of this string meaning addition of 1 to mat[5-2][3-2].
         - Now check if the mat[5][3] is already greater (i.e. without including this string) hence following condition
         - max(mat[5][3], mat[5-2][3-2]+1). If yes then update mat[5][3]
         
         - similarly, perform the same calculation for mat[5][2], mat[4][3], mat[4][2], mat[3][3], mat[3][2], mat[2][3], mat[2][2] and update the max
         - stopping at mat[2][2] because there are 2 zeros and 2 ones in the current string, including this string would at least need 2 zeros and 2 ones.



        '''
        for st in strs:
            z = st.count('0')
            o = len(st) - z
            for i in range(m, z-1, -1):
                for j in range(n, o-1, -1):
                    print(i, j, z, o)
                    mat[i][j] = max(mat[i][j], mat[i-z][j-o]+1)
        return mat[m][n]


if __name__ == '__main__':
    sol = Solution()
    
    strs = ["10","0001","111001","1","0"]
    strs = ["1100"]
    m = 5
    n = 3

    r = sol.findMaxForm(strs, m, n)
    print(r)