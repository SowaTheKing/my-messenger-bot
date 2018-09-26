# coding=utf-8
from google import *
from weather import *
from ztm import *

greeting = (["hi", "hey", "hello"])


def classify(msg):
    msg = msg.lower().strip()

    if (msg == "help"):
        # return "commonly used commands: \n1.Greeting: Hi\n\n2.google <word> (for google search).\n3.weather city_name "
        return """Well, i'm a little chatBot created my evil-programmer (Actually he is just a beginer lol).
        And mine purpose is to server mine master.
        
        In future, i will be armed hackster, internet rouge who is gonna hack just for fun. But for now, i'm not 
        so don't ddos me pls"""

    if (msg in greeting):
        return "Hello! Whats up?"

    if (msg.find("google") == 0):
        # try:
        query = msg.split()[1]
        return search(query, num=10)

    if (msg == "pawel"):
        return """No Paweł to jest kurwa prze-chuj. Jezu co to jest za diabeł, developer pierwsza klasa a jeszcze jaki prztstojny.
        
        No kurwa chciałbym być jak Paweł. Moze nawet nie ten najfajniejszy Maryszczuk, ale bylejaki. I tak lepszy od połowy
        śmierdzących polaczków."""

    if (msg.find("rozklad") == 0):
        return ztm()

    if (msg.find("weather") == 0):
        try:
            city = msg.split()[1]
            return weather(city)
        except:
            return "please enter valid city name"

    return "sorry! I didn't get that"


if __name__ == '__main__':
    while (1):
        msg = raw_input("Enter something: ")
        print(classify(msg))
