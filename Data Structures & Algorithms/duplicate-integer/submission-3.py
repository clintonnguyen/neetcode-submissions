class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmp = set()
        for num in nums:
            if num in hashmp:
                return True
            else:
                hashmp.add(num)
        return False
