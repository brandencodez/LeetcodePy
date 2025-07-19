#Using in-place (modifying the i/p arr only)
class Solution:
    def removeDuplicates(self, nums):
        k = 1
        for i in range(1,len(nums)):
            if nums[i] !=nums[i-1]:
                nums[k] =nums[i]   #place in k position
                k+=1

        return k
    
    
    
# Part 2 (return atleast 2 elements)

class Solution:
    def removeDuplicates(self, nums):
        k = 2

        for i in range(2,len(nums)):  #start from 2 since we need first 2 elements
            if nums[i] != nums[k-2]:   # compare indices of o/p arr since 2 duplicates 
                nums[k] = nums[i]
                k+=1
        return k
    