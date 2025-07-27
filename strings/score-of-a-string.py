def scoreOfString(self, s: str) -> int:
        sum = 0

        for ptr1 in range(len(s)-1):
             ptr2 = ptr1+1
             val_1 = s[ptr1]
             val_2 = s[ptr2]

             asci_val1 = ord(val_1)
             asci_val2 = ord(val_2)
             result = abs(asci_val1 - asci_val2)
             sum+= result
        return sum
