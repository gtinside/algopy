from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        self.dp = {}
        nums = sorted(nums)
        return self.check(0, nums)
    

    def check(self, index, nums):
        if index >= len(nums):
            return 0
        
        if index in self.dp:
            return self.dp[index]
        
        # pick it
        sum_pick = nums[index]
        next_index = index + 1
        while next_index < len(nums) and nums[next_index] == nums[index]:
            sum_pick += nums[next_index]
            next_index+=1
            
        while next_index < len(nums) and nums[next_index] == nums[index] + 1:
            next_index+=1
        

        sum_pick = sum_pick + self.check(next_index, nums)

        # don't pick it
        don_pick_sum = self.check(index + 1, nums)

        self.dp[index] = max(sum_pick, don_pick_sum)
        return max(sum_pick, don_pick_sum)


print(Solution().deleteAndEarn([2,2,3,3,3,4]))
        