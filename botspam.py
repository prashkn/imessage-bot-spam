from py_imessage import imessage
from time import sleep

phone = "1234567890"

for x in range(10):
    guid = imessage.send(phone, "type your message here" + str(x+1) + " out of 10000000 messages sent")