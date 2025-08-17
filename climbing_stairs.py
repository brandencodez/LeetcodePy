class Solution:
    def climbStairs(self, n):
        hashMap = {}   
        
        def climb(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in hashMap:
                return hashMap[n]
            hashMap[n] = climb(n-1) + climb(n-2)
            return hashMap[n]
        
        return climb(n)