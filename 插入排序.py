import pdb
class Solution():
    def insert_sort(self, nums):
        n = len(nums)
        if n == 1:
            return nums
        for j in range(1, n):
            key = nums[j]
            i = j-1
            while i >= 0 and nums[i] > key:
                nums[i+1] = nums[i]
                i = i-1
            nums[i + 1] = key
        
        return nums

result = Solution()
print(result.insert_sort([5,6,4,3,8,1,0]))