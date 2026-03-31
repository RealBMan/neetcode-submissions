class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suf_dp = [1] * len(nums)
        pref_dp = [1] * len(nums)

        final_arr = [0] * len(nums)

        for i in range(1, len(nums)):
            pref_dp[i] = pref_dp[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            suf_dp[i] = suf_dp[i + 1] * nums[i + 1]
        
        for i in range(len(nums)):
            final_arr[i] = pref_dp[i] * suf_dp[i]

        return final_arr
        