class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        brackets = {')':'(','}':'{',']':'['}
        stack = []
        for char in s:
            if char in brackets.values():
                stack.append(char)
            else:
                if len(stack) == 0 or brackets[char] != stack[len(stack)-1]:
                    return False
                else:
                    stack.pop()
        if len(stack) != 0:
            return False
        return True
            