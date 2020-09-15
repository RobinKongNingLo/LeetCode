class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [0] * (amount + 1)
        for i in range(1, amount + 1):
            min_coin = amount + 1
            for coin in coins:
                if i - coin >= 0:
                    if table[i - coin] == -1: 
                        continue
                    elif table[i - coin] + 1 < min_coin:
                        min_coin = table[i - coin] + 1
            if min_coin == amount + 1: #Which means there is no result
                table[i] = -1
            else:
                table[i] = min_coin
        return table[-1]