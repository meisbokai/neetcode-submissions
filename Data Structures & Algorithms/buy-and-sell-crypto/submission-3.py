class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        h = prices[0]
        l = prices[0]
        profit = 0
        for p in prices:
            if p < l:
                l = p
                h = p
            if p > h:
                h = p
                if h-l > profit:
                    profit = h-l
        return profit