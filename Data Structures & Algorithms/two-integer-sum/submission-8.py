class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in differences and differences[difference] != i:
                return [differences[difference], i]
            else:
                differences[num] = i

                
