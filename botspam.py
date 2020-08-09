from py_imessage import imessage
from time import sleep

phone = "19197986440"

message = "string here"

def Convert(string):
    newArray = list(string.split(" "))
    return newArray

newMessage = Convert(message)
for i in range(len(newMessage)):
    guid = imessage.send(phone, newMessage[i])