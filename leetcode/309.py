class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        '''all situations: 1. buy the stock 2. sell the ticket
        3. cooldown '''  
        sell = 0
        buy = -prices[0]
        cooldown = 0
        for i in range(1,n):
            temp = sell
            sell = max(sell, buy + prices[i])
            buy = max(buy, cooldown - prices[i])
            cooldown = temp
            print(f'{i}: sell:{sell}, buy:{buy}, cooldown: {cooldown}, price: {prices[i]}')
        return sell
from typing import List

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables:
        # freeze_profit (f) - profit of the day before cooldown
        # sell_profit (f0) - profit after selling the stock
        # hold_profit (f1) - profit after buying the stock or holding onto the stock bought previously
        freeze_profit, sell_profit, hold_profit = 0, 0, -prices[0]

        # Iterate through the stock prices, starting from the second day
        for current_price in prices[1:]:
            # Update profits for the current day
            # freeze_profit remains as the sell_profit from the previous day
            # sell_profit is the maximum of either keeping the previous sell_profit or selling stock today (hold_profit + current_price)
            # hold_profit is the max of either keeping the stock bought previously or buying new stock after cooldown (freeze_profit - current_price)
            freeze_profit, sell_profit, hold_profit = (
                sell_profit, 
                max(sell_profit, hold_profit + current_price),
                max(hold_profit, freeze_profit - current_price)
            )
            print(f' sell:{sell_profit}, buy:{hold_profit}, cooldown: {freeze_profit}, price:{current_price}')

        # The maximum profit will be after all trades are done, which means no stock is being held, hence sell_profit
        return sell_profit
    
price = [1,2,3,0,2]
solution = Solution()
result = solution.maxProfit(price)
print(result)

a = 1
b = 2


a,b= b+1,a+1
print(a,b)