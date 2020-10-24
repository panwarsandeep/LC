from collections import defaultdict
class Solution:
    '''
    The idea here is to first store the last occurance of the elements.
    At max the answer can be 26 characters long i.e. a-z
    iterate throug the string (maintain one stack)
    - if the char is not present in stack: check if top of stack is greater than character:
    - - if yes then also check if the stack top char has other occurances later in the string: (how to check this?)
    - - - compare its last occurance with current index of the string. If thats the case, revmoe that char from 
          stack assuming that the char will be later added in the stack at its desired position.
    - - insert the new char in the stack
    This way we'll have desired result in the stack
    '''
    def smallestSubsequence(self, s):
        cmap = {c: i  for i, c in enumerate(s)}
        stk = []
        # dict just to keep track of whether the element is present in stack or not
        # this improves running time from 44ms to 24ms, extra memory though
        #bmask = 0
        for i, ch in enumerate(s):
            if not tdict[ch]:
            #if not bmask & (1 << (ord(ch) - ord('a'))):
                while stk and stk[-1] > ch and cmap[stk[-1]] > i:
                    tdict[stk[-1]] = 0
                    #bmask &= ~(1 << (ord(stk[-1]) - ord('a')))
                    stk.pop()
                stk.append(ch)
                tdict[ch] = 1
                #bmask |= 1 << (ord(ch) - ord('a'))
        return (''.join(stk))



if __name__ == '__main__':
    sol = Solution()
    
    s = "bcabc"
    s = "cbacdcbc"
    print(s)
    r = sol.smallestSubsequence(s)
    print(r)
    

