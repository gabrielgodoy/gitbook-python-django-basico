from operator import attrgetter


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    # String representation of the object instance
    # This will show when the object is printed
    def __repr__(self):
        return self.name + ':' + str(self.user_id)


users = [
    User('Bucky', 43),
    User('Sally', 5),
    User('Tuna', 61),
    User('Brian', 2),
    User('Joby', 77),
    User('Amanda', 9)
]

for user in users:
    print(user)

print('-----')

# Sorted by name
for user in sorted(users, key=attrgetter('name')):
    print(user)

print('-----')

# Sort by user_id
for user in sorted(users, key=attrgetter('user_id')):
    print(user)
