import pdb
class Solution():
    def countingsort(self, A, k):
        pdb.set_trace()
        C = [0] * (k+1)
        B = [0] * len(A)
        for j in range(len(A)):
            C[A[j]] += 1
        for i in range(1,k+1):
            C[i] += C[i-1]
        for j in range(len(A) - 1, -1, -1):
            B[C[A[j]]-1] = A[j]
            C[A[j]] -= 1
        return B
    
result = Solution()
print(result.countingsort(A=[5,6,4,3,8,1,0], k=8))
        