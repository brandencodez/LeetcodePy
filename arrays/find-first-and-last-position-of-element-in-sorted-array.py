#Binary Search

class Solution:
       def searchRange(self, nums, target):
        l=0
        h=len(nums)-1

        while l<=h:
            mid=(l+h)//2
            if nums[l]==nums[h]==target:
                return [l,h]
            if target> nums[mid]:
                l=mid+1
            elif target < nums[mid]:
                h=mid-1
            else: 
                if nums[l]!= target:           #condition for checking 1st occurence 
                    l+=1
                if nums[h]!= target:           # condition for checking if actual end
                    h-=1   
        
        return -1, -1
       
        