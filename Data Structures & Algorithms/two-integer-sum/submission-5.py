class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in diff:
                return [diff[difference], i]
            else:
                diff[nums[i]] = i
        
