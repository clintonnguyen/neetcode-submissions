class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        shash = {}
        thash = {}
        for char in s:
            if char not in shash:
                shash[char] = 1
            else:
                shash[char] += 1
        for char in t:
            if char not in thash:
                thash[char] = 1
            else:
                thash[char] += 1
        return shash == thash
        