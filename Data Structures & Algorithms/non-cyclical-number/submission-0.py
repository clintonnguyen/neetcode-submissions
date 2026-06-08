class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()
        while n not in cache:
            cache.add(n)
            n = self.sum(n)
            if n == 1:
                return True
        return False
    def sum(self, n) -> int:
        output = 0
        while(n > 0):
            output += (n % 10) ** 2
            n //= 10
        return output
            