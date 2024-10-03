import pdb
import random
class Solution():
    def randomized_partition(self, A, p, r):
        i = random.randint(p,r)
        A[r], A[i] = A[i], A[r]
        return self.partition(A, p, r)
    
    def partition(self, A, p, r):
        x = A[r]
        i = p-1
        for j in range(p, r):
            if A[j] <= x:
                i = i+1
                A[i], A[j] = A[j], A[i]
        A[i+1], A[r] = A[r], A[i+1]
        return i+1
    
    def quicksort(self, A, p, r):
        if p < r:
            q = self.randomized_partition(A, p, r)
            self.quicksort(A, p, q-1)
            self.quicksort(A, q+1, r)
        return A

result = Solution()
print(result.quicksort([5,6,4,3,8,1,0], 0, 6))

