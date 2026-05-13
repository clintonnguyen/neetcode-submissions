class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        diff = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in diff and diff[difference] != i:
                return [diff[difference], i]
            else:
                diff[nums[i]] = i
            
        return ans