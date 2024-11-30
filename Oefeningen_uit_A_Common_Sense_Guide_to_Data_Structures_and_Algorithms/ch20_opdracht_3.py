def find_greatest_profit(array):
    buy_price = array[0]
    greatest_profit = 0

    for price in array:
        potential_profit = price - buy_price

        if price < buy_price:
            buy_price = price

        elif potential_profit > greatest_profit:
            greatest_profit = potential_profit
    
    return greatest_profit

myArray = [10, 7, 5, 8, 11, 2, 6]
print(find_greatest_profit(myArray))