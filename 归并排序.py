import pdb
class Solution():
    def merge(self, nums, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid
        L = [num for num in nums[left:mid+1]] + [float('inf')]
        R = [num for num in nums[mid+1:right+1]] + [float('inf')]
        i = j = 0
        for k in range(left, right+1):
            if L[i] <= R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1

    def merge_sort(self, nums, left, right):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(nums, left, mid)
            self.merge_sort(nums, mid+1, right)
            self.merge(nums, left, mid, right)
        return nums

result = Solution()
print(result.merge_sort([5,6,4,3,8,1,0], 0, 6))