class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        currSum = 0
        ans = 0
        freq = {}

        for right in range(len(nums)):
            currSum += nums[right]
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            if right - left + 1 > k:
                currSum -= nums[left]
                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                left += 1

            if right - left + 1 == k and len(freq) == k:
                ans = max(ans, currSum)

        return ans
