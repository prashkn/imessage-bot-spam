from py_imessage import imessage
from time import sleep

phone = "1234567890"

message = "string with spaces"

def Convert(string):
    newArray = list(string.split(" "))
    return newArray

newMessage = Convert(message)
for i in range(len(newMessage)):
    guid = imessage.send(phone, newMessage[i])