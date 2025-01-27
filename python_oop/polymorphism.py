from abc import ABC, abstractmethod

class Message(ABC):
  @abstractmethod
  def print_msg(self):
    pass

  @abstractmethod
  def send_msg(self):
    pass

  
class Email(Message):
  def __init__(self, body, sender):
    self.body = body
    self.sender = sender

  def print_msg(self):
    print("Email body:{}".format(self.body))
  
  def send_msg(self, receiver):
    print("Send mail from {} to {}".format(self.sender, receiver))


class SMS(Message):
  def __init__(self, txt, phone_num):
    self.txt = txt
    self.phone_num = phone_num

  def print_msg(self):
    print("SMS txt:{}".format(self.txt))
  
  def send_msg(self, receiver):
    print("Send SMS from {} to {}".format(self.phone_num, receiver))


class Katok(Message):
  def __init__(self, txt, KatokID):
    self.txt = txt
    self.KatokID = KatokID

  def print_msg(self):
    print("Katok!!: {}".format(self.txt))
  
  def send_msg(self, receiver):
    print("Send Katok to {}".format(receiver))


class MessageSender:
  def __init__(self):
    self.messages = []

  def add_message(self, new_message):
    if isinstance(new_message, Message):
      self.messages.append(new_message)
    else:
      print("Wrong item: {}".format(new_message))

  def send_all(self):
    for message in self.messages:
      message.send_msg(message.receiver)


email1 = Email("email body", "abc@gmail.com")
email1.receiver = "def@gmail.com"

sms1 = SMS("sms txt", "111-222-3333")
sms1.receiver = "333-444-5555"

katok1 = Katok("Katok msg", "John")
katok1.receiver = "Tom"

message_sender1 = MessageSender()
message_sender1.add_message(email1)
message_sender1.add_message(sms1)
message_sender1.add_message(katok1)
message_sender1.add_message("myemail")
message_sender1.send_all()