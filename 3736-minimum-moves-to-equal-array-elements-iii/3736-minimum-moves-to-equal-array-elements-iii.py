class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        need = max(nums)
        ops = 0 
        for i in range(len(nums)):
            ops += (need - nums[i])
        return ops 