
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        
        ans =0
        n= len(nums)

        for i in range(n):
            g =0
            l =1
            prod = 1

            for j in range(i,n):

                prod *= nums[j]

                g = math.gcd(g, nums[j])
                l = math.lcm(l, nums[j])

                if prod == g * l:
                    ans = max(ans, j-i+1)
        
        return ans
