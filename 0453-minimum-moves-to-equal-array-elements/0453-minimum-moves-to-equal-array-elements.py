class Solution:
    def minMoves(self, nums: list[int]) -> int:
        
        min_ele = min(nums)

        ops =0
        for i in range(len(nums)):
            ops += (nums[i] - min_ele)
        return ops