
def isValid( s: str) -> bool:
        stack = []
        HashMap = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in HashMap:
                if stack and stack[-1] == HashMap[char]:        #check top of stack
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True
    
print(isValid("()"))          