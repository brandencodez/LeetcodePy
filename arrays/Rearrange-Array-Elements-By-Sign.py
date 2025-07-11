class Solution:
    def rearrangeArray(self, nums):
        arr1 = []
        arr2 = []
        arr3 = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                arr1.append(nums[i])
            if nums[i] < 0:
                arr2.append(nums[i])
        
        for i in range(len(arr1)):    # arrays are equal in length
            arr3.append(arr1[i])
            arr3.append(arr2[i])
            
        return arr3
    

            