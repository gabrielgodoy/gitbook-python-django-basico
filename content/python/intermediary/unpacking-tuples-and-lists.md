a, (b, c), d = [1, [2, 3], 4]
data, item, price = ['December 23, 2015', 'ball', 23]


def drop_first_last(grades):
    first, *middle, last = grades
    average = sum(middle) / len(middle)

    print(average)


# It discards first and last items in the list, and prints the average of all the remaining items
drop_first_last([9, 8, 7, 9, 6, 8, 5, 9, 7, 6, 10])
