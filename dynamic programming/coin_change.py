# 322. Coin Change
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [amount + 1] * (amount + 1)
        res[0] = 0
        
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    res[i] = min(res[i], res[i - coin] + 1)

        if res[amount] == amount + 1:
            return -1
        return res[amount]