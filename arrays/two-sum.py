class Solution:
    def twoSum(self, nums, target):
        i=0
        j=len(nums)-1

        for i in range(len(nums)):
            for j in range (len(nums)):
                while nums[i] != nums[j]:
                    if nums[i]+nums[j]== target:
                        return i,j
                    else:
                        i=i+1
                        j=j-1