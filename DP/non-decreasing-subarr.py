from typing import List

class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        self.memo = {}
        ans = 0
        for i in range(len(nums1)):
            ans = max(ans, self.check(float("-inf"), i, nums1, nums2))

        return ans
        
    

    def check(self, prevValue, index, nums1, nums2):
        if index >= len(nums1):
            return 0
        
        if (prevValue, index) in self.memo:
            return self.memo[(prevValue, index)]
        
        len1 = 0
        if prevValue <= nums1[index]:
            len1 = 1 + self.check(nums1[index], index + 1, nums1, nums2)
        
        len2 = 0
        if prevValue <= nums2[index]:
            len2 = 1 + self.check(nums2[index], index + 1, nums1, nums2)
        
        self.memo[(prevValue, index)] = max(len1, len2)
        return max(len1, len2)



print(Solution().maxNonDecreasingLength([2,3,1], [1,2,1]))