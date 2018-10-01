import requests


def ztm():

    site = 'http://87.98.237.99:88/delays?stopId=1066'
    r = requests.get(site)
    p = r.json()
    text = ""
    text += str("Numer: " + str(p['delay'][0]['tripId']) + "\n")
    text += str("Czas przybycia: " + str(p['delay'][0]['estimatedTime']) + "\n")
    text += str("Nazwa lini:" + str(p['delay'][0]['headsign']))
    print "DEBUG: Returning %sn" % text
    return text
