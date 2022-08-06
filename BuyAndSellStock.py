def maxProfit(prices: list[int]) -> int:
    if len(prices) == 1:
        return 0

    profit = left = 0
    right = 1

    while right < len(prices):
        difference = prices[right] - prices[left]

        if difference >= 0:
            profit = max(difference,profit)
        else:
            left+=1
        right += 1
    return profit


print(maxProfit([7,1,5,3,6,4]))