class CreditCard:
  MAX_PAYMENT_LIMIT = 3000000

  # 인스턴스 변수 앞에 던더를 붙이면 변수를 숨긴다
  def __init__(self, name, password, payment_limit):
    self.name = name
    self.__password = password
    self.__payment_limit = payment_limit

  @property
  def password(self):
    return "Can not display"

  @password.setter
  def password(self, new_password):
    self.__password = new_password

  @property
  def payment_limit(self):
    return self.__payment_limit

  @payment_limit.setter
  def payment_limit(self, new_payment_limit):
    if new_payment_limit >= 0 and new_payment_limit <= CreditCard.MAX_PAYMENT_LIMIT:
      self.__payment_limit = new_payment_limit
    else:
      print("The limit should be between 0 and 3 million.")


card = CreditCard("kim", "1234", 100000)

print(card.name)
print(card.password)
print(card.payment_limit)

card.name = "lee"
card.password = "1111"
card.payment_limit = -10

print(card.name)
print(card.password)
print(card.payment_limit)




class Person:
  DEFAULT_LIMIT_AGE = 19

  def __init__(self, name, age):
    self.age = age
    self.name = name

  def check_age(self):
    return self.age >= Person.DEFAULT_LIMIT_AGE

class Hof:
  pass
  
  
class Pub:
  pass
  
person1 = Person("kim", 20)
person2 = Person("lee", 18)

print(person1.check_age())
print(person2.check_age())