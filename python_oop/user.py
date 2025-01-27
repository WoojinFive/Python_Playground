class User:
  user_count = 0

  def __init__(self, name, pw, email):
    self.name = name
    self.pw = pw
    self.email = email
    User.user_count += 1

  def checkpw(self, pw):
    if self.pw == pw:
      print("pass")
    else:
      print("fail")

  def __str__(self):
    return "Hello, my name is {}.".format(self.name)


user1 = User("kim", "1234", "kim@gmail.com")
user1.checkpw(user1.pw)

user1.user_count = 55

user2 = User("lee", "5678", "lee@gmail.com")

print(User.user_count)
print(user1.user_count)
print(user2.user_count)

print(user1)

print(user1.name, user1.pw, user1.email)