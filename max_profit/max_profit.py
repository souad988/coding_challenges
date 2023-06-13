'''
Write a Python function called max_profit that takes a list of integers, where the i-th integer represents the price of a given stock on day i, and returns the maximum profit you can achieve by buying and selling the stock.

You may complete, at most, two complete buy/sell transactions to maximize profits on a stock.

Input:

prices = [3, 3, 5, 0, 0, 3, 1, 4]
Output: 6

Explanation:

Buy on day 4 (price = 0) and sell on day 6 (price = 3): profit = 3 - 0 = 3. Then buy again on day 7 (price = 1) and sell on day 8 (price = 4): profit = 4 - 1 = 3. Total profit: 3 + 3 = 6.



'''

def max_profit(prices):
    if len(prices) < 2:
        return 0
    
    buy1, buy2 = float('inf'), float('inf')
    profit1, profit2 = 0, 0
    
    for price in prices:
       
        buy1 = min(buy1, price)
        profit1 = max(profit1, price - buy1)
        buy2 = min(buy2, price - profit1)
        profit2 = max(profit2, price - buy2)
        print(price,buy1,profit1,buy2,profit2)
        
    return profit2


def test_max_profit():
    assert max_profit([3, 3, 5, 0, 0, 3, 1, 4]) == 6, "Should be 6"

if __name__ == "__main__":
    print('test runing')
    test_max_profit()
    print("Everything passed")    