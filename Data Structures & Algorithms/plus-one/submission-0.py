class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for i in range(len(digits)):
            number += digits[i] * (10**(len(digits)-1-i))
        number += 1
        res = []
        while number != 0:
            res.insert(0, number % 10)
            number //= 10
        return res