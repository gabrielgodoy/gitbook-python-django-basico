stocks = {
    'GOOG': 520.98,
    'FB': 310.89,
    'YHOO': 130.88,
    'AMZN': 156.77,
    'APPL': 123.43
}

# Get minimum and maximum
# Zipping keys and values

# Like keys and values are two separate lists
# stocks.values() => [520.98, 310.89, 130.88, 156.77, 123.43]
# stocks.keys() => ['GOOG', 'FB', 'YHOO', 'AMZN', 'APPL']

# returns a tuple with min values between stock values
print('Min stock value is', min(zip(stocks.values(), stocks.keys())))

# returns a tuple with max values between stock values
print('Max stock value is', max(zip(stocks.values(), stocks.keys())))

# Sorting by stock value
print('Stocks sorted by stock value', sorted(zip(stocks.values(), stocks.keys())))

# Sorting alphabetically
print('Stocks alphabetically', sorted(zip(stocks.keys(), stocks.values())))
