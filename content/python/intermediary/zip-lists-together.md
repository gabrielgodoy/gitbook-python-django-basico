first = ['gabriel', 'jonas', 'willian']
last = ['godoy', 'mendes', 'justen']

names = zip(first, last)  # zip makes a list of tuples pairs
# [('gabriel', 'godoy'), ('jonas', 'mendes'), ('willian', 'justen')]

for list_a, list_b in names:
    print(list_a, list_b)
