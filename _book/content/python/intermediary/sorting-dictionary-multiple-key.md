from operator import itemgetter

users = [
    {'fname': 'Rafael', 'lname': 'Fragoso'},
    {'fname': 'Gabriel', 'lname': 'Oliveira'},
    {'fname': 'Gabriel', 'lname': 'Delrey'},
    {'fname': 'Gabriel', 'lname': 'Alvares'},
    {'fname': 'Joao', 'lname': 'Serra'},
    {'fname': 'Tiago', 'lname': 'Godoy'},
    {'fname': 'Paulo', 'lname': 'Gustavo'}
]

# In itemgetter, sort by property fname
# for user in sorted(users, key=itemgetter('fname')):
#     print(user)

print('-----')

# Sort by firstname, and then sort by lastname
for user in sorted(users, key=itemgetter('fname', 'lname')):
    print(user)
