class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0


user_1 = User("001", "angela")
user_2 = User("002", "jack")

print(user_1.id)
print(user_1.username)
print(user_1.followers)

print(user_2.id)
print(user_2.username)
print(user_2.followers)
