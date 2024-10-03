import pdb
class Solution():
    def find_max_cross_subarray(self, A, low, mid, high):
        left_sum = float('-inf')
        sum = 0
        max_left, max_right = mid, mid
        for i in range(mid, low-1, -1):
            sum += A[i]
            if sum > left_sum:
                left_sum = sum
                max_left = i
        right_sum = float('-inf')
        sum = 0
        for i in range(mid+1, high+1, 1):
            sum += A[i]
            if sum > right_sum:
                right_sum = sum
                max_right = i
        
        return (max_left, max_right, left_sum + right_sum)
    
    def find_maximum_subarray(self, A, low, high):
        if high == low:
            return (low, high, A[low])
        else:
            mid = (low + high) // 2
            left_low, left_high, left_sum = self.find_maximum_subarray(A, low, mid)
            right_low, right_high, right_sum = self.find_maximum_subarray(A, mid+1, high)
            cross_low, cross_high, cross_sum = self.find_max_cross_subarray(A, low, mid, high)
            if left_sum >= right_sum and left_sum >= cross_sum:
                return (left_low, left_high, left_sum)
            elif right_sum >= left_sum and right_sum >= cross_sum:
                return (right_low, right_high, right_sum)
            else:
                return (cross_low, cross_high, cross_sum)

result = Solution()
print(result.find_maximum_subarray([5,6,-4,3,-8,1,0], 0, 6))