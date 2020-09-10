class Solution:
    def lemonadeChange(self, bills):
        col = {5:0, 10:0, 20:0}
        for b in bills:
            col[b] += 1
            if b == 5: continue
            if b == 10:
                if col[5] > 0:
                    col[5] -= 1
                else:
                    return False

            if b == 20:
                if col[10] and col[5]:
                    col[10] -= 1
                    col[5] -= 1
                elif col[5] > 2:
                    col[5] -= 3
                else:
                    return False
        print(col)
        return True

if __name__ == '__main__':
    sol = Solution()
    
    bills = [5, 5, 5, 10, 20]
    #bills = [5,5,10,10,20]
    r = sol.lemonadeChange(bills)
    print(r)