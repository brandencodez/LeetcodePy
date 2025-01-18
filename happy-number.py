class Solution:
    def isHappy(self, n):
        hashset = set()       # Keep track of visited numbers
        while n != 1:        #condition used to check if equal to 1

            if n in hashset:          
                return False          # i.e repeated numbers
            hashset.add(n)  
            n = self.sum_of_squares(n)  
        return True 

    @staticmethod
    def sum_of_squares(n):
        sum = 0
        while n > 0:
            digit = n % 10        #removing the last digit
            sum += digit*digit  
            n = n // 10                   #remove the last digit from the number
        return sum
