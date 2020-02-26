def maxProfit(prices):
    '''
        ith element of array = price stock on that day (ith day)
        must buy one and sell one stock for max profit
        must sell stock before buy stock
        this function returns max profit or 0 if there is none
        O(n)
    '''
    # create variables for profit and buy stock
    profit = 0
    # make buy 1st element of array
    buy = prices[0]
    # itereate through array to see all prices
    for price in prices:
        # if price is less then buy, make buy the current price
        if price < buy:
            buy = price
        # if price greater the buy, see if it increases the proft
        elif price - buy > profit:
            profit = price - buy

    # return results
    return profit

if __name__ == "__main__":
    print(maxProfit([7,1,5,3,6,4]))
    print(maxProfit([7,6,5,4,3,2,1]))