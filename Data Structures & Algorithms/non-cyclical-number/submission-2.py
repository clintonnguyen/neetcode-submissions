class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sum(n)
        while slow != fast:
            slow = self.sum(slow)
            fast = self.sum(self.sum(fast))
        if fast == 1:
            return True
        return False
    def sum(self, n) -> int:
        output = 0
        while(n > 0):
            output += (n % 10) ** 2
            n //= 10
        return output
            