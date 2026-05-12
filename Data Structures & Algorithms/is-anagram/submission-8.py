class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmp = {}
        for char in s:
            if char not in hashmp:
                hashmp[char] = 1
            else:
                hashmp[char] += 1
        for char in t:
            if char not in hashmp or hashmp[char] == 0:
                return False
            hashmp[char] -= 1
        return True
        