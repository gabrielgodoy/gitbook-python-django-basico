income = [10, 30, 75]


def double_money(money):
    return money * 2


# Map runs all items through a function
# map(FUNCTION, ITEMS)
new_income = list(map(double_money, income))  # Run double_money on each item in income

print(new_income)
