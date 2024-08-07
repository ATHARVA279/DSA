def max_profit(prices):
    """
    Function to find the maximum profit you can achieve from buying and selling the stock on different days.

    :param prices: List[int] - The array of stock prices.
    :return: int - The maximum profit.
    """
    min_price = float('inf')  # Initialize to a very high value
    max_profit = 0  # Initialize to zero
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

# Example usage:
if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print("Maximum profit is:", max_profit(prices))
