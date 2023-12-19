class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        def helper(length):
            if length >high:
                return 0
            
            if length in self.dp:
                return self.dp[length]
            
            res = 0
            if length >=low:
                res = 1
            
            res += helper(length + zero)
            res += helper(length + one)

            res = res % (10**9 + 7)
            self.dp[length] = res

            return res
        
        self.dp = {}
        return helper(0)

print(Solution().countGoodStrings(low=3, high=3, zero=1, one=2))