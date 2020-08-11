from py_imessage import imessage
from time import sleep

phone = ""
message = ""

def Convert(string):
    newArray = list(string.split(" "))
    return newArray

newMessage = Convert(message)
for i in range(len(newMessage)):
    guid = imessage.send(phone, newMessage[i])