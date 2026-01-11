class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted = ""

        for char in s:
            if char.isalnum():
                converted+= char.lower()
        
        rev = converted[::-1]

        if rev == converted:
            return True
        else:
            return False