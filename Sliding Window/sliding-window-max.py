from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        myQ = deque()
        ans = []

        for i in range(len(nums)):
            while myQ and myQ[0] < i-k+1:
                myQ.popleft()
            
            while myQ and nums[myQ[-1]] < nums[i]:
                myQ.pop()
            
            myQ.append(i)
            if i>=k - 1:
                ans.append(nums[myQ[0]])
        
        return ans

sol = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
result = sol.maxSlidingWindow(nums, k)
print(result)