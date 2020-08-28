import heapq

'''
Flattens all the values into one array and heapify that.
since this is min heap, hence keep removing k-1 elements from heap (from top)
after that the top of heap element would be Kth smallest number 
'''

class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        heap = []
        for i in range(n):
            for j in range(n):
                heap.append(matrix[i][j])
        #print(heap)
        
        heapq.heapify(heap)
        #print(heap)
        for i in range(k-1):
            heapq.heappop(heap)
        #print(heap)
        return heap[0]





if __name__ == '__main__':
    sol = Solution()
    
    matrix = [
        [ 1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 8

    matrix = [[1,2],[1,3]]
    k = 2

    matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    k = 15
    r = sol.kthSmallest(matrix, k)
    print(r)