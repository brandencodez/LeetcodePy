class Solution:
    def threeSum(self, nums):
        arr = []
        nums.sort()

        for i in range(0,len(nums)-1):
             if i > 0 and nums[i] == nums[i-1]:   # duplicate skip
                    continue
             lptr = i+1
             rptr = len(nums)-1

             while lptr < rptr:
                    threeSum = nums[i]+nums[lptr]+nums[rptr]  
                    if threeSum == 0:
                        arr.append([nums[i],nums[lptr],nums[rptr]])
                        lptr+=1
                        rptr-=1

                        # removing duplicate from pointer
                        while lptr < rptr and nums[lptr] == nums[lptr-1]:
                            lptr+=1
                        while lptr < rptr and  nums[rptr] == nums[rptr+1]:
                            rptr-=1
                    
                    elif threeSum > 0:
                        rptr-=1
                    else:
                        lptr+=1

        return arr
    
    


