import heapq  # Allow to sort things easily

grades = [32, 43, 654, 34, 132, 66, 99, 532]
# Gets 3 biggest ones inside grades list
# print(heapq.nlargest(3, grades))

stocks = [
    {'ticker': 'APPL', 'price': 201},
    {'ticker': 'GOOG', 'price': 800},
    {'ticker': 'F', 'price': 54},
    {'ticker': 'MSFT', 'price': 313},
    {'ticker': 'TUNA', 'price': 68}
]

# Get two cheapest stocks
# lambda quick function gets the stock price for each stock

print(heapq.nsmallest(2, stocks, key=lambda stock: stock['price']))
