from collections import defaultdict
from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sum = 0
        myDict = defaultdict(int)
        for num in nums:
            sum += num
            myDict[sum%k]+=1
        

        ans = 0
        for key,value in myDict.items():
            if key != 0:
                ans += value*(value - 1)//2
            else:
                ans += value*(value - 1)//2 
                ans+=value
        
        return ans
        
print(Solution().subarraysDivByK(nums=[4,5,0,-2,-3,1], k = 5))