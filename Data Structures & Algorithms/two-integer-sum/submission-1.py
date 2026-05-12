class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in complements:
                ans = [nums.index(complement), i]
                return ans
            else:
                complements.append(nums[i])
        