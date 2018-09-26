import requests
import pyowm


def ztm(stop):
    city = str(stop)
    site = 'http://87.98.237.99:88/delays?stopId=1066' \
           #+ str(stop)
    r = requests.get(site)
    p = r.json()
    text = ""
    text += str("Numer: " + str(p['delay'][0]['tripId']) + "\n")
    text += str("Czas przybycia: " + str(p['delay'][0]['estimatedTime']) + "\n")
    text += str("Nazwa lini:" + str(p['delay'][0]['headsign']))

    return (text)
