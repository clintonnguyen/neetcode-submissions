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
            if char not in hashmp or t.count(char) != hashmp[char]:
                return False
        return True
        