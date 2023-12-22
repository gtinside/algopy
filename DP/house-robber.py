from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        self.dp = {}
        return self.letsRob(0, nums)
    

    def letsRob(self, index, nums):
        if index >= len(nums):
            return 0
        
        if index in self.dp:
            return self.dp[index]
        
        money1 = nums[index] + self.letsRob(index + 2, nums)
        money2 = self.letsRob(index + 1, nums)

        self.dp[index] = max(money1, money2)
        return max(money1, money2)
    
print(Solution().rob([1,2,3,1]))
    