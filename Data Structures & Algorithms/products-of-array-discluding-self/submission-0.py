class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        product = 1
        zero_cnt = 0
        for num in nums:
            if num == 0:
                zero_cnt += 1
                continue
            product *= num
        if zero_cnt > 1:
            return output
        for i, c in enumerate(nums):
            if zero_cnt == 1:
                if c == 0:
                    output[i] = product
                else:
                    output[i] = 0
            else:
                output[i] = product // c
        return output
