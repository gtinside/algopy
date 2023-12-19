from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        count1, count2 = nums1.count(0), nums2.count(0)
        
        if count1 == 0 and count2 == 0:
            if sum1 == sum2:
                return sum1
            else:
                return -1
        elif count1 != 0 and count2 != 0:
            return max(sum1 + count1, sum2 + count2)
        elif count1 == 0:
            if sum1 >= sum2 + count2:
                return sum1
            else:
                return -1
        else:
            if sum2 >= sum1 + count1:
                return sum2
            else:
                return -1


print(Solution().minSum([3,2,0,1,0], nums2 = [6,5,0]))
        
            
