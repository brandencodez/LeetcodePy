class Solution:
    def rotate(self, nums, k):
        k = k%len(nums)
        nums.reverse()   # reverse entire array
        nums[:k] = reversed(nums[:k])   # reverse the k elements
        nums[k:] = reversed(nums[k:])   # reverse remaining elements