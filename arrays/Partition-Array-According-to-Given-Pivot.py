class Solution:
    def partition_array(self,nums,pivot):
        arr1=[]
        arr2=[]
        p=[]  #storing pivot 
        
        for i in range(len(nums)):
            if nums[i] < pivot:
                arr1.append(nums[i])
            elif nums[i] > pivot:
                arr2.append(nums[i])
            else:
                p.append(nums[i])
        
        arr3= arr1+p+arr2
        return arr3
                
