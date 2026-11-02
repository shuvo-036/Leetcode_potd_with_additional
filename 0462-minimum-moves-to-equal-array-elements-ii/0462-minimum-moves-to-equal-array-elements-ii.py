class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        middle = nums[(n//2)]
        total=0
        for i in range(n):
            total += abs(nums[i]- middle)
        return total