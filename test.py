class User:
    def __init__(self, user_id, username, password):
        self.id = user_id
        self.username = username
        self.password = password
        self.follower = 0
        self.following = 0

    def follow(self,user):
        self.following += 1
        user.follower += 1



user_1 = User(1,"Abraham","pass")
user_1.username = "KAren"
print(user_1.id)
print(user_1.username)
print(user_1.password)

user_2 = User(2, "Karen","pass2")
user_1.follow(user_2)
print(user_1.follower)
print(user_1.following)
print(user_2.following)
print(user_2.follower)


