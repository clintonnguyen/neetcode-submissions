class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        for char in s:
            if char.isalnum():
                newString = newString + char.lower()
        for i in range(len(newString)//2):
            if newString[i] != newString[len(newString) - 1 - i]:
                return False
        return True

        