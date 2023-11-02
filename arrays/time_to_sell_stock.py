# Naive Approach
# Maximise for first sale, then maximise subsequent sales if not at end
# Problems: there could be a higher profit to be had towards
# the end of the array that a smaller sale needs to be had at the beginning

# Optimal Solution
# Leveraging the surrounding logic that time only moves forward and we can 
# only hold one stock per day, we can calculate the profit using the rule that if
# the value increases from one day to the next its possible to make that profit using a
# buy sell spread. i.e. the max profit is the aggregate of the day to day profit
class Solution:
    def maxProfit(prices: list[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                max_profit += diff
        return max_profit


print(Solution.maxProfit(list([7, 1, 5, 3, 6, 4])))
