from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.dp = {}
        return self.check(0, prices, True)
    

    def check(self, index, prices, canBuy):
        if index>= len(prices):
            return 0
        
        if (index, canBuy) in self.dp:
            return self.dp[(index, canBuy)]

        if canBuy:
            profit1 = -prices[index] + self.check(index + 1, prices, False)
            profit2 = self.check(index + 1, prices, True)
            self.dp[(index, canBuy)] = max(profit1, profit2)
            return max(profit1, profit2)
        else:
            profit1 = prices[index] + self.check(index + 1, prices, True)
            profit2 = self.check(index + 1, prices, False)
            self.dp[(index, canBuy)] = max(profit1, profit2)
            return max(profit1, profit2)

print(Solution().maxProfit(prices=[7,1,5,3,6,4]))