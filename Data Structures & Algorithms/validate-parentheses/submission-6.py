class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
        '}':'{', ']':'[', ')':'('
        }
        stack = []
        for char in s:
            if char in brackets.values():
                stack.append(char)
            else:
                if not stack or brackets[char] != stack[-1]:
                    return False
                else:
                    stack.pop()
        return not stack

